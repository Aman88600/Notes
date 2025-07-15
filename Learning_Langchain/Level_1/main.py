from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Loading the .env file
load_dotenv()

# Getting the API key
api_key = os.getenv("GROQ_API_KEY")

# making an object(llm) using the ChatGroq class
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192",  # or 70b if you want
)

# Making the prompt using the from_template() method
template = "Translate this into French:\n\n{text}"
prompt = PromptTemplate.from_template(template)

# making the chain using the LLMChain class
chain = LLMChain(llm=llm, prompt=prompt)

# using the invoke() method to get the response
response = chain.invoke({"text":"Good Morning!"})

# Prithind the response
print(response['text'])
