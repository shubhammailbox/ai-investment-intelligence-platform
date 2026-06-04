import json

def analyze_transcript(transcript_data):    
    """
    Analyzes an earnings call transcript and extracts key investment signals.
    This script takes a transcript, runs it through a function that looks for growth and risk keywords, and then returns structured insights.

    Parameters:
        transcript_data (dict): Contains company name and transcript text

    Returns:
        dict: Structured insights including:
            - company
            - confidence level
            - growth signals
            - risk signals    
    """

    text = transcript_data["transcript"].lower()

    result = {
        "company": transcript_data["company"],
        "confidence": "Neutral",
        "growth_signals": [],
        "risk_signals": []
    }

    # Simple keyword-based AI (v1)
    if "strong" in text or "growth" in text:
        result["confidence"] = "High"
        result["growth_signals"].append("Positive growth commentary")

    if "risk" in text or "uncertainty" in text:
        result["risk_signals"].append("Risk mentioned by management")

    return result


# Test
if __name__ == "__main__":

    sample = {
        "company": "AAPL",
        "transcript": "The company reported strong growth but highlighted risks due to macroeconomic conditions."
    }

    analysis = analyze_transcript(sample)

    print(json.dumps(analysis, indent=2))