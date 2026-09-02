"""
Keeping the FastAPI application layer modular. app.py is the application entry point. 
It loads environment configuration for local development, creates the FastAPI application 
with the API metadata, and registers the API router. 
The actual endpoint definitions are kept separately in routes.py, 
while request and response schemas are defined in models.py. 
This keeps the API wiring separate from the endpoint logic and data models.

"""

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from ai_models.api.routes import router

# creating the web application object
app = FastAPI(
    title = "Dhyanful Finance AI API",
    description = "AI Investment Research Platform",
    version  = "1.0.0")

# This is basically saying here are the API routes that this application should expose to
app.include_router(router)

