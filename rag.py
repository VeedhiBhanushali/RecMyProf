from langchain_pinecone import PineconeVectorStore
from logging import getLogger

logger = getLogger(__name__)

class RAG:
    def __init__(self, pinecone_client, pinecone_index_name, embedding):
        self.pinecone_client = pinecone_client
        self.pinecone_index_name = pinecone_index_name
        self.vector_store = None
        self.embedding = embedding
        self._initialize()

    def _initialize(self):
        if self.pinecone_index_name not in self.pinecone_client.list_indexes().names():
            raise ValueError(f"Index {self.pinecone_index_name} not found in Pinecone. Please create the index first.")

        index = self.pinecone_client.Index(self.pinecone_index_name)
        self.vector_store = PineconeVectorStore(
            index, 
            self.embedding,
            namespace="sjsu",
            text_key="description"
        )
        logger.info(f"Vector Store initialized with index {self.pinecone_index_name}")
        
    def lookup(self, query: str, top_k=3):
        print(f"\nDebug RAG - Looking up query: {query}")
        self._initialize()
        results = self.vector_store.similarity_search(
            query, 
            top_k=top_k,
            namespace="sjsu"
        )
        print(f"Debug RAG - Found results: {results}")
        return results
    
    def get_retriever(self):
        print("Debug RAG - Getting retriever")
        self._initialize()
        return self.vector_store.as_retriever(
            search_kwargs={"k": 3, "namespace": "sjsu"}
        )

def get_professor_info(professor_name):
    try:
        # Get professor data from Pinecone
        results = index.query(
            vector=get_embedding(professor_name),
            top_k=1,
            namespace="sjsu",
            include_metadata=True
        )
        
        if results.matches:
            metadata = results.matches[0].metadata
            # Make sure we're including research and contact info
            if "contact_info" in metadata:
                metadata["research"] = metadata["contact_info"].get("research", "")
            return metadata
        return None
    except Exception as e:
        print(f"Error getting professor info: {e}")
        return None