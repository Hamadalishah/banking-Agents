from fastapi import APIRouter,HTTPException
from .graph import agent

router2 = APIRouter()

@router2.get("/rag/{query}")
async def get_rag(query: str):
    config = {"configurable": {"thread_id": "4"}}
    try:
        result = agent.invoke({"messages": [("user", query)]}, config) #type: ignore
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
