"""
Configuration Management
"""

import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # LLM Configuration
    MODEL_NAME: str = "gemma:2b"  # or "llama3:8b"
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_TIMEOUT: int = 120
    
    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "sqlite:///./haseena_bibi.db"
    
    # Security (optional)
    API_KEY: Optional[str] = None  # For LAN auth if needed
    
    # Prompt defaults
    SYSTEM_PROMPT: str = """You are Haseena Bibi, a witty, supportive CS Professor.
    Your students are in 5th semester BS CS. Help with:
    - Operating Systems
    - Database Management Systems
    - Software Engineering
    - Programming (Python, C++, Java)
    
    Be encouraging, use humor occasionally, and always explain concepts clearly.
    When given code, debug it and explain the logic line by line.
    """
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
