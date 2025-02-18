from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
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

def create_sjsu_professors_data():
    professors = [
        {
            "id": "sjsu_prof_leslie_albert",
            "values": None,  # Will be filled with embeddings
            "metadata": {
                "name": "Leslie Albert",
                "university": "San Jose State University",
                "department": "School of Information Systems & Technology",
                "position": "Professor, Director",
                "school": "Lucas College of Business",
                "location": "San Jose, CA",
                "source": "SJSU Faculty Directory",
                "description": """Dr. Leslie Albert is a Professor and Director at the School of Information Systems & Technology 
                in the Lucas College of Business at San Jose State University. She specializes in Information Systems 
                and Technology Management.""",
                "email": "leslie.albert@sjsu.edu",
                "office": "Business Tower",
                "research": ["Information Systems", "Technology Management"],
                "university_id": "sjsu"
            }
        },
        {
            "id": "sjsu_prof_anu_basu",
            "values": None,  # Will be filled with embeddings
            "metadata": {
                "name": "Anu Basu",
                "university": "San Jose State University",
                "department": "School of Global Innovation and Leadership",
                "position": "Professor, Director",
                "school": "Lucas College of Business",
                "location": "San Jose, CA",
                "source": "SJSU Faculty Directory",
                "description": """Dr. Anu Basu is a Professor and Director at the School of Global Innovation and Leadership 
                in the Lucas College of Business at San Jose State University.""",
                "email": "anu.basu@sjsu.edu",
                "office": "Business Tower",
                "university_id": "sjsu"
            }
        },
        {
            "id": "sjsu_prof_simon_rodan",
            "values": None,
            "metadata": {
                "name": "Simon Rodan",
                "university": "San Jose State University",
                "department": "School of Global Innovation and Leadership",
                "position": "Professor",
                "school": "Lucas College of Business",
                "location": "San Jose, CA",
                "source": "SJSU Faculty Directory",
                "description": """Dr. Simon Rodan is a Professor in the School of Global Innovation and Leadership. 
                His research interests include strategic management and organizational learning.""",
                "email": "simon.rodan@sjsu.edu",
                "office": "Business Tower 950",
                "research": ["Strategic Management", "Organizational Learning"],
                "university_id": "sjsu"
            }
        },
        {
            "id": "sjsu_prof_malu_roldan",
            "values": None,
            "metadata": {
                "name": "Malu Roldan",
                "university": "San Jose State University",
                "department": "School of Information Systems & Technology",
                "position": "Professor",
                "school": "Lucas College of Business",
                "location": "San Jose, CA",
                "source": "SJSU Faculty Directory",
                "description": """Dr. Malu Roldan is a Professor in the School of Information Systems & Technology. 
                She specializes in digital innovation and transformation.""",
                "email": "malu.roldan@sjsu.edu",
                "office": "Business Tower 250",
                "research": ["Digital Innovation", "Business Transformation"],
                "university_id": "sjsu"
            }
        },
        {
            "id": "sjsu_prof_philip_heller",
            "values": None,
            "metadata": {
                "name": "Philip Heller",
                "university": "San Jose State University",
                "department": "Computer Science",
                "position": "Professor",
                "school": "College of Science",
                "location": "San Jose, CA",
                "source": "SJSU Faculty Directory",
                "description": """Dr. Philip Heller is a Professor in the Computer Science Department. 
                He specializes in Java programming and software engineering.""",
                "email": "philip.heller@sjsu.edu",
                "office": "MacQuarrie Hall 416",
                "research": ["Java Programming", "Software Engineering"],
                "university_id": "sjsu"
            }
        },
        {
            "id": "sjsu_prof_chris_pollett",
            "values": None,
            "metadata": {
                "name": "Chris Pollett",
                "university": "San Jose State University",
                "department": "Computer Science",
                "position": "Professor",
                "school": "College of Science",
                "location": "San Jose, CA",
                "source": "SJSU Faculty Directory",
                "description": """Dr. Chris Pollett is a Professor in the Computer Science Department. 
                His research focuses on search engines and web crawling technologies.""",
                "email": "chris.pollett@sjsu.edu",
                "office": "MacQuarrie Hall 416",
                "research": ["Search Engines", "Web Crawling", "Algorithms"],
                "university_id": "sjsu"
            }
        }
    ]
    
    # Add embeddings to each professor
    for prof in professors:
        text_for_embedding = f"""
        Professor Information:
        Name: {prof['metadata']['name']}
        University: {prof['metadata']['university']}
        Department: {prof['metadata']['department']}
        Position: {prof['metadata']['position']}
        School: {prof['metadata']['school']}
        Description: {prof['metadata']['description']}
        Contact: {prof['metadata']['email']}
        Location: {prof['metadata']['location']}
        Office: {prof['metadata']['office']}
        """
        prof["values"] = get_embedding(text_for_embedding)
    
    return professors

def test_pinecone():
    try:
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        index_name = "professors-index"
        namespace = "sjsu"  # Define namespace
        
        # List current indexes
        current_indexes = [index.name for index in pc.list_indexes()]
        print(f"Current indexes: {current_indexes}")
        
        # Create or get index
        if index_name not in current_indexes:
            print(f"Creating index: {index_name}")
            pc.create_index(
                name=index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )
            print("Index created successfully!")
            print("Waiting for index to be ready...")
            time.sleep(20)  # Give more time for index to be ready
        
        # Get the index
        index = pc.Index(index_name)
        
        # List existing namespaces
        try:
            print(f"Existing namespaces: {index.describe_index_stats()}")
        except Exception as e:
            print(f"Could not get namespace stats: {e}")
        
        # Delete existing data in namespace
        try:
            index.delete(delete_all=True, namespace=namespace)
            print(f"Cleared existing data in namespace: {namespace}")
        except Exception as e:
            print(f"Note: No existing data to clear in namespace: {namespace}")
        
        # Get and upload SJSU professors data
        print("Generating professor embeddings...")
        sjsu_professors = create_sjsu_professors_data()
        
        print("Uploading professor data...")
        index.upsert(
            vectors=sjsu_professors,
            namespace=namespace
        )
        
        print("SJSU professors data uploaded successfully!")
        print("Waiting for data to be indexed...")
        time.sleep(10)  # Wait for data to be indexed
        
        # Test queries
        test_queries = [
            "Who is Leslie Albert at SJSU?",
            "Tell me about Professor Basu at San Jose State University",
            "Who is Chris Pollett?",
            "Tell me about Philip Heller",
            "What department is Malu Roldan in?",
            "How can I contact Simon Rodan?"
        ]
        
        print("\nVerifying data with test queries...")
        for query in test_queries:
            print(f"\nTesting query: {query}")
            query_embedding = get_embedding(query)
            
            response = index.query(
                namespace=namespace,
                vector=query_embedding,
                top_k=1,
                include_metadata=True
            )
            
            if response.matches:
                match = response.matches[0]
                print(f"Found match: {match.metadata['name']}")
                print(f"Score: {match.score}")
                print(f"University: {match.metadata['university']}")
                print(f"Department: {match.metadata['department']}")
                print(f"Email: {match.metadata['email']}")
                print(f"Description: {match.metadata['description']}")
            else:
                print("No matches found!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Error type: {type(e)}")
        print(f"Error details: {str(e)}")

def verify_data_for_chatbot():
    try:
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        index = pc.Index("professors-index")
        
        # Verify index exists and has data
        stats = index.describe_index_stats()
        print("\nIndex Statistics:")
        print(stats)
        
        # Test a simple query that matches the chatbot's format
        test_query = "Who is Leslie Albert at San Jose State University?"
        query_embedding = get_embedding(test_query)
        
        response = index.query(
            namespace="sjsu",
            vector=query_embedding,
            top_k=1,
            include_metadata=True
        )
        
        if response.matches:
            print("\nTest Query Results:")
            print(f"Query: {test_query}")
            print(f"Found: {response.matches[0].metadata['name']}")
            print(f"Score: {response.matches[0].score}")
            print("Data is properly stored and retrievable!")
        else:
            print("No matches found. Data might not be properly stored.")
            
    except Exception as e:
        print(f"Verification failed: {e}")

def verify_all_professors():
    try:
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        index = pc.Index("professors-index")
        
        # Get all professors
        response = index.query(
            namespace="sjsu",
            vector=[0.1] * 1536,  # Dummy vector to get all records
            top_k=10,  # Increase if you have more professors
            include_metadata=True
        )
        
        print("\nVerifying all professors in database:")
        for i, match in enumerate(response.matches, 1):
            print(f"\n{i}. {match.metadata['name']}")
            print(f"   Department: {match.metadata['department']}")
            print(f"   Email: {match.metadata['email']}")
    except Exception as e:
        print(f"Verification failed: {e}")

if __name__ == "__main__":
    test_pinecone()
    print("\nVerifying data for chatbot...")
    time.sleep(5)  # Wait a bit for data to be fully indexed
    verify_data_for_chatbot()
    verify_all_professors() 