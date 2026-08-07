"""

My implementation has two stages. During indexing, I use embeddings.py 
to convert all documents into vector embeddings and store them in a FAISS vector database. 
This happens once when the knowledge base is prepared. During retrieval, retrieval.py 
receives the user's question. LangChain automatically converts that question into an 
embedding using the same embedding model, performs a similarity search against the 
stored vectors, and returns the most relevant documents. My RAG pipeline then uses those 
retrieved documents as context for the LLM to generate an accurate, grounded response."

"""



import os

from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found. Please check your .env file."
    )

from ai_models.rag.ingestion.load_data import load_investor_principles
from ai_models.rag.embeddings import create_vector_store
from ai_models.rag.pipeline.rag_pipeline import build_full_rag_pipeline

from ragas import evaluate
from ragas.metrics import Faithfulness, ResponseRelevancy
from datasets import Dataset
from langchain_openai import OpenAIEmbeddings

def main():
    # Step: Load data
    documents = load_investor_principles()

    # Step: Create vector store
    vector_store = create_vector_store(documents)

    # Query
    #query = "What are key investing principles?"
    #query = "How can I find multibagger stocks?"
    #query = "How can I invest in US markets for Vanguard ETF's"
    query = "How should I build a long term portfolio for moderate investor type?"

    # Run pipeline where we are retrieving as well
    answer, docs = build_full_rag_pipeline(query, vector_store)

    # Adding Evaluation Block As We need to check if LLM is hallucinating 
    data = {
    "question": [query],
    "answer": [answer],
    "contexts": [[doc.page_content for doc in docs]]
            }

    dataset = Dataset.from_dict(data)

    # Step: Run evaluation
    embeddings = OpenAIEmbeddings()

    result = evaluate(
        dataset,
        metrics=[Faithfulness(),ResponseRelevancy()],
        embeddings=embeddings
            )
    
    print("\n--- ANSWER ---\n")
    print(answer)

    print("\n--- EVALUATION ---\n")
    print(result)


if __name__ == "__main__":
    main()