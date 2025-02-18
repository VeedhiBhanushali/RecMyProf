# Updated WebSocket App Code

import asyncio
import time
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import io
import base64
from dotenv import load_dotenv
from typing import Dict, List
from uuid import uuid4
import base64

from fastapi import FastAPI, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from agent import ProfessorRaterAgent
from langchain_core.messages import HumanMessage, AIMessage
from tools import run_tools
from pinecone import Pinecone
from tools.ratemyprof_api.sjsu_professors import SJSU_PROFESSORS, search_professors
from tools.ratemyprof_api.sjsu_professors import format_professor_info
from analytics.visualization import ProfessorAnalytics
from analytics.predictor import ProfessorPredictor
from analytics.context_matcher import StudentContextMatcher

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

analytics = ProfessorAnalytics()
predictor = ProfessorPredictor()
context_matcher = StudentContextMatcher()

@app.get("/")
async def get(request: Request):
    """
    Serve the chat interface and manage session state.
    """
    # Update WebSocket URL to use the correct port
    ws_url = f"ws://{request.headers.get('host', 'localhost:8001')}/chat"
    
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

@app.get("/test")
async def test():
    return {"message": "Server is running!"}

@app.get("/pref")
async def preferences(request: Request):
    return templates.TemplateResponse("preferences.html", {"request": request})

@app.get("/dash")
async def dashboard(request: Request):
    try:
        stats, plot_url = generate_professor_stats()
        # Get visualizations
        rating_dist = analytics.create_rating_distribution()
        dept_comp = analytics.create_department_comparison()
        corr_matrix = analytics.create_correlation_matrix()
        feedback_analysis = analytics.create_feedback_analysis()
        
        return templates.TemplateResponse(
            "dashboard.html", 
            {
                "request": request, 
                "stats": stats, 
                "rating_dist": rating_dist,
                "dept_comp": dept_comp,
                "corr_matrix": corr_matrix,
                "feedback_analysis": feedback_analysis
            }
        )
    except Exception as e:
        print(f"Dashboard error: {str(e)}")
        return templates.TemplateResponse(
            "dashboard.html",
            {
                "request": request,
                "stats": {
                    "avg_rating": 0,
                    "avg_difficulty": 0,
                    "total_professors": 0,
                    "avg_would_take_again": 0,
                    "departments": {}
                },
                "rating_dist": "",
                "dept_comp": "",
                "corr_matrix": "",
                "feedback_analysis": "",
                "error": "Error generating dashboard"
            }
        )

@app.post("/pref")
async def process_preferences(request: Request):
    form_data = await request.form()
    try:
        preferences = {
            'teaching_style': form_data.get('teaching_style'),
            'min_rating': float(form_data.get('min_rating', 0) or 0),
            'max_difficulty': float(form_data.get('max_difficulty', 5) or 5),
            'department': form_data.get('department'),
            'would_take_again': float(form_data.get('would_take_again', 0) or 0)
        }
        
        # Get student context
        student_context = {
            'international': 'international' in form_data.getlist('context[]'),
            'working': 'working' in form_data.getlist('context[]'),
            'first_gen': 'first_gen' in form_data.getlist('context[]'),
            'esl': 'esl' in form_data.getlist('context[]')
        }
        
        # Get schedule preferences
        schedule_prefs = {
            'early_morning': 'early' in form_data.getlist('timing[]'),
            'evening': 'evening' in form_data.getlist('timing[]'),
            'hybrid': 'hybrid' in form_data.getlist('timing[]'),
            'flexible': 'flexible' in form_data.getlist('timing[]')
        }
        
        matching_professors = filter_professors(preferences)
        
        # Enhance results with context matching and predictions
        for prof in matching_professors:
            # Calculate context match score
            prof['context_score'] = context_matcher.calculate_context_score(
                prof, 
                {'context': student_context, 'schedule': schedule_prefs}
            )
            
            # Predict success likelihood
            prof['success_prediction'] = predictor.predict_success(
                student_context,
                prof
            )
            
            # Adjust final match score
            prof['match_score'] = (
                prof['match_score'] * 0.6 +  # Base match
                prof['context_score'] * 0.3 +  # Context match
                prof['success_prediction'] * 0.1  # Predicted success
            )
        
        return {"professors": matching_professors}
    except ValueError:
        return {"error": "Invalid input values"}, 400
    except Exception as e:
        return {"error": str(e)}, 500

def generate_professor_stats():
    try:
        # Filter out non-professor entries
        professors = {k: v for k, v in SJSU_PROFESSORS.items() if isinstance(v, dict)}
        df = pd.DataFrame.from_dict(professors, orient='index')
        
        # Generate statistics
        stats = {
            'avg_rating': df['overall_rating'].mean(),
            'avg_difficulty': df['difficulty'].mean(),
            'total_professors': len(df),
            'avg_would_take_again': df['would_take_again'].mean(),
            'departments': df['department'].value_counts().to_dict()
        }
        
        # Generate rating distribution plot
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='overall_rating', bins=20)
        plt.title('Distribution of Professor Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        
        # Convert plot to base64
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')
        plt.close()
        
        return stats, plot_url
    except Exception as e:
        print(f"Error generating stats: {e}")
        return {
            'avg_rating': 0,
            'avg_difficulty': 0,
            'total_professors': 0,
            'avg_would_take_again': 0,
            'departments': {}
        }, ''

def filter_professors(preferences):
    all_matches = []
    matching = []
    for prof_id, prof in SJSU_PROFESSORS.items():
        try:
            # Get selected preferences
            selected_prefs = preferences.get('preferences', [])
            
            # Calculate base match score from ratings
            base_score = 0
            if prof['overall_rating'] >= preferences['min_rating']:
                base_score += 30
            if prof['difficulty'] <= preferences['max_difficulty']:
                base_score += 20
            if prof['would_take_again'] >= preferences['would_take_again']:
                base_score += 20
            
            # Check if professor matches selected preferences
            matches_preferences = True
            pref_score = 0
            if selected_prefs:
                prof_tags = set(prof.get('tags', []) + 
                              prof.get('teaching_style', []) + 
                              prof.get('notes', []))
                
                for pref in selected_prefs:
                    # Map preference to relevant keywords
                    keywords = {
                        'attendance_mandatory': ['ATTENDANCE MANDATORY', 'MUST ATTEND'],
                        'assignment_heavy': ['LOTS OF HOMEWORK', 'HEAVY WORKLOAD'],
                        'test_heavy': ['TEST HEAVY', 'MANY QUIZZES'],
                        'participation_heavy': ['PARTICIPATION MATTERS', 'MUST PARTICIPATE'],
                        'great_lecturer': ['AMAZING LECTURES', 'GREAT LECTURER'],
                        'clear_grading': ['CLEAR GRADING', 'FAIR GRADER'],
                        'extra_credit': ['EXTRA CREDIT', 'BONUS POINTS'],
                        'self_study': ['SELF STUDY', 'INDEPENDENT LEARNING'],
                        'easy_grader': ['EASY GRADER', 'FAIR GRADING'],
                        'project_based': ['GROUP PROJECTS', 'PROJECT BASED'],
                        'responsive': ['ACCESSIBLE', 'RESPONSIVE', 'HELPFUL'],
                        'exam_heavy': ['TOUGH EXAMS', 'DIFFICULT TESTS']
                    }
                    
                    # Check if any keywords match professor's tags
                    if any(keyword.lower() in ' '.join(prof_tags).lower() 
                          for keyword in keywords.get(pref, [])):
                        pref_score += 30 / len(selected_prefs)  # Distribute 30 points among preferences
            
            # Calculate total match score
            total_score = base_score + pref_score
            
            # Add department bonus
            if not preferences['department'] or prof['department'] == preferences['department']:
                total_score += 20
            else:
                total_score *= 0.5  # Reduce score for wrong department
            
            prof['match_score'] = total_score
            all_matches.append(prof)
            
        except (KeyError, TypeError) as e:
            print(f"Error processing professor {prof_id}: {e}")
            continue
    
    # Sort by match score and return all professors
    all_matches.sort(key=lambda x: x['match_score'], reverse=True)
    
    # Return top 10 matches
    return all_matches[:10]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="debug"  # Enable debug logging
    )
