"""
AI Search API Python Client Library

A Python client library for the AI Search API that provides intelligent search
capabilities with context awareness and semantic understanding.

Example:
    ```python
    from aisearchapi import AISearchAPIClient, ChatMessage
    
    client = AISearchAPIClient(api_key='your-api-key-here')
    
    # Basic search
    result = client.search(prompt='What is machine learning?')
    print(result.answer)
    
    # Search with context
    result = client.search(
        prompt='What are the main advantages?',
        context=[ChatMessage(role='user', content='I am researching solar energy')],
        response_type='markdown'
    )
    
    # Check balance
    balance = client.balance()
    print(f'Available credits: {balance.available_credits}')
    ```
"""

from .client import AISearchAPIClient
from .types import (
    ChatMessage,
    SearchRequest,
    SearchResponse,
    BalanceResponse,
    ClientConfig,
    AISearchAPIError,
    ResponseType,
    ChatMessageRole
)

__version__ = "1.0.0"
__author__ = "AI Search API"
__email__ = "support@aisearchapi.io"

__all__ = [
    # Main client class
    "AISearchAPIClient",
    
    # Data classes and types
    "ChatMessage",
    "SearchRequest", 
    "SearchResponse",
    "BalanceResponse",
    "ClientConfig",
    
    # Exception classes
    "AISearchAPIError",
    
    # Type aliases
    "ResponseType",
    "ChatMessageRole",
]