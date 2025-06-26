from fastapi import FastAPI
from pydantic import BaseModel
from agent.langgraph_agent import langgraph_agent

app = FastAPI()

class ChatRequest(BaseModel):
    text: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = langgraph_agent(req.text)
    return {"reply": response}
