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

3. router_node
   - Determine which workflow path should execute based on user query.

4. market_data_node
   - 

5. investment_research_node
   -
   
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
from ai_models.tools.market_data_tools import get_market_data

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
    Determine which workflow path should execute based on the user query.
    """

    print("\n--- ROUTER NODE RUNNING ---\n")

    query = state["query"].lower()

    market_keywords = [
    "etf",
    "share",
    "shares"]
    
    if any(keyword in query for keyword in market_keywords):
        route = "market_research"
    else:
        route = "rag"

    print(f"Route selected: {route}")

    return {
        "route": route
    }

def market_data_node(state):

    """
    Use LLM tool calling to determine and retrieve market data 
    for the financial instrument in the user query.
    """

    print("\n--- Market Data Node Running ---\n")

    # Read User Query
    query = state["query"]
    print(f"User Query: {query}")

    # Initialize LLM
    llm = ChatOpenAI(
        model = "gpt-4o-mini"
    )

    # Give the LLM access to market-data-tool
    llm_with_tools = llm.bind_tools(
        [get_market_data]
    )

    #Ask the LLM to determine whether/how to use the tool
    response = llm_with_tools.invoke(query)

    print("\n ----LLM Response---")
    print (response)

    print("\n---Tool calls---")
    print(response.tool_calls)

    return {
                "answer": "Tool calling test completed"
    }

def investment_research_node(state):
    """
    
    AI Investment Research Agent.

    Purpose:
    --------
    Performs investment research by combining multiple
    sources of information before generating a recommendation.

    Workflow:
    --------
    1. Retrieve live market data
    2. Retreive investments principles (RAG)
    3. Combine both
    4. Ask LLM to reason
    5. Return Investment Recommendation

    Example:
    --------
    Suppose if user asks  - Should I invest 1000$ in NVDA share, what would your agent do?
    It would check what NVDA is and get its current market information, then it recalls 
    Buffet's investment principles on good valuation, think about user question and then 
    do some recommendation. This node is doing all the thinking.
    
    """
    print("\n *** Investment Research Node Running ***")

    # Step1: Retrieve the live market data

    # Step2: Retrieve investment knowledge from RAG

    # Step3: Combine both sources

    # Step4: Ask the LLM to reason over the combined context

    # Step5: Retrun the investment recommendation

    
def route_query(state):
    
    """
    Return routing decision for LangGraph conditional edges
    """

    return state["route"]