from fastapi import FastAPI,HTTPException,APIRouter
from langchain_core.messages import HumanMessage
from .graph import graph


router = APIRouter()


@router.get("/summarize")
async def summarize():
    return {"message": "Hello, World!"}



@router.post("/summarize/{query}")
async def summarize(query: str):
    thread_id = "1"
    config = {"thread_id": thread_id}
    try:
        message = graph.invoke({"messages": [HumanMessage(content=query)]},config)
        return message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



