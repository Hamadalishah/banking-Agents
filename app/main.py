from fastapi import FastAPI
from .rout import router
import uvicorn
app = FastAPI()

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


def start():
    # create_tables()
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1", 
        port=8000,
        reload=True
    )

"""
To run this project:

1. Make sure you have Poetry installed:
   curl -sSL https://install.python-poetry.org | python3 -

2. Initialize project with Poetry:
   poetry init
   
3. Add dependencies:
   poetry add fastapi uvicorn langchain langgraph langchain-google-genai python-dotenv

4. Run the project:
   poetry run python -m summarizer_agent.main

Or directly with uvicorn:
   poetry run uvicorn summarizer_agent.main:app --reload

The API will be available at:
- http://localhost:8000/summarize (GET)
- http://localhost:8000/summarize/{query} (POST)
"""


