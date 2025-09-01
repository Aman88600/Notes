# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# import os
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("groq_api")

# llm = ChatGroq(
#     groq_api_key=api_key,
#     model_name="llama3-8b-8192",
# )

# # Prompt for summarization
# summarize_prompt = PromptTemplate.from_template(
#     "Please arrang the following content in a concise and clear way:\n\n{content}"
# )

# summarizer_chain = summarize_prompt | llm

# def summarizer_function(content: str) -> str:
#     """Summarizes the given content."""
#     try:
#         result = summarizer_chain.invoke({"content": content})
#         return result.content.strip()
#     except Exception as e:
#         return f"❌ Error during summarization: {e}"
    
# if __name__ == "__main__":
#     file = open("page_source.txt") 
#     text = file.read()
#     print(text)
#     file.close()
#     output = summarizer_function(text)
#     print(output)

import requests
import csv

def get_ai_response(raw_text):
    response = requests.post(
        'https://api.perplexity.ai/chat/completions',
        headers={
            'Authorization': 'Bearer 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',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'sonar-pro',
            'messages': [
                {
                    'role': 'user',
                    'content': f"Arrange the follwing content in a structured way in json format with following fields Basic Info Activity Exoerience Education Certification and Skills {raw_text}"
                }
            ]
        }
    )
    text = response.json()
    return text['choices'][0]['message']['content']

with open('Partial_ids/google.csv', mode='r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Loop through the rows in the CSV
    scrape_lock = True
    for row in csv_reader:
        if "http" in row[0]:
            name = row[0].split("/")[-1]
            print(name)
            sec_file=open(f"full_ids/{name}.txt", "r", encoding='utf-8')
            text = sec_file.read()
            sec_file.close()
            print(f"write{name}")
            output = get_ai_response(text)
            tri_file=open(f"full_ids_ai/{name}.txt", "w", encoding='utf-8')
            tri_file.write(output)
            tri_file.close()