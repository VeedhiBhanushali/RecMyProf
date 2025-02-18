from pinecone import Pinecone
import os
from dotenv import load_dotenv
from sjsu_professors import SJSU_PROFESSORS
import time
from openai import OpenAI

# Load environment variables
load_dotenv()

def get_embedding(text):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

def create_professor_metadata(professor_data):
    metadata = {
        "first_name": professor_data["first_name"],
        "last_name": professor_data["last_name"],
        "department": professor_data["department"],
        "overall_rating": professor_data["overall_rating"],
        "num_ratings": professor_data["num_ratings"],
        "would_take_again": professor_data["would_take_again"],
        "difficulty": professor_data["difficulty"]
    }
    
    # Get professor's ID from their data
    prof_id = next((k for k, v in SJSU_PROFESSORS.items() if v == professor_data), None)
    
    # Add contact info if available
    if prof_id and "contact_info" in SJSU_PROFESSORS and prof_id in SJSU_PROFESSORS["contact_info"]:
        contact_info = SJSU_PROFESSORS["contact_info"][prof_id]
        metadata["email"] = contact_info.get("email", "")
        metadata["phone"] = contact_info.get("phone", "")
        metadata["research"] = contact_info.get("research", "")
    
    return metadata

def create_professor_text(professor_data):
    # Get professor's ID from their data
    prof_id = next((k for k, v in SJSU_PROFESSORS.items() if v == professor_data), None)
    
    # Get contact info if available
    contact_info = {}
    if prof_id and "contact_info" in SJSU_PROFESSORS and prof_id in SJSU_PROFESSORS["contact_info"]:
        contact_info = SJSU_PROFESSORS["contact_info"][prof_id]

    text = f"""Professor {professor_data['first_name']} {professor_data['last_name']} 
    teaches in the {professor_data['department']} department.
    They have an overall rating of {professor_data['overall_rating']} out of 5.0
    based on {professor_data['num_ratings']} student ratings.
    {professor_data['would_take_again']}% of students would take them again.
    Students rate their difficulty as {professor_data['difficulty']} out of 5.0.
    """
    
    if contact_info:
        if "email" in contact_info:
            text += f"\nEmail: {contact_info['email']}"
        if "phone" in contact_info:
            text += f"\nPhone: {contact_info['phone']}"
        if "research" in contact_info:
            text += f"\nResearch Interests: {contact_info['research']}"
    
    return text

def load_professors_to_pinecone():
    try:
        print("Starting professor upload process...")
        print("Checking environment variables...")
        if not os.getenv('OPENAI_API_KEY'):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        if not os.getenv('PINECONE_API_KEY'):
            raise ValueError("PINECONE_API_KEY not found in environment variables")
        print("Environment variables found")

        # Initialize Pinecone
        print("Initializing Pinecone connection...")
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        index_name = "professors-index"
        namespace = "sjsu"

        print("Getting Pinecone index...")
        # Get the index
        index = pc.Index(index_name)
        
        print("Starting to process professor data...")
        # Prepare professor data
        professors_data = []
        total_professors = len([k for k in SJSU_PROFESSORS.keys() if k != "contact_info"])
        print(f"Found {total_professors} professors to process")

        for prof_id, prof_data in SJSU_PROFESSORS.items():
            if prof_id == "contact_info":
                continue
                
            print(f"Processing professor: {prof_id}")
            text_for_embedding = create_professor_text(prof_data)
            embedding = get_embedding(text_for_embedding)
            
            professors_data.append({
                'id': f"sjsu_prof_{prof_id}",
                'values': embedding,
                'metadata': create_professor_metadata(prof_data)
            })

        # Upload in batches
        batch_size = 100
        for i in range(0, len(professors_data), batch_size):
            batch = professors_data[i:i + batch_size]
            index.upsert(
                vectors=batch,
                namespace=namespace
            )
            print(f"Uploaded batch {i//batch_size + 1} of {(len(professors_data)-1)//batch_size + 1}")
            time.sleep(1)  # Small delay between batches

        print("Successfully loaded all professors into the Pinecone index")
        
        # Verify the upload
        stats = index.describe_index_stats()
        print("\nIndex Statistics after upload:")
        print(stats)

    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Error type: {type(e)}")
        print(f"Error details: {str(e)}")

if __name__ == "__main__":
    load_professors_to_pinecone() 