"""
Type definitions and custom exceptions for AI Search API Python client.
"""

from typing import Literal, List, Dict, Any, Optional
from dataclasses import dataclass


# Type aliases
ResponseType = Literal['text', 'markdown']
ChatMessageRole = Literal['user']


@dataclass
class ChatMessage:
    """Individual chat message for providing conversation context."""
    role: ChatMessageRole
    content: str


@dataclass
class SearchRequest:
    """Parameters for the search API request."""
    prompt: str
    context: Optional[List[ChatMessage]] = None
    response_type: Optional[ResponseType] = None


@dataclass
class SearchResponse:
    """Successful response from the search API."""
    answer: str
    sources: List[str]
    response_type: ResponseType
    total_time: int


@dataclass
class BalanceResponse:
    """Response from the balance API."""
    available_credits: int


@dataclass
class ClientConfig:
    """Configuration options for the API client."""
    api_key: str
    base_url: str = "https://api.aisearchapi.io"
    timeout: int = 30


class AISearchAPIError(Exception):
    """Custom error class for API-related errors."""
    
    def __init__(self, description: str, status_code: Optional[int] = None, response: Optional[Dict[str, Any]] = None):
        super().__init__(description)
        self.description = description
        self.status_code = status_code
        self.response = response
        self.error = {
            "description": description
        }
    
    def __str__(self) -> str:
        if self.status_code:
            return f"AISearchAPIError [{self.status_code}]: {self.description}"
        return f"AISearchAPIError: {self.description}"