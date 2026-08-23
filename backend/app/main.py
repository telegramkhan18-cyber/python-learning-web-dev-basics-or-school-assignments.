"""
HASEENA BIBI — Backend Entry Point
Offline Hybrid AI Educational Assistant
"""

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.api.routes import chat, code, tasks, health
from app.core.llm_manager import LLMManager
from app.database.connection import init_db

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup & shutdown events"""
    logger.info("🚀 Starting Haseena Bibi Backend...")
    
    # Initialize LLM
    app.state.llm = LLMManager()
    logger.info(f"✅ Loaded model: {settings.MODEL_NAME}")
    
    # Initialize database
    await init_db()
    logger.info("✅ Database connected")
    
    yield
    
    # Shutdown cleanup
    logger.info("👋 Shutting down...")

# Initialize app
app = FastAPI(
    title="Haseena Bibi API",
    description="Offline Hybrid AI Assistant for CS Students",
    version="1.0.0",
    lifespan=lifespan
)

# CORS — allow mobile app on LAN
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(code.router, prefix="/api/v1/code", tags=["Code"])
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["Tasks"])
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])

@app.get("/")
async def root():
    return {
        "name": "Haseena Bibi",
        "status": "running",
        "model": settings.MODEL_NAME,
        "version": "1.0.0"
    }

# WebSocket endpoint for streaming
@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    # Streaming logic here
