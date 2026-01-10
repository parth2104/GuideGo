from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agents
import uvicorn

app=FastAPI(title="AI Agent")
model_names=["gpt-5-mini-2025-08-07","llama-3.1-8b-instant"]


class RequestStatus(BaseModel):
    model_name:str
    model_provider: str
    system_prompt: str
    messages: str


@app.post("/chat")
def chat_end_point(request:RequestStatus):
    """
    API end point of chatmodel
    """
    if request.model_name not in model_names:
        return {"error":"Please select active model"}
    
    model_name= request.model_name
    model_provider =request.model_provider
    prompt=request.system_prompt
    query=request.messages
    

    response=get_response_from_ai_agents(model_name,model_provider,prompt,query)

    return response
    








