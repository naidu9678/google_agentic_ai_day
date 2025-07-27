import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Import your agent and ADK components
from vertexai.preview import reasoning_engines
import agent

# Import CORS middleware to allow your frontend to connect
from fastapi.middleware.cors import CORSMiddleware

# --- Initialization ---
app = FastAPI(
    title="Financial Agent API",
    description="An API for interacting with a multi-agent financial assistant.",
    version="1.0.0"
)

# This will now initialize correctly because the MODEL env var will be set.
agent_app = reasoning_engines.AdkApp(
    agent=agent.root_agent,
    enable_tracing=True,
)

# --- CORS Configuration ---
# Allows your frontend to communicate with this backend.
origins = [
    "https://financial-ai-backend-1084701352060.us-central1.run.app",
    "https://finadvisorai-chat.web.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Data Models ---
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = Field(None, description="The existing session ID.")
    user_id: str = Field("u_123", description="A unique identifier for the user.")

class ChatResponse(BaseModel):
    response: str
    session_id: str

# --- API Endpoint ---
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Handles a chat interaction with the financial agent.
    """
    try:
        current_session_id = request.session_id
        
        if not current_session_id:
            print("Creating a new session...")
            session = agent_app.create_session(user_id=request.user_id)
            current_session_id = session.id

        print(f"Using session ID: {current_session_id}")

        full_response = ""
        for event in agent_app.stream_query(
            user_id=request.user_id,
            session_id=current_session_id,
            message=request.message,
        ):
            text_part = event.get("content", {}).get("parts", [{}])[0].get("text")
            if text_part:
                full_response += text_part
        
        if not full_response:
            full_response = "The agent processed your request but did not return a text response."

        return ChatResponse(response=full_response, session_id=current_session_id)

    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

