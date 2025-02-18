from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

def check_professors():
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    index = pc.Index("professors-index")
    stats = index.describe_index_stats()
    print(f"Total professors in index: {stats.total_vector_count}")
    print(f"Namespaces: {stats.namespaces}")

if __name__ == "__main__":
    check_professors() 