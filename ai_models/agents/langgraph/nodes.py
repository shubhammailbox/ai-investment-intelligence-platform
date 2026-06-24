"""
nodes.py

Purpose:
--------
This module contains the executable workflow nodes used in the
LangGraph-based financial AI workflow.

Each node represents a single unit of work inside the AI execution graph.
Nodes receive the current workflow state, perform a task, and return
updated state values.

Current Nodes:
--------------
1. retrieve_documents_node
   - Retrieves relevant financial documents from vector database
   - Uses semantic similarity search
   - Updates workflow state with retrieved documents

2. generate_answer_node
   - Uses retrieved context to generate grounded financial responses
   - Calls the LLM using prompt-based reasoning
   - Updates workflow state with final generated answer

03.06.2026   
3. router_node
   - Determine which workflow path should execute based on user query.

4. etf_node
    - ETF path if its in the query 
   
Architecture Role:
------------------
This module forms the execution layer of the LangGraph workflow engine.
Each node acts as an independent AI workflow step.

Author:
-------
Shubham Mishra

"""

from langchain_openai import ChatOpenAI
from ai_models.rag.retriever.retrieval import retrieve_documents
from ai_models.tools.etf_tools import get_etf_data

def retrieve_documents_node(state):
    """
    Retrieve relevant documents from vector database.
    """

    print("\n--- RETRIEVE NODE RUNNING ---\n")

    # Read values from workflow state
    query = state["query"]
    vector_store = state["vector_store"]

    # Retrieve relevant documents
    documents = retrieve_documents(
        query=query,
        vector_store=vector_store,
        k=3
    )

    # Return updated workflow state
    return {
        "documents": documents
    }


def generate_answer_node(state):

    """
    Generate grounded financial answer using retrieved documents.
    """

    print("\n--- GENERATE ANSWER NODE RUNNING ---\n")

    # Read values from workflow state
    query = state["query"]
    documents = state["documents"]

    # Build context from retrieved documents
    context = "\n".join(
        [doc.page_content for doc in documents]
    )

    # Prompt template
    prompt = f"""
    You are a financial advisor AI.

    STRICT RULES (MUST FOLLOW):
    1. Answer ONLY using the information provided in the context.
    2. Do NOT use any external knowledge.
    3. Do NOT add explanations beyond the context.
    4. If the answer is not fully available in the context, say:
    "I don't have enough data to answer this."
    5. Do NOT infer, assume, or generalize.
    6. Answer ONLY what is asked
    7. Do not include unrelated principles.

    OUTPUT FORMAT:
    - Use bullet points
    - Keep answers concise
    - Use exact phrases from context wherever possible

    Context:
    {context}

    Question:
    {query}
    """

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini"
    )

    # Generate response
    response = llm.invoke(prompt)

    # Return updated workflow state
    return {
        "answer": response.content
    }

def router_node(state):
    """
    Determine which workflow path should execute
    based on the user query.
    """

    print("\n--- ROUTER NODE RUNNING ---\n")

    query = state["query"].lower()

    if "etf" in query:
        route = "etf"
    else:
        route = "rag"

    print(f"Route selected: {route}")

    return {
        "route": route
    }

def etf_node(state):

    """
    ETF Agent node.
    
    Purpose:
    -----------
    Handles ETF related user queries.

    Responsibilities:
    ----------------
    - Read query from state
    - Extract ETF ticker
    - Call ETF Tool
    - Generate user friendly answer
    - Update workflow state

    Returns:
    -----------
    Updated State Dictionary
    """

    print("\n--- ETF NODE RUNNING ---\n")

    # Read User Query
    query = state["query"]
    print(f"User Query: {query}")

    # ETF node should decide the ETF
    if   "voo" in query.lower():
        ticker = "VOO"
    elif "vti" in query.lower():
        ticker = "VTI"
    elif "vwra" in query.lower():
        ticker = "VWRA"
    elif "qqqm" in query.lower():
        ticker = "QQQM"
    elif "soxx" in query.lower():
        ticker = "SOXX"
    else: 
        ticker = "VOO"
    
    # call the ETF tool now from /tools
    print(f"Ticker Selected: {ticker}")

    etf_data = get_etf_data.invoke(
        {
        "ticker": ticker
        }
    )
    
    # create the answer and call it
    answer = f"""
    
    ETF Information:

    Ticker: {etf_data["ticker"]}
    Name: {etf_data["name"]}
    Expense Ratio: {etf_data["expense_ratio"]}
    Category:{etf_data["category"]}

    """

    return {
                "answer": answer
    }

    
def route_query(state):
    
    """
    Return routing decision 
    for LangGraph conditional edges
    """

    return state["route"]