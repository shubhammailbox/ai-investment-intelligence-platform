"""
Uses an LLM to analyze earnings call transcripts and extract structured insights
such as confidence, growth signals, and risk factors.
"""
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
client = OpenAI()

import json
import os

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found. Please check your .env file."
    )


def analyze_transcript_llm(transcript_data):

    transcript = transcript_data["transcript"]
    company = transcript_data["company"]

    prompt = f"""
    You are a financial analyst.

    Analyze the following earnings call transcript and extract:

    1. Management confidence (High / Medium / Low)
    2. Growth signals
    3. Risk factors

    Return output in JSON format like:
    {{
        "company": "{company}",
        "confidence": "...",
        "growth_signals": [...],
        "risk_signals": [...]
    }}

    Transcript:
    {transcript}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result_text = response.choices[0].message.content.strip()

    # Remove markdown formatting if present
    if result_text.startswith("```"):
        result_text = result_text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(result_text)
    except:
        return {"error": result_text}


# Test
if __name__ == "__main__":

    sample = {
        "company": "AAPL",
        "transcript": "The company reported strong growth driven by AI but highlighted risks due to macroeconomic uncertainty."
    }

    result = analyze_transcript_llm(sample)

    print(json.dumps(result, indent=2))