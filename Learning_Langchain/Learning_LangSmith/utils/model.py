from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(model_name="llama3-8b-8192", temperature=0.3)
