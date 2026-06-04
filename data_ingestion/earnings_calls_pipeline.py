"""
Ingests earnings call data for multiple companies and stores it in AWS S3.
Acts as the data ingestion layer of the pipeline, generating raw transcripts.
"""

import requests
import json
import boto3
from datetime import datetime

API_KEY = "eWyM019hTgT2d6YcKTlsUhaRLFhdxrvn"
S3_BUCKET = "ai-investment-intelligence-data-dhyanful"

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "NFLX"]


def fetch_transcript(ticker):

    transcripts = {
        "AAPL": "Apple reported strong iPhone and services growth but highlighted supply chain risks.",
        "MSFT": "Microsoft showed strong cloud growth driven by Azure and AI investments.",
        "GOOGL": "Google reported strong advertising revenue but mentioned competition in AI space.",
        "AMZN": "Amazon reported strong AWS growth but rising logistics costs impacted margins.",
        "META": "Meta highlighted strong ad recovery and investments in AI infrastructure.",
        "NVDA": "NVIDIA reported explosive growth driven by AI chip demand.",
        "TSLA": "Tesla showed growth in EV deliveries but faced pricing pressure.",
        "NFLX": "Netflix reported strong subscriber growth and expansion into gaming."
    }

    return {
        "company": ticker,
        "date": str(datetime.now().date()),
        "transcript": transcripts.get(ticker, "No data available")
    }


def upload_to_s3(data, ticker):

    s3 = boto3.client("s3")

    file_name = f"earnings_calls/{ticker}_{datetime.now().date()}.json"

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=file_name,
        Body=json.dumps(data)
    )

    print(f"Uploaded {ticker} transcript to S3")


def run_pipeline():

    for ticker in tickers:

        print(f"Fetching transcript for {ticker}")

        transcript = fetch_transcript(ticker)

        if transcript:
            upload_to_s3(transcript, ticker)


if __name__ == "__main__":
    run_pipeline()