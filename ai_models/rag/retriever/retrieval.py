from typing import List
from langchain.schema import Document
from langsmith import traceable

@traceable(name="Retrieve Documents")
def retrieve_documents(query:str, vector_store, k: int = 5) -> List[Document]:
    print("RETRIEVAL FUNCTION CALLED")
    
    """

    Retrieve relevant documents based on user query.

    Imp:During retrieval when similarity_search(query) is executed,
    LangChain autoamtically converts the user query into an embedding using the 
    same embedding model.

    What input does it need?
    Args:
        query (str): User Query
        vector_store: FAISS vector database
        k(int): Number of documents to retrieve

    Returns:
        This function retun list of LangChain documents.
        List[Document]: Top relevant documents
    
    """

    # This is the main logic in here 
    results = vector_store.similarity_search(query, k=k)
    
    return results


