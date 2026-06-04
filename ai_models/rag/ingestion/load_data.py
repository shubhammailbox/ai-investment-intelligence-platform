import json
import os
from typing import List
from langchain.schema import Document


def load_investor_principles(path: str = "data/investor_principles_structured.json") -> List[Document]:
    """
    Load investor principles from a JSON file and convert them into LangChain Document objects.
    These LangChain Documents are type of data structures only.

    This function reads a structured JSON file containing investment principles
    (with author and text), and transforms each entry into a Document suitable
    for embedding and retrieval in a RAG pipeline.

    Each principle is converted into a Document where:
    - page_content contains the author and the principle text
    - metadata contains additional attributes for filtering and traceability

    Args:
        path (str): File path to the investor principles JSON file.

    Returns:
        List[Document]: List of Document objects ready for embedding and retrieval.

    Raises:
        FileNotFoundError: If the JSON file does not exist at the given path.
        json.JSONDecodeError: If the file is not a valid JSON.
    """

    # Step1: Initiate the List
    documents: List[Document] = []

    # Step2: Load JSON file
    with open(path, "r") as f:
        data = json.load(f)

    # Extract principles list safely
    principles = data.get("principles", [])

    # Document creation
    for item in principles:
        principle = item.get("principle","")
        details   = item.get("details", "")
        framework = item.get("framework", "")
        author    = item.get("author","")


        doc = Document (
            page_content= f"{principle}.{details}",
            metadata ={
                "framework": framework,
                "author": author,
                "time_horizon": item.get("time_horizon", ""),
                "tags":item.get("tags",[]),                       
                "source": "investor_principles_structured",
                "type" : "principles"
            }
        )

        documents.append(doc)

    return documents


if __name__ == "__main__":
    print("Running load_data module...")
    print("Current working directory:", os.getcwd())

    docs = load_investor_principles()

    print(f"Loaded {len(docs)} documents.\n")

    for d in docs[:6]:
        print(d.page_content)
        print(d.metadata)
        print("------")