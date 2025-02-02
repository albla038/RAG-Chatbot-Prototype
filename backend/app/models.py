# Pydantic models
from pydantic import BaseModel

class QueryReqBody(BaseModel):
  query: str
  context: str = ""
  id: int = 0