from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Getting the api key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192"
)

def translator_worker_function(text, target_language):
    prompt = PromptTemplate.from_template(
        "Translate the following into {language}:\n\n{text}"
    )
    chain = prompt | llm
    # with open("web_scraper_output.txt") as file:
    #     text_from_file = file.read()
    return chain.invoke({"text": text, "language": target_language}).content
