# Getting the API KEY from the .env file
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
# print(api_key)

# Main code
from langchain.llms.base import LLM
from groq import Groq
from pydantic import BaseModel, Field

class GroqLLM(LLM, BaseModel):  # Inherit from BaseModel to work with Pydantic
    api_key: str  # Declare api_key as a Pydantic field
    
    def __init__(self, **kwargs):
        # Use Pydantic's initialization method to handle the api_key
        super().__init__(**kwargs)

    def _call(self, prompt: str) -> str:
        # Instantiate the Groq client inside the _call method to avoid Pydantic issues
        client = Groq(api_key=self.api_key)
        
        try:
            # Call Groq API and get the response
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role": "user", "content": prompt}],
                temperature=1,
                max_completion_tokens=1024,
                top_p=1,
                stream=False  # Not streaming, just want the final response
            )
            
            # Print the response to understand the structure better
            print("Full Response:", completion)
            
            # Ensure the response contains choices and we access the correct content
            if completion.choices and 'message' in completion.choices[0]:
                # Correctly accessing the message content
                return completion.choices[0].message.get('content', "No content available.")
            else:
                return "No valid response from Groq API."
        
        except Exception as e:
            # Catch any errors that occur during the API call
            return f"Error occurred: {str(e)}"

    @property
    def _llm_type(self):
        return "Groq"

    @property
    def _identifying_params(self):
        return {"api_key": self.api_key}
    
# Make sure to define your API key before running the code
api_key = api_key  # Replace with your actual API key

groq_llm = GroqLLM(api_key=api_key)

# Test with a simple prompt
completion = groq_llm._call("what is the speed of light?")
print(completion)
