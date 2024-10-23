from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

available_models = ['openai', 'gemini', 'ollama']


def create_model(model_name: str = os.getenv("LLM_MODEL")):
    if model_name not in available_models:
        raise ValueError(
            f"Model {model_name} not available. Available models: {available_models}"
        )

    if model_name == 'openai':
        return ChatOpenAI(
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )

    if model_name == 'gemini':
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            api_key=os.getenv("GEMINI_API_KEY"),
        )

    if model_name == 'ollama':
        return OllamaLLM(model="llama3.2:3b")
