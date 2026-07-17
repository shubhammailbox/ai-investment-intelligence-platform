
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from ai_models.api.routes import router

# creating the web application object
app = FastAPI(
    title = "Dhyanful Finance AI API",
    description = "AI Investment Research Platform",
    version  = "1.0.0")

app.include_router(router)

