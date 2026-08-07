
from typing import List,Tuple
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langsmith import traceable

from ai_models.rag.retriever.retrieval import retrieve_documents

@traceable(name = "RAG Pipeline")
def build_full_rag_pipeline(query: str, vector_store) -> Tuple[str, List[Document]]:

    """
    Execute full RAG pipeline

    Now this is the brain of the system.
    Goal of this pipeline is to take user query --> fetch the documents from vector DB
    --> setup a context (augumentation)--> generate the result
    
    Take a user query and return an AI-generated answer using retrieved knowledge”

    Steps:
    1. Retrive relevant documents
    2. Build context
    3. Generate prompt
    4. Call LLM

    Args:
        query (str): User Query
        vector store: FAISS vector database

    Returns:
        LLM output based on the matched results

    """

    # Step 1: Retrieve
    results = retrieve_documents(query, vector_store)

    # Step 2: Build Context (Augumnetation)
    context = "\n".join([doc.page_content for doc in results])

    # Step 3: Prompt
    # This is a new prompt that we will be using to increase the faithfulness metrics
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

    #Step 4: LLM  
    llm = ChatOpenAI(model = "gpt-4o-mini")
    response = llm.invoke(prompt)
    
    #Step 5: Return
    return response.content,results