"""

evaluate_rag.py

Purpose:
---------

This module is responsible for evaluating the performance and quality 
of the Retrieval Augmented generation (RAG) pipeline.

The evaluation process includes:
1. Running the RAG pipeline end to end.
2. Measuring answer quality using RAGAS metrics
3. Detecting Hallucinations and relevancy issues
4. Sending traces to LangSmith for observability and debugging


Key Metrics:
------------

- Faithfulness:
    Measures whether the generated answer is grounded in the related context.

- Answer Relevancy:
    Measures how relevant the answer is to the users query.

Why This File Exists:
------------
The purpose of separating evaluation from testing is to maintain clean architecture and separation of responsibilities

- test_rag.py:
    Used for basic functional testing of the pipeline.

- evaluate_rag.py:
    Used for quality measurement, observability,
    benchmarking, and future experimentation.

Author:
-------
Shubham Mishra
"""

import os 

from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found. Please check your .env file."
    )

from datasets import Dataset

from ragas import evaluate
from ragas.metrics import Faithfulness, ResponseRelevancy

from langchain_openai import OpenAIEmbeddings
from langchain.callbacks import tracing_v2_enabled

from ai_models.rag.ingestion.load_data import load_investor_principles
from ai_models.rag.embeddings import create_vector_store
from ai_models.rag.pipeline.rag_pipeline import build_full_rag_pipeline

def main():
    """
    Run the complete RAG evaluation workflow.

    Workflow:
    -----------
    1. Load strcutured investment principles
    2. Create vector embeddings and FAISS vector store
    3. Define or Add Query which user wish to ask
    4. Execute the RAG pipeline - this step has retrieval as well (later we will create a separate .py)
    5. Evaluate generated answers using RAGAS
    6. Send traces to LangSmith

    Returns:
    ------
    None 
    """

    #Step1: Load strcutured investment principles
    documents = load_investor_principles()
    print(f"\n Loaded {len(documents)}documents")

    #Step 2: Create vector embeddings and FAISS vector store
    vector_store = create_vector_store(documents)
    print(f"\nVector store created sucessfully")

    #Step3: Define or Add user Query 
    query = "How should i build a long term portfolio for multibaggers?"
    print(f"\nRunning evaluation for query: \n{query}")

    #Step:4 Running the full RAG pipeline with Tracing
    with tracing_v2_enabled():
        answer,docs = build_full_rag_pipeline(
            query=query, 
            vector_store=vector_store)
        
    # Step5: Print generated answer
    print(f"\n-----ANSWER -------\n")
    print(answer)

    # Step:6 Prepare Evaluation Datasets
    data = {
        "question":[query],
        "answer":[answer],
        "contexts":[[doc.page_content for doc in docs]]
    }

    dataset = Dataset.from_dict(data)

    # Step7: Initialise Embedding Model
    embeddings = OpenAIEmbeddings()

    #Step8: Run RAGAS Evaluation
    result = evaluate(
        dataset,
        metrics=[Faithfulness(), ResponseRelevancy()],
        embeddings=embeddings
    )

    print(f"\n-----EVALUATION SCORES ARE--------\n")
    print(result)


if __name__ == "__main__":
    main()