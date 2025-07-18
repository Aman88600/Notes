# define_worker.py

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192"
)

def define_function(text: str) -> str:
    """Use LLM to explain or define the input text."""
    prompt = f"Explain this in simple terms: {text}"
    return llm.invoke(prompt).content
