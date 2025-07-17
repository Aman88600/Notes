from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192",
)

# Prompt for summarization
summarize_prompt = PromptTemplate.from_template(
    "Please summarize the following content in a concise and clear way:\n\n{content}"
)

summarizer_chain = summarize_prompt | llm

def summarizer_function(content: str) -> str:
    """Summarizes the given content."""
    try:
        result = summarizer_chain.invoke({"content": content})
        return result.content.strip()
    except Exception as e:
        return f"❌ Error during summarization: {e}"
