from dotenv import load_dotenv
import os
from groq_llm import GroqLLM

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
groq_llm = GroqLLM(api_key=api_key)
completion = groq_llm._call("what is the speed of light?")
print(completion)