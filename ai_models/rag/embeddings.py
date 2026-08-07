from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from typing import List

"""
What is the job of this file?
Suppose your library has 1000 books, someone walks in and ask do you have 
any book on investing. Now shall we read all 1000 books everytime? No. We will organise.
This is what this file is doing - prepare the library before sutomer arrives.

Documents --> Embedding Model --> Document Vectors --> FAISS Database

"""

def get_embeddings():
    """
    Initialise and return the embedding model

    LangChain uses the "text-embedding-3-small" embedding model to convert every document
    into vector embeddings
    
    Returns:
        OpenAIEmbeddings: Embedding model instance.
    
    """

    return OpenAIEmbeddings(
        # Below is the change we did lately due to newer OpenAI SDK's, Langchain updates and tokenizer mappings
        model="text-embedding-3-small"
    )

def create_vector_store(documents: List[Document]):
    """
    Create a FAISS vector store from documents.

    IMP: This function converts LangChain documents into embeddings and stores them 
    in a FAISS vector database for similarity search.

    Eg: Suppose you have 3 documents:

    Document 1:Amazon Revenue increased
    Document 2:Apple launched new iPhone
    Document 3:Microsoft Azure Growth

    Instead of storinng only texts, LangChain asks the embedding model  - can you tell me
    the meaning of this document. Post that FAISS stores - 

    Vector A → Amazon document
    Vector B → Apple document
    Vector C → Microsoft document

    That's all. Later -  If the user query is - tell me about microsoft cloud business, 
    in the similarity search it compares question vector i.e microsoft with 3 documents Amazon vector, 
    Apple vector and microsoft vector from the embeddings. And it says Microsoft 98%,
    Amazon-45%, Apple -10% and it returns Microft document.
    
    Args:
        documents (List[Documents]): List of documents to index

    Returns:
        FAISS: Vector store instance.
    """

    # Reuse embedding model
    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(documents, embeddings)

    return vector_store