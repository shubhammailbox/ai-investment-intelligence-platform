"""
Generates reasoning-based investment guidance by combining market context,
company insights, and investor principles using an LLM.
"""

from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

from ai_models.langchain.mf_recommender import recommend_mutual_funds
import json
import os

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found. Please check your .env file."
    )

# -------------------------------
# Load Investor Principles
# -------------------------------
def load_principles():
    """
    Loads investor principles from JSON file.
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "investor_principles.json")

    with open(file_path, "r") as f:
        data = json.load(f)

    return data["principles"]


# -------------------------------
# Format Principles for Prompt
# -------------------------------
def format_principles(principles):
    """
    Converts structured principles into readable text for LLM.
    """

    return "\n".join(
        [f"{p['author']}: {p['text']}" for p in principles]
    )


# -------------------------------
# Generate Investment Advice
# -------------------------------
def generate_investment_advice(market_context, company_insights):
    """
    Combines:
    - Market context
    - Company insights
    - Investor principles

    And generates reasoning-based investment guidance.
    """

    principles = load_principles()
    formatted_principles = format_principles(principles)

    prompt = f"""
    You are an AI investment advisor inspired by Warren Buffett and Charlie Munger.

    Your role is to guide investors on HOW TO THINK, not what to buy or sell.

    ---------------------
    Market Context:
    {market_context}

    ---------------------
    Company Insights:
    {company_insights}

    ---------------------
    Investor Principles:
    {formatted_principles}

    ---------------------

    Provide:

    1. What is happening in the market
    2. How a long-term investor should think
    3. Key risks to consider

    Important Rules:
    - Do NOT give direct buy/sell advice
    - Keep it simple and clear
    - Focus on reasoning, not prediction
    - Think like a disciplined long-term investor

    Return in clean text format.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def get_mutual_fund_investment_advice():

    mf_data = recommend_mutual_funds(age=30, risk="high")

    print("Mutual Fund Recommendations:")
    print(mf_data)

# -------------------------------
# TEST BLOCK
# -------------------------------
if __name__ == "__main__":

    # Example Market Context
    market_context = {
        "nifty_level": 22900,
        "trend": "market correction",
        "macro": "geopolitical tensions and global uncertainty"
    }

    # Example Company Insights (you can replace with S3 output later)
    company_insights = [
        {
            "company": "AAPL",
            "confidence": "High",
            "growth_signals": ["AI-driven growth", "Strong services revenue"],
            "risk_signals": ["Macroeconomic slowdown"]
        },
        {
            "company": "MSFT",
            "confidence": "High",
            "growth_signals": ["Cloud growth", "AI integration"],
            "risk_signals": ["Enterprise spending slowdown"]
        }
    ]

    advice = generate_investment_advice(market_context, company_insights)

    print("\nAI Investment Advice:\n")
    print(advice)