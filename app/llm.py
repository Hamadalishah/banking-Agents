from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()
api_key: Optional[str] = os.getenv("GOOGLE_API_KEY")

llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=api_key #type: ignore
)

        