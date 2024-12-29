from ..llm import llm
from .rag import tools
from langchain_core.runnables import Runnable
from langgraph.graph import MessagesState


llm_with_tools: Runnable = llm.bind_tools(tools)
sys_msg = " You are the help full banking rag assistant please help the user with their queries and search the rag for the best answer"

def assistant(state: MessagesState): 
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"][-10:])]}


