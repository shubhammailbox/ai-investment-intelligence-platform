"""
run_graph.py

Purpose:
--------
This module serve as the runtime execution entrypoint for the 
LangGraph based financial AI workflow system.

The script perform the following:
- loads structured financial knowledge data
- creates the vector database
- initializes workflow state
- builds the LangGraph workflow
- executes the AI workflow graph
- prints the final generated response

Architecture Role:
------------------
This module acts as the runtime launcher for the financial AI agent system.

It connects:
- data ingestion
- vector retrieval
- workflow orchestration
- AI generation

Future Enhancements:
--------------------
Future versions may include:
- API integration
- FastAPI serving
- streaming responses
- Bedrock integration
- multi-agent orchestration
- production deployment

Author:
-------
Shubham Mishra
"""

from dotenv import load_dotenv

load_dotenv()
import os

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found. Please check your .env file."
    )

from ai_models.rag.ingestion.load_data import load_investor_principles
from ai_models.rag.embeddings import create_vector_store
from ai_models.agents.langgraph.financial_graph import build_financial_graph
from ai_models.agents.langgraph.graph_service import run_research

def main():

    #"query"     : "How should I build a long term portfolio for multibaggers?",
    #"query"    : "What are the best Vanguard ETFs?",
    #"query"    : "Give me some suggestions for the stock picking",
    #"query"    : "US & Korea stocks are at all time high, just wondering what should i do now? should i buy or wait?",
    #"query"    : "What should be the asset allocation for next 10 years?",
    #"query"    : "Tell me about NVDA stock and if its worth buying now",
    
    query = input("Enter your question: ")

    answer = run_research(query)

    print(answer)

if __name__ == "__main__":
    main()



