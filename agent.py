import os
from dotenv import load_dotenv
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from rag import RAG
from tools.rmp_client import RMPClient as RateMyProfClient

class ProfessorRaterAgent:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Pinecone Setup
        self.PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        if self.PINECONE_API_KEY is None:
            raise ValueError("Please set the PINECONE_API_KEY environment variable")

        # Initialize Pinecone client and embeddings
        self.pc_client = Pinecone(api_key=self.PINECONE_API_KEY)
        self.embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
        self.index_name = "professors-index"

        # Initialize RAG with Pinecone client, index, and embeddings
        self.rag = RAG(self.pc_client, self.index_name, self.embeddings)

        # Initialize retriever
        self.retriever = self.rag.get_retriever()

        # Initialize LLM (Language Model)
        self.llm = ChatOpenAI(model="gpt-4o-mini")

        # System prompt for contextualizing questions
        self.contextualize_q_system_prompt = (
            "Given a chat history and the latest user question "
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question, just "
            "reformulate it if needed and otherwise return it as is."
        )

        # Create a prompt template for contextualizing questions
        self.contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        # Create history aware retriever
        self.history_aware_retriever = create_history_aware_retriever(
            self.llm, self.retriever, self.contextualize_q_prompt
        )

        # Update the qa_system_prompt to handle both internal and RMP data
        self.qa_system_prompt = """
You are a Professor Information Assistant that provides information about SJSU professors from both the internal database and Rate My Professor data.

When you find information about a professor, format your response like this:
- Name: [Professor Name]
- Department: [Department]
- Position: [Position]
- Email: [Email if available]
- Office: [Office Location if available]
- Description: [Professor Description]

If Rate My Professor data is available, also include:
- Overall Rating: [Rating]/5.0
- Number of Ratings: [Number]
- Would Take Again: [Percentage]%
- Difficulty: [Rating]/5.0

Combine information from both sources when available to provide the most comprehensive response.
If you can't find the professor in either database, respond with "NO PROFESSOR".

{context}
"""

        # Create a prompt template for the QA system
        self.qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.qa_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        # Create a chain for question answering
        self.question_answer_chain = create_stuff_documents_chain(
            self.llm, 
            self.qa_prompt,
            document_variable_name="context"
        )

        # Create a retrieval chain using the history-aware retriever and QA chain
        self.rag_chain = create_retrieval_chain(
            self.history_aware_retriever, 
            self.question_answer_chain
        )

        self.client = RateMyProfClient()

    def format_professor_info(self, professor_data):
        # Format the professor information including research interests
        if "research" in professor_data:
            research_info = f"\n🔬 Research Interests:\n{professor_data['research']}"
        else:
            research_info = ""
            
        return f"""Name: {professor_data['first_name']} {professor_data['last_name']}
🏛️ Department: {professor_data['department']}
📊 Overall Rating: {professor_data['overall_rating']}/5.0
📈 Number of Ratings: {professor_data['num_ratings']}
👍 Would Take Again: {professor_data['would_take_again']}%
📚 Difficulty: {professor_data['difficulty']}/5.0{research_info}"""

    def invoke(self, input: str, chat_history: list):
        """Invoke the retrieval chain with the provided input and chat history."""
        try:
            print(f"\nDebug - Query: {input}")
            
            # Process the user's query through the retrieval chain
            result = self.rag_chain.invoke({
                "input": input, 
                "chat_history": chat_history
            })
            
            print(f"Debug - Raw Result: {result}")
            
            if not result.get('answer'):
                print("Debug - No answer found, returning NO PROFESSOR")
                return "NO PROFESSOR"
            
            # Check if the response includes RMP data by looking at the answer content
            if 'overall rating' in result['answer'].lower() or 'would take again' in result['answer'].lower():
                return result['answer']
            else:
                return "NO PROFESSOR"  # This will trigger RMP lookup in main.py
            
        except Exception as e:
            print(f"Debug - Error in invoke: {str(e)}")
            return f"An error occurred: {str(e)}"

    def stream(self, input: str, chat_history: list):
        """Stream the retrieval chain with the provided input and chat history.

        Args:
            input (str): The user input or query.
            chat_history (list): A list of messages representing the chat history.

        Yields:
            str: The AI's response text.
        """
        # Process the user's query through the retrieval chain
        for chunk in self.rag_chain.stream({"input": input, "chat_history": chat_history}):
            if answer_chunk := chunk.get("answer"):
                yield answer_chunk


# Example usage to start the continual chat
def start_chat(bot: ProfessorRaterAgent):
    """Start a continual chat session with the AI."""
    print("Start chatting with the AI! Type 'exit' to end the conversation.")
    chat_history = []  # Collect chat history here (a sequence of messages)
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        # Invoke the bot with the user's query and chat history
        answer = bot.invoke(query, chat_history)
        # Display the AI's response
        print(f"AI: {answer}")
        # Update the chat history
        chat_history.append(HumanMessage(content=query))
        chat_history.append(SystemMessage(content=answer))


# Main function to start the continual chat
if __name__ == "__main__":
    bot = ProfessorRaterAgent()
    start_chat(bot)