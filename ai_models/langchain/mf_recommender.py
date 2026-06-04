from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import json


def clean_output(text):
    return text.replace("```json", "").replace("```", "").strip()


def recommend_mutual_funds(age: int, risk: str):
    
    llm = ChatOpenAI(model="gpt-4", temperature=0)

    prompt = PromptTemplate(
        input_variables=["age", "risk"],
        template="""
You are a financial advisor.

Return ONLY valid JSON.

Do NOT use markdown
Do NOT add explanation
Do NOT add any extra text

Only suggest Indian mutual funds.

Output format:
{{
  "funds": [
    {{
      "fund_name": "string",
      "reason": "string"
    }}
  ]
}}

Task:
Suggest exactly 3 mutual funds for:
- Age: {age}
- Risk: {risk}
"""
    )

    formatted_prompt = prompt.format(age=age, risk=risk)

    response = llm.invoke(formatted_prompt)

    cleaned = clean_output(response.content)

    try:
        parsed = json.loads(cleaned)
        return parsed
    except:
        return {"error": "Parsing failed", "raw_output": cleaned}


def load_investor_principles():
    with open("data/investor_principles.json", "r") as f:
        return json.load(f)
    
def format_principles(principles):
    return json.dumps(principles, indent=2)

# TEST CODE
if __name__ == "__main__":
    result = recommend_mutual_funds(28, "high")
    
    import json
    print(json.dumps(result, indent=2))