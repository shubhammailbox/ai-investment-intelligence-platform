"""
End-to-end pipeline that reads raw transcripts from S3, applies LLM analysis,
and stores structured insights back into S3.
"""

import boto3
import json
from ai_models.earnings_analysis import analyze_transcript
from ai_models.llm_analysis import analyze_transcript_llm

S3_BUCKET = "ai-investment-intelligence-data-dhyanful"


def get_files_from_s3():

    s3 = boto3.client("s3")

    response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix="earnings_calls/")

    files = []

    if "Contents" in response:
        for obj in response["Contents"]:
            files.append(obj["Key"])

    return files


def read_file_from_s3(file_key):

    s3 = boto3.client("s3")

    response = s3.get_object(Bucket=S3_BUCKET, Key=file_key)

    content = response["Body"].read().decode("utf-8")

    return json.loads(content)


def save_to_s3(data, file_key):

    s3 = boto3.client("s3")

    # Convert raw file path → processed path
    new_key = file_key.replace("earnings_calls/", "processed/").replace(".json", "_analysis.json")

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=new_key,
        Body=json.dumps(data)
    )

    print(f"Saved analysis to S3: {new_key}")


def run_pipeline():

    files = get_files_from_s3()

    print(f"Found {len(files)} files in S3")

    for file_key in files:

        print(f"\nProcessing file: {file_key}")

        data = read_file_from_s3(file_key)

        result = analyze_transcript_llm(data)

        print("AI Insights:")
        print(json.dumps(result, indent=2))

        # saving the result back to s3 bucket
        save_to_s3(result, file_key)


if __name__ == "__main__":
    run_pipeline()