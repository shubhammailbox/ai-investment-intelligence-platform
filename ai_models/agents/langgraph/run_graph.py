"""
run_graph.py

ROLE:
-----
This is the runtime entry point for the Dhyanful V1 LangGraph application.

WHAT THIS FILE DOES:
--------------------
1. Takes the user's query as input.
2. Calls run_research() from graph_service.py.
3. run_research() prepares and executes the LangGraph workflow.
4. Receives the final answer returned by the workflow.
5. Prints the answer to the user.

IMPORTANT:
----------
This file does NOT define the LangGraph workflow.

It simply starts the execution.

Execution flow:

User Query
    ↓
run_graph.py
    ↓
run_research(query)
    ↓
graph_service.py
    ↓
initialize_graph()
    ├── Load investment knowledge
    ├── Create FAISS vector store
    └── Build/compile LangGraph
    ↓
graph.invoke(initial_state)
    ↓
LangGraph executes nodes
    ↓
Final State
    ↓
result["answer"]
    ↓
run_graph.py prints the answer


MENTAL MODEL:
-------------
run_graph.py = "Start the application and give it a question."

graph_service.py = "Prepare and execute the AI workflow."

financial_graph.py = "Define the workflow and node connections."

nodes.py = "Define what each node actually does."

state.py = "Define the shared data that flows between nodes."


"""

import os

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found. Please check your .env file."
    )

from ai_models.agents.langgraph.graph_service import run_research

def main():

    #"query"    : "How should I build a long term portfolio for multibaggers?"
    #"query"    : "What are the best Vanguard ETFs?",
    #"query"    : "Give me some suggestions for the stock picking",
    #"query"    : "US & Korea stocks are at all time high, just wondering what should i do now? should i buy or wait?",
    #"query"    : "What should be the asset allocation for next 10 years?",
    #"query"    : "Tell me about NVDA stock and if its worth buying now",
    
    # 1. Takes the user question
    query = input("Enter your question: ")


    # 2. Send the question to graph_service.py
    # 3. graph_service.py executes the LangGraph workflow
    # 4. Receive the final answer
    answer = run_research(query)

    print(answer)

if __name__ == "__main__":
    main()



