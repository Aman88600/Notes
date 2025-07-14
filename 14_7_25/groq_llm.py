# groq_llm.py
from langchain.llms.base import LLM
from groq import Groq
from pydantic import BaseModel, Field
from typing import Optional, List
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class GroqLLM(LLM, BaseModel):
    api_key: str = Field(default_factory=lambda: os.getenv("GROQ_API_KEY"))

    model: str = "meta-llama/llama-4-scout-17b-16e-instruct"
    temperature: float = 1.0
    max_tokens: int = 1024
    top_p: float = 1.0

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        client = Groq(api_key=self.api_key)

        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error occurred: {str(e)}"

    @property
    def _llm_type(self) -> str:
        return "groq"

    @property
    def _identifying_params(self):
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "top_p": self.top_p
        }
