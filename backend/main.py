#
# Masab's Support Agent - FastAPI Backend (Portfolio Version - Corrected)
#

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# <<< FIX: Removed 'load_knowledge_base' from this import, as it will live in this file now.
from agent_core import create_support_agent

app = FastAPI(
    title="Masab's AI Portfolio API",
    description="API for the AI agent that answers questions about Masab Farooque.",
    version="1.3.1" # Version bump for the crash fix
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    session_id: str = "portfolio_demo_session"

class ChatResponse(BaseModel):
    response: str

# <<< FIX: The load_knowledge_base function is now defined directly in main.py.
def load_knowledge_base():
    """Reads the knowledge base file and returns its content."""
    try:
        with open("knowledge_base.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "CRITICAL ERROR: knowledge_base.txt not found."

agent_with_history = create_support_agent()
KNOWLEDGE_BASE = load_knowledge_base()

@app.get("/", tags=["Status"])
def read_root():
    return {"status": "ok", "message": "Masab's AI Portfolio API is running."}

@app.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat_with_agent(request: ChatRequest):
    user_message = request.message

    augmented_input = f"""
PROFESSIONAL PROFILE & RESUME CONTEXT:
---
{KNOWLEDGE_BASE}
---

USER'S QUESTION:
{user_message}
"""

    try:
        config = {"configurable": {"session_id": request.session_id}}
        
        ai_response_obj = await agent_with_history.ainvoke(
            {"input": augmented_input},
            config=config
        )
        response_text = ai_response_obj.content
        
    except Exception as e:
        print(f"Error during agent invocation: {e}")
        response_text = "I'm having a little trouble right now. Please try again in a moment."

    return ChatResponse(response=response_text)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)