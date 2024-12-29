from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from dotenv import load_dotenv
import os

load_dotenv()
loader = TextLoader("app/rag/rag.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",  # Required model name
)

db = FAISS.from_documents(texts, embeddings) 
retriever = db.as_retriever()

# Create your  reteriever tool
retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="Banking_information_sender",
    description="Searches information about bank from provided vector and return accurare as you can",
    
)

# Export as a list
tools = [retriever_tool]  # Make sure this is a list

