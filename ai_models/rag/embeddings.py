from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from typing import List


def get_embeddings():
    """
    Initialise and return the embedding model
    
    Returns:
        OpenAIEmbeddings: Embedding model instance.
    
    """

    return OpenAIEmbeddings(
        #Below is the chaneg we did lately due to newer OpenAI SDK's, Langchain updates and tokenizer mappings
        model="text-embedding-3-small"
    )

def create_vector_store(documents: List[Document]):
    """
    Create a FAISS vector store from documents.

    IMP: This function converts LangChain documents into embeddings and stores them 
    in a FAISS vector database for similarity search.
    
    Args:
        documents (List[Documents]): List of documents to index

    Returns:
        FAISS: Vector store instance.
    """

    # Reuse embedding model
    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(documents, embeddings)

    return vector_store