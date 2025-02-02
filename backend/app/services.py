from .config import env

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

async def call_model(query: str, context: str = ""):
  llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key= env.OPENAI_API_KEY
    )
  
  llm_response = await llm.ainvoke([SystemMessage(content=context), HumanMessage(content=query)])

  return {
    "response": llm_response.content,
    "metadata": llm_response.response_metadata
  }
          