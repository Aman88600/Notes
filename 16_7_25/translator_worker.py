from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

def translator_function(text, target_language="French"):
    prompt = PromptTemplate.from_template(
        "Translate the following into {language}:\n\n{text}"
    )
    chain = prompt | llm
    return chain.invoke({"text": text, "language": target_language}).content
