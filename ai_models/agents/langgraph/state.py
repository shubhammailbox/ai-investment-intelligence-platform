"""
state.py

Purpose:
--------
This module defines the shared workflow state used across
the LangGraph-based financial AI workflow.

The state acts as shared memory flowing between workflow nodes.
Each node reads values from the state, updates the state,
and passes it forward to the next node.

Analogy:
--------
Think of state like a baton in a relay race.
Each workflow node receives the baton,
updates it, and passes it to the next node.

Current Workflow State Includes:
--------------------------------
- query:
    User's financial query

- documents:
    Retrieved documents from vector database

- answer:
    Final AI-generated response

- vector_store:
    FAISS vector database used for retrieval
"""

from typing import TypedDict, List, Any
from langchain_core.documents import Document


class FinancialAgentState(TypedDict):

    query: str
    documents: List[Document]
    answer: str
    vector_store: Any

    # stored routing decision
    route: str
    market_data: str