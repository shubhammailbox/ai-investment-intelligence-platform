from langchain_openai import ChatOpenAI
from ai_models.tools.market_data_tools import get_market_data

llm = ChatOpenAI(model = "gpt-4o-mini")

# tool binding with LLM
llm_with_tools = llm.bind_tools([get_market_data])

response = llm_with_tools.invoke("What is the current price of Marvell stock?")

print (response)
