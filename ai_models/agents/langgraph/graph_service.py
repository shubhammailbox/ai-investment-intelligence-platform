
from ai_models.rag.ingestion.load_data import load_investor_principles
from ai_models.rag.embeddings import create_vector_store
from ai_models.agents.langgraph.financial_graph import build_financial_graph

def initialize_graph():

    """
    Build the AI application.

    This function loads the knowledge base,
    creates the vector database,
    and compiles the LangGraph workflow.
    
    """
    # Step1: Load structured financial knowledge
    documents = load_investor_principles()

    # Step2: Create vector database
    vector_store = create_vector_store(documents)

    # Step3: Build Graph
    graph = build_financial_graph()

    return graph, vector_store


def run_research(query: str):

    # This gives us a compiled LangGraph workflow, A FAISS vector store
    # Eg: Open the restraunt and prepare the kitchen
    graph, vector_store = initialize_graph()

    initial_state = {
        "query": query,
        "documents": [],
        "answer": "",
        "vector_store": vector_store,
        "route": ""
    }

    #LangGraph, start executing workflow using this initial state
    result = graph.invoke(initial_state)

    return result["answer"]

