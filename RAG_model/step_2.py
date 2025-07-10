# Main code
from langchain.llms.base import LLM
from groq import Groq
from pydantic import BaseModel, Field

class GroqLLM(LLM, BaseModel):
    api_key: str
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _call(self, prompt: str) -> str:
        client = Groq(api_key=self.api_key)
        
        try:
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role": "user", "content": prompt}],
                temperature=1,
                max_completion_tokens=1024,
                top_p=1,
                stream=False
            )            
            print("Full Response:")
            print(type(completion))
            main_text = completion.choices[0].message.content
            return main_text
        
        except Exception as e:
            return f"Error occurred: {str(e)}"
    @property
    def _llm_type(self):
        return "Groq"
    @property
    def _identifying_params(self):
        return {"api_key": self.api_key}
    

