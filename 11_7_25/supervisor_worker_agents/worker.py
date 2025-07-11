# worker.py
from groq_llm import GroqLLM
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
llm = GroqLLM(api_key=api_key)

def worker_task(instruction: str) -> str:
    prompt = f"You are a helpful assistant. Complete the following task:\n\n{instruction}\n\nAnswer:"
    return llm._call(prompt)
