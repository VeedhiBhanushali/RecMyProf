from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client using API key from environment variable
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def generate_haiku():
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Changed from "gpt-4" to "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": "Write a haiku about AI"}
            ]
        )
        # Print the generated haiku
        print(completion.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_haiku() 