"""
routes.py

Purpose
-------
Defines the REST API endpoints
for the Dhyanful Finance AI Platform.

"""

from fastapi import APIRouter
from ai_models.agents.langgraph.graph_service import run_research

from ai_models.api.models import (
    ResearchRequest,
    ResearchResponse
)

router = APIRouter()


@router.get("/")
def home():
    """
    Home endpoint.
    """

    return {
        "message": "Welcome to Dhyanful Finance AI API"
    }


@router.get("/health")
def health_check():
    """
    Health check endpoint.

    Used by monitoring systems
    to verify the service is running.
    """

    return {
        "status": "healthy"
    }


@router.post("/research", response_model=ResearchResponse)
def investment_research(
    request: ResearchRequest
):

    """
    AI Investment Research Endpoint.
    The API simply calls the service

    """
    print("\n===== API CALLED =====")
    print(request.query)

    answer = run_research(request.query)

    return ResearchResponse(
        answer=answer
    )