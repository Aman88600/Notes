# v1_basic_qa_groq.py

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from groq_llm import GroqLLM  # same as before

# Step 1: Define the prompt using ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers questions clearly and concisely."),
    ("human", "{question}")
])

# Step 2: Use your GroqLLM (chat-compatible)
llm = GroqLLM(temperature=0.7)

# Step 3: Output parser to clean up result
output_parser = StrOutputParser()

# Step 4: Compose everything using LCEL (pipe syntax)
chain = prompt | llm | output_parser

# Step 5: Ask a question
question = input("Ask any question: ")

# Step 6: Run the chain
response = chain.invoke({"question": question})

# Step 7: Show result
print("\n🔍 Question:", question)
print("📄 Answer:", response)
