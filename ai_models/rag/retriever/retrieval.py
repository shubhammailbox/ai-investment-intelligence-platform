"""
In below implementation, I first create a FAISS vector store by calling FAISS.from_documents().
At that stage, LangChain uses the text-embedding-3-small embedding model to convert every 
document into vector embeddings and stores those vectors alongside the original documents 
and their metadata.

During retrieval, code simply calls similarity_search(query). Although I only pass 
the user's text query, LangChain automatically uses the same embedding model that was 
attached to the vector store during indexing to convert the query into an embedding.
FAISS then performs a semantic similarity search between the query vector and all stored
document vectors, retrieves the top-k nearest neighbors, and LangChain returns them as 
Document objects that I can pass into my RAG prompt."

"""



from typing import List
from langchain_core.documents import Document
from langsmith import traceable

@traceable(name="Retrieve Documents")
def retrieve_documents(query:str, vector_store, k: int = 5) -> List[Document]:
    print("RETRIEVAL FUNCTION CALLED")
    
    """

    Retrieve relevant documents based on user query.

    Imp:During retrieval when similarity_search(query) is executed,

    How does embeddings work: When a user asks a question, LangChain autoamtically converts 
    the user query into an embedding using the same embedding model to convert the question 
    into another vector. The vector database then performs a similarity search to find
    the document vectors that are closest to the query vector.

    For eg: If the user query is - tell me about microsoft cloud business, in the similarity 
    search it compares question vector i.e microsoft with 3 documents Amazon vector, 
    Apple vector and microsoft vector from the embeddings. And it says Microsoft 98%,
    Amazon-45%, Apple -10% and it returns Microft document.

    What input does it need?
    Args:
        query (str): User Query
        vector_store: FAISS vector database
        k(int): Number of documents to retrieve

    Returns:
        This function retun list of LangChain documents.
        List[Document]: Top relevant documents
    
    """

    # entire retrieval is happening here
    results = vector_store.similarity_search(query, k=k)
    
    return results


