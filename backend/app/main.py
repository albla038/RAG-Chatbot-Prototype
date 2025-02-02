from fastapi import FastAPI
from .models import QueryReqBody
from .services import call_model
from .config import env

app = FastAPI()

@app.get("/")
async def root():
  return {"status": "ok", "message": "All systems up and running"}

@app.get("/key")
async def key():
  return {"message": "Hello user", "key": env.DEV_TEST_KEY}

@app.post("/ask")
async def ask(req_body: QueryReqBody):
  query = req_body.query
  context = req_body.context
  id = req_body.id

  model_response = await call_model(query, context)

  return {
    "model_response" : model_response,
    "user": {
      "query": query,
      "context": context,
      "id": id
      }
    }