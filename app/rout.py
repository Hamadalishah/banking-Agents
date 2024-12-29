from fastapi import HTTPException,APIRouter
from langchain_core.messages import HumanMessage
from .graph import graph


router = APIRouter()


@router.get("/summarize")
async def route_summarize():
    return {"message": "Hello, World!"}



@router.post("/summarize/{query}")
async def summarize(query: str):
    thread_id = "1"
    config = {"thread_id": thread_id}
    try:
        message = graph.invoke({"messages": [HumanMessage(content=query)]},config) #type: ignore
        return message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





