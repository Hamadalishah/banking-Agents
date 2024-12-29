from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph,START,END
from langgraph.graph.state import CompiledStateGraph
from .memory import call_model,summarize_conversation,should_continue
from .memory import State


# Define a new graph
workflow: StateGraph = StateGraph(State)

# Add nodes
workflow.add_node("conversation",call_model )
workflow.add_node(summarize_conversation)

# Add edges
workflow.add_edge(START, "conversation")
workflow.add_conditional_edges("conversation", should_continue)
workflow.add_edge("summarize_conversation", END)

#add memory saver
memory: MemorySaver = MemorySaver()
# Compile
graph: CompiledStateGraph = workflow.compile(memory)

