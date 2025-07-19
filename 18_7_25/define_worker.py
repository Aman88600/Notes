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

def define_function() -> str:
    """Use LLM to explain or define the input text."""
    with open("web_scraper_output.txt") as file:
        text_from_file = file.read()
    prompt = f"Explain this in simple terms: {text_from_file}"
    return llm.invoke(prompt).content
