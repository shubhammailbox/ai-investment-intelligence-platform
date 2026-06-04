"""
financial_graph.py

Purpose:
--------
This module defines and builds the LnagGraph workflow orchestration
fro the AI-powered financial intelligence system.

The workflow raph coordinates the execution order of AI nodes,
allowing the system to perform multi-step reasoning and execution.


Current Workflow:
-----------------
START
  ↓
Router
  ↓
 ┌──────────────┬──────────────┐
 ↓              ↓
ETF         Retrieve Documents
 ↓              ↓
END         Generate Answer
              ↓
             END

Why This File Exists:
---------------------

The purpose of this module is to separate workflow orchestration logic 
from individual node implementations.

This enables:
- scalable workflow design
- graph based execution
- reusable node composition
- future conditional routing
- future agentic AI capabailities

Architecture Role:
--------------------
This module acts as the orchestraion engine for the the financial AI system.
It defines how workflow nodes are connected and executed.

Future Enhancements:
--------------------
- tool execution
- evaluation nodes
- portfolio analysis workfloes
- ETF recommendation workflows
- multi agents systems

Author:
-------
Shubham Mishra
"""


from langgraph.graph import StateGraph, END

from ai_models.agents.langgraph.state import FinancialAgentState

from ai_models.agents.langgraph.nodes import (
  retrieve_documents_node,
  generate_answer_node,
  router_node,
  etf_node,
  route_query
)


def build_financial_graph():
    """
    Build and compile the LangGraph financial workflow

    Returns:
        CompiledStateGraph:
            Executable LangGraph workflow.
    """
    
    # create workflow object
    workflow = StateGraph(FinancialAgentState)

    # Add workflow nodes

    workflow.add_node(
        "router",
        router_node
    )

    workflow.add_node(
        "etf",
        etf_node
    )

    workflow.add_node(
    "retrieve_documents", 
     retrieve_documents_node
     )
    
    #
    workflow.add_node(
        "generate_answer", 
        generate_answer_node
        )    

    # add starting point
    workflow.set_entry_point(
        "router"
        )   

    # Adding conditional edge
    workflow.add_conditional_edges(
        "router",
        route_query,
      {
          "etf": "etf",
          "rag": "retrieve_documents"
      }
    )

     # add edge between etf and end
    workflow.add_edge(
      "etf",
      END 
                    )
    # add edge between retrieve and answer same like graph
    workflow.add_edge(
        "retrieve_documents",
        "generate_answer")
    
    # generation --> end edge
    workflow.add_edge(
    "generate_answer", 
    END
                    )
    
    # Compile executable graph
    return workflow.compile()

