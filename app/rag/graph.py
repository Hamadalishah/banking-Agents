from langgraph.graph import StateGraph, START, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from .rag import tools
from langgraph.checkpoint.memory import MemorySaver
from .llm import assistant

builder = StateGraph(MessagesState) 
builder.add_node("assistant", assistant) 
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "assistant") 
builder.add_conditional_edges("assistant", tools_condition) 
builder.add_edge("tools", "assistant")

memory: MemorySaver = MemorySaver()
agent = builder.compile(checkpointer=memory)



