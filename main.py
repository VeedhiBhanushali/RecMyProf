# Updated WebSocket App Code

import asyncio
import time
import os
from dotenv import load_dotenv
from typing import Dict, List
from uuid import uuid4

from fastapi import FastAPI, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

from agent import ProfessorRaterAgent
from langchain_core.messages import HumanMessage, AIMessage
from tools import run_tools
from pinecone import Pinecone
from tools.ratemyprof_api.sjsu_professors import SJSU_PROFESSORS, search_professors
from tools.ratemyprof_api.sjsu_professors import format_professor_info

load_dotenv()

# CONSTANTS
SECRET_KEY = os.getenv("SECRET_KEY", "S@MPL3")
SESSION_TIMEOUT = int(os.getenv("SESSION_TIMEOUT", 60))
BUFFER_SIZE = int(os.getenv("BUFFER_SIZE", "1024"))
STREAM = True # os.getenv("STREAM", "False").lower() == "true"

# App Setup
app = FastAPI(
    title="Rate My Professor",
    description="A chatbot that helps you find professors based on your requirements using AI and Rate My Professor DB.",
)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
agent = ProfessorRaterAgent()

# In Memory Storage (Will later be replaced with Redis)
user_sessions: Dict[str, WebSocket] = {}  # Active sessions
chat_history: Dict[str, List[str]] = {}  # Chat history for each session
session_timestamps: Dict[str, float] = {}  # Last active time for each session

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    """
    Serve the chat interface and manage session state.
    """
    # Update WebSocket URL to use the correct port
    ws_url = f"wss://{request.headers.get('host')}/chat"
    
    session_id = request.cookies.get("session_id")
    
    if session_id and session_id in session_timestamps:
        if time.time() - session_timestamps[session_id] > SESSION_TIMEOUT:
            # Clear expired session
            del chat_history[session_id]
            del session_timestamps[session_id]
            session_id = None
    elif session_id and session_id not in session_timestamps:
        session_id = None

    if not session_id:
        session_id = str(uuid4())
    
    # Update session timestamps and chat history
    session_timestamps[session_id] = time.time()
    chat_history[session_id] = []

    response = templates.TemplateResponse(
        "chat.html", 
        {
            "request": request, 
            "ws_url": ws_url
        }
    )
    response.set_cookie("session_id", session_id)
    return response

@app.websocket("/chat")
async def chat_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for handling real-time chat messages.
    """
    try:
        await websocket.accept()
        print("WebSocket connection accepted")

        session_id = websocket.cookies.get("session_id")
        if not session_id:
            print("No session ID found")
            await websocket.close()
            return
        
        if not session_id in chat_history:
            chat_history[session_id] = []
            session_timestamps[session_id] = time.time()
            
        heartbeat_task = asyncio.create_task(send_heartbeat(websocket))
            
        while True:
            try:
                message = await websocket.receive_text()
                if message == "ping":
                    continue
                    
                print(f"Received message: {message}")
                
                # First check if it's a direct professor name query
                message_lower = message.lower()
                professor_found = False
                
                try:
                    # Reset connection state for new query
                    ai_message = None
                    
                    # Check SJSU_PROFESSORS first
                    for prof_id, prof_data in SJSU_PROFESSORS.items():
                        if prof_id == "contact_info":
                            continue
                        full_name = f"{prof_data['first_name']} {prof_data['last_name']}".lower()
                        if message_lower in full_name or full_name in message_lower:
                            response = format_professor_info(prof_data)
                            await websocket.send_text(response)
                            professor_found = True
                            ai_message = response
                            break
                    
                    # If not a direct professor query, check if it's a course query
                    if not professor_found and ("teach" in message_lower or "who" in message_lower) and "cs" in message_lower:
                        response = search_professors(message)
                        await websocket.send_text(response)
                        professor_found = True
                        ai_message = response

                    # If neither professor nor course found, use the agent as fallback
                    if not professor_found:
                        if STREAM:
                            await websocket.send_text("<STREAM>")
                            buffer = ""
                            
                            for chunk in agent.invoke(message, chat_history[session_id]):
                                buffer += chunk
                                if len(buffer) >= BUFFER_SIZE:
                                    await websocket.send_text(buffer)
                                    buffer = ""
                            
                            if buffer:
                                await websocket.send_text(buffer)
                                await websocket.send_text("<END>")
                                ai_message = buffer
                        else:
                            ai_message = agent.invoke(message, chat_history[session_id])
                            await websocket.send_text(ai_message)

                    # Only update chat history if we got a response
                    if ai_message:
                        chat_history[session_id].append(HumanMessage(message))
                        chat_history[session_id].append(AIMessage(ai_message))
                        session_timestamps[session_id] = time.time()
                except Exception as e:
                    print(f"Error processing message: {e}")
                    await websocket.send_text(f"Sorry, I encountered an error: {str(e)}")
                    continue

            except WebSocketDisconnect:
                break
            except Exception as e:
                print(f"Error in message handling: {e}")
                break

    except Exception as e:
        print(f"WebSocket error: {str(e)}")
    finally:
        if 'heartbeat_task' in locals():
            heartbeat_task.cancel()
        try:
            await websocket.close()
        except:
            pass

async def send_heartbeat(websocket: WebSocket):
    """Background task to send heartbeat"""
    try:
        while True:
            await asyncio.sleep(30)
            await websocket.send_text("ping")
    except:
        pass

async def session_cleanup_task():
    """
    Background task to clean up expired sessions.
    """
    while True:
        current_time = time.time()
        expired_sessions = [
            session_id for session_id, timestamp in session_timestamps.items()
            if current_time - timestamp > SESSION_TIMEOUT
        ]
        
        for session_id in expired_sessions:
            del chat_history[session_id]
            del session_timestamps[session_id]

        await asyncio.sleep(60)  # Run cleanup every 60 seconds

@app.on_event("startup")
async def startup_event():
    """
    Event handler to start background tasks.
    """
    asyncio.create_task(session_cleanup_task())

async def get_index_stats():
    """Get statistics about the professors index"""
    try:
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        index = pc.Index("professors-index")
        stats = index.describe_index_stats()
        return stats
    except Exception as e:
        print(f"Error getting index stats: {e}")
        return None

@app.get("/stats")
async def stats():
    """Get index statistics"""
    stats = await get_index_stats()
    if stats:
        return {
            "total_professors": stats.total_vector_count,
            "namespaces": stats.namespaces
        }
    return {"error": "Could not get index statistics"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="debug"  # Enable debug logging
    )
