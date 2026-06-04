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

def main():
    
    # Step1: Load structured financial knowledge
    documents = load_investor_principles()
    print(f"\n Loaded {len(documents)} documents")

    # Step2: Create vector database
    vector_store = create_vector_store(documents)
    print("\nVector store created successfully")

    # Step3: Build Graph
    graph = build_financial_graph()
    print("\nFinancial workflow graph compiled")

    # Step4: Create Initial Workflow State
    # This is the same state object that we created in notebook now its getting productonized
    initial_state = {
   #"query"     : "How should I build a long term portfolio for multibaggers?",
   # "query"     : "What are the best Vanguard ETFs?",
    "query"     : "Give me some suggestions for the stock picking",
    "documents" : [],
    "answer"    : "",
    "vector_store": vector_store,
    "route":""
                    }
    
    # Step5 - Execute LangGraph workflow
    result = graph.invoke(initial_state)

    # Step6 - Print Final Answer
    print("\n----- FINAL ANSWER -----\n")
    print(result["answer"])


if __name__ == "__main__":
    main()



