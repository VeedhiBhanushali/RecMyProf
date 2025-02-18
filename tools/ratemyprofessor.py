import requests
import json
import os
import sys
from dotenv import load_dotenv
from .rmp_client import RMPClient

# Load environment variables
load_dotenv()

# Get the absolute path to the tools directory
tools_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(tools_dir)

# Add both directories to Python path
for path in [tools_dir, parent_dir]:
    if path not in sys.path:
        sys.path.append(path)

# Base URL for the requests
BASE_URL = "https://www.ratemyprofessors.com/graphql"
AUTHORIZATION = os.getenv("RMP_AUTHORIZATION")  # Load Authorization token from .env

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7",
    "Authorization": f"Basic {AUTHORIZATION}",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    # "Cookie": COOKIES,
    "Origin": "https://www.ratemyprofessors.com",
    "Referer": "https://www.ratemyprofessors.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

# Initialize the RMP client
rmp_client = RMPClient()

def load_query_from_file(file_path: str) -> str:
    """
    Load a GraphQL query from a file.

    Args:
        file_path (str): The path to the file containing the GraphQL query.

    Returns:
        str: The GraphQL query as a string.
    """
    
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_path, file_path)
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()

def send_graphql_request(query: str, variables: dict):
    """
    Send a GraphQL request to the RateMyProfessors API.

    Args:
        query (str): The GraphQL query string.
        variables (dict): The variables for the GraphQL query.

    Returns:
        dict: The response from the API in JSON format, or an error message.
    """
    payload = {
        "query": query,
        "variables": variables
    }

    try:
        response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()  # Raises an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def format_university_response(response, limit):
    """
    Format the response for universities to a specific schema.

    Args:
        response (dict): The JSON response from the API.
        limit (int): The maximum number of results to return.

    Returns:
        list: A list of dictionaries containing university details.
    """
    formatted_data = []
    if "data" in response and "newSearch" in response["data"] and "schools" in response["data"]["newSearch"]:
        edges = response["data"]["newSearch"]["schools"]["edges"]
        for edge in edges[:limit]:
            node = edge["node"]
            university_info = {
                "id": node.get("id"),
                "legacyId": node.get("legacyId"),
                "name": node.get("name"),
                "city": node.get("city"),
                "state": node.get("state"),
                "avgRatingRounded": node.get("avgRatingRounded"),
                "numRatings": node.get("numRatings"),
                "departments": [{"id": dept.get("id"), "name": dept.get("name")} for dept in node.get("departments", [])],
                "summary": node.get("summary", {})
            }
            formatted_data.append(university_info)
    return formatted_data

def format_professor_response(response, limit):
    """
    Format the response for professors to a specific schema.

    Args:
        response (dict): The JSON response from the API.
        limit (int): The maximum number of results to return.

    Returns:
        list: A list of dictionaries containing professor details.
    """
    formatted_data = []
    if "data" in response and "newSearch" in response["data"] and "teachers" in response["data"]["newSearch"]:
        edges = response["data"]["newSearch"]["teachers"]["edges"]
        for edge in edges[:limit]:
            node = edge["node"]
            professor_info = {
                "name": f"{node.get('firstName', '')} {node.get('lastName', '')}",
                "department": node.get("department"),
                "school": node.get("school", {}).get("name"),
                "rating": {
                    "overall": node.get("avgRating"),
                    "would_take_again": node.get("wouldTakeAgainPercentRounded"),
                    "difficulty": node.get("avgDifficulty"),
                    "total_ratings": node.get("numRatings")
                },
                "top_tags": node.get("teacherRatingTags", [])[:3]
            }
            formatted_data.append(professor_info)
    return formatted_data

def get_professor(name: str, limit: int = 5):
    """Get professor information using both APIs"""
    # First try the Python API
    result = rmp_client.search_professor(name)
    if result:
        return [result]
        
    # If not found, try the GraphQL API
    query = load_query_from_file('search_professor_by_name.graphql')
    variables = {
        "query": {"text": name},
        "count": limit
    }
    
    response = send_graphql_request(query, variables)
    return format_professor_response(response, limit)

def get_university(university: str, limit: int = 5):
    """
    Get professors by university.

    Args:
        university (str): The name of the university.
        limit (int): The maximum number of results to return.

    Returns:
        list: A list of formatted university details or an error message.
    """
    query = load_query_from_file('search_university_by_name.graphql')
    variables = {
        "query": {"text": university}
    }

    response = send_graphql_request(query, variables)
    return format_university_response(response, limit)


def get_professors_by_university_id(school_id: str, professor_name: str, limit: int = 5):
    """
    Get teachers by school ID.

    Args:
        school_id (str): The ID of the school.
        professor_name (str): The text to search for within the teachers.
        limit (int): The maximum number of results to return.

    Returns:
        list: A list of formatted teacher details or an error message.
    """
    query = load_query_from_file('search_teachers_by_school_id.graphql')
    variables = {
        "query": {"text": professor_name, "schoolID": school_id},
        "count": limit
    }

    response = send_graphql_request(query, variables)
    return format_professor_response(response, limit)

# # Example usage:
# # Example 1: Search for a Professor by Name
# result_professor = get_professor(name="John", limit=1)
# print("Professor Search Result:", result_professor)
# print("----------------------")

# # Example 2: Search for a University by Name
# result_university = get_university(university="Harvard", limit=1)
# print("University Search Result:", result_university)
# print("----------------------")

# # Example 3: Search for Professors by University ID
# result_professors_by_university = get_professors_by_university_id(
#     school_id="U2Nob29sLTQ3NzM=", professor_name="Ha", limit=5
# )
# print("Professors by University ID Result:", result_professors_by_university)
# print("----------------------")


from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent

# Define Pydantic Models for Arguments
class GetProfessorArgs(BaseModel):
    name: str = Field(..., title="The name of the professor to be searched.")
    limit: int = Field(5, title="The maximum number of results to return.")

class GetUniversityArgs(BaseModel):
    university: str = Field(..., title="The name of the university to be searched.")
    limit: int = Field(5, title="The maximum number of results to return.")

class GetProfessorsByUniversityIDArgs(BaseModel):
    school_id: str = Field(..., title="The ID of the school.")
    professor_name: str = Field(..., title="The search field for the professor's name.")
    limit: int = Field(5, title="The maximum number of results to return.")


rate_tools = [
    StructuredTool.from_function(
        func=get_professor,
        name="GetProfessor",
        description="Get a professor by their name.",
        args_schema=GetProfessorArgs,
    ),
    StructuredTool.from_function(
        func=get_university,
        name="GetUniversity",
        description="Get Universities and Their Departments.",
        args_schema=GetUniversityArgs,
    ),
    StructuredTool.from_function(
        func=get_professors_by_university_id,
        name="GetProfessorsByUniversityID",
        description="Get professors by university ID. You can use the GetUniversity tool to get the university ID.",
        args_schema=GetProfessorsByUniversityIDArgs,
    ),
]

# Initialize a ChatOpenAI model
llm = ChatOpenAI(model="gpt-4o-mini")

prompt = hub.pull("hwchase17/openai-tools-agent")

agent = create_tool_calling_agent(
    llm=llm,
    tools=rate_tools,
    prompt=prompt,
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=rate_tools,
    verbose=True,
    handle_parsing_errors=True,
)

def extract_school_and_name(input: str) -> tuple[str, str]:
    """Extract school and professor name from input"""
    input = input.lower()
    
    # Common school abbreviations and their full names
    schools = {
        "sjsu": "SJSU",
        "san jose state": "SJSU",
        "uci": "UCI",
        "uc irvine": "UCI",
        "mit": "MIT",
        "massachusetts institute of technology": "MIT",
        "stanford": "Stanford",
        "harvard": "Harvard",
        "berkeley": "Berkeley",
        "uc berkeley": "Berkeley"
    }
    
    # Find school in input
    school = "SJSU"  # default
    for key, value in schools.items():
        if key in input:
            school = value
            input = input.replace(key, "")  # Remove school name from input
            break
    
    # Extract professor name
    name = input
    removals = [
        "professor",
        "tell me about",
        "show me",
        "what are the ratings for",
        "find",
        "at",
        "prof",
        "dr",
        "dr."
    ]
    
    for text in removals:
        name = name.replace(text, "")
    
    # Clean up extra spaces and punctuation
    name = name.strip()
    name = ' '.join(name.split())  # Remove multiple spaces
    
    print(f"Extracted: Name='{name}', School='{school}'")  # Debug print
    return school, name

def run_tools(input: str, chat_history: list):
    """Process input and return professor information."""
    try:
        # Extract school and professor name from input
        school, name = extract_school_and_name(input)
        print(f"Searching for {name} at {school}")  # Debug print
        
        # Search using RMP client
        result = rmp_client.search_professor(name, school)
        
        # Format the response
        if result:
            prof = result  # Note: result is already a single dict, not a list
            rating_info = prof.get('rating', {})
            
            # Build the response string
            response_parts = [
                f"\nHere's what I found on Rate My Professor:\n",
                f"Professor: {prof['name']}",
                f"Department: {prof.get('department', 'Not specified')}",
                f"School: {prof.get('school', 'Not specified')}"
            ]
            
            if rating_info:
                response_parts.extend([
                    "\nRatings:",
                    f"- Overall: {rating_info.get('overall', 'N/A')}/5.0",
                    f"- Total Ratings: {rating_info.get('total_ratings', 0)}"
                ])
                
                if rating_info.get('would_take_again'):
                    response_parts.append(f"- Would Take Again: {rating_info['would_take_again']}%")
                if rating_info.get('difficulty'):
                    response_parts.append(f"- Difficulty: {rating_info['difficulty']}/5.0")
            
            return "\n".join(response_parts)
            
        return f"I couldn't find any information about Professor {name} at {school}."
        
    except Exception as e:
        return f"Sorry, I encountered an error while searching: {str(e)}"

if __name__ == "__main__":
    from langchain_core.messages import HumanMessage, AIMessage
    chat_history = []
    while True:
        query = input("You: ")
        if query == "exit":
            break
        print("----------------------")
        chat_history.append(HumanMessage(query))
        ai_message =agent_executor.invoke({"input": query, "chat_history": chat_history})["output"]
        print("AI: ", ai_message)
        chat_history.append(AIMessage(ai_message))