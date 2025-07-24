# Getting the api key
from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("GROQ_API_KEY")

# making the groq LLM
from langchain_groq import ChatGroq

llm = ChatGroq(groq_api_key = api_key,
         model_name="llama3-8b-8192")

response = llm.invoke("What is the speed of light?")
print(response)