import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


def create_model():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        api_key=api_key,
    )
