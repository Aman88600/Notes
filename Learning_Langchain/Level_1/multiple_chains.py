from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

# Loading the .env file
load_dotenv()

# Getting the API key
api_key = os.getenv("GROQ_API_KEY")

# making an object(llm) using the ChatGroq class
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192",  # or 70b if you want
)


# 1 Summary Chain

summary_template = "Summariz the follwing:\n\n{text}"
summary_prompt = PromptTemplate.from_template(summary_template)
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)

# 2 Translation chain
# Making the prompt using the from_template() method
translate_template = "Translate this into French:\n\n{text}"
translate_prompt = PromptTemplate.from_template(translate_template)

# making the chain using the LLMChain class
translate_chain = LLMChain(llm=llm, prompt=translate_prompt)



# Combining the two chains
overall_chain = SimpleSequentialChain(chains=[summary_chain, translate_chain], verbose=True)

# using the invoke() method to get the response
response = overall_chain.invoke("LangChain lets you build LLM apps by linking prompts, memory, tools, and models together.")

# Prithind the response
print(response)
