"""
models.py

Purpose
-------
Defines the request and response models
used by the FastAPI application.

Using Pydantic models gives us:
- Automatic validation
- Type safety
- API documentation
- Serialization

"""

from pydantic import BaseModel


class ResearchRequest(BaseModel):
    """
    Request model for investment research.
    """

    query: str


class ResearchResponse(BaseModel):
    """
    Response returned by the AI.
    """

    answer: str