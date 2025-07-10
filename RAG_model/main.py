# Getting the API KEY from the .env file
import os
from dotenv import load_dotenv
from step_2 import GroqLLM

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
api_key = api_key 
groq_llm = GroqLLM(api_key=api_key)

# Prompt function
completion = groq_llm._call("what is the speed of light?")

# Code
# main.py
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Step 1: Load & Split Text File
def load_documents(file_path="black_hole.txt"):
    loader = TextLoader(file_path)
    raw_docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(raw_docs)

# Step 2: Embed & Save to Chroma
def embed_and_save(docs, db_path="db"):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embedding_model, persist_directory=db_path)
    vectorstore.persist()

# Step 3: Load vector DB
def load_vectorstore(db_path="db"):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=db_path, embedding_function=embedding_model)

# Step 4: RAG-style QA
def ask_with_rag(question: str, vectorstore, llm, k=3):
    # Step 1: Retrieve top-k chunks
    docs = vectorstore.similarity_search(question, k=k)
    
    # Step 2: Build context
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # Step 3: Inject context into the prompt
    prompt = f"""Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:"""

    # Step 4: Get response from LLM
    answer = llm._call(prompt)

    # Step 5: Print sources
    print("\n📄 Sources used:")
    for i, doc in enumerate(docs, start=1):
        snippet = doc.page_content.strip().replace('\n', ' ')
        print(f"Chunk {i}: {snippet[:120]}{'...' if len(snippet) > 120 else ''}")

    return answer


# === MAIN ===
if __name__ == "__main__":
    # STEP A: Setup LLM and vectorstore
    file_path = "black_hole.txt"  # Change to your .txt file
    db_path = "db"

    if not os.path.exists(db_path):
        print("🔄 Creating vector DB...")
        docs = load_documents(file_path)
        embed_and_save(docs, db_path)

    # Load DB and LLM
    vectorstore = load_vectorstore(db_path)
    groq_llm = GroqLLM(api_key=api_key)

    # Interactive loop
    print("\n✅ RAG System Ready. Ask anything from your file.")
    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() == "exit":
            break
        answer = ask_with_rag(question, vectorstore, groq_llm)
        print("\n📌 Answer:", answer)
