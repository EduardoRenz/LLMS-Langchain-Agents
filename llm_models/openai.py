from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def create_model():
    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key
    )
