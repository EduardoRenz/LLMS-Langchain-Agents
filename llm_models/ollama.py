from langchain_ollama import OllamaLLM
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def create_model():
    return OllamaLLM(model="llama3.2:3b")
