"""
AI Search API Client for Python

Provides easy-to-use methods for interacting with the AI Search API,
including intelligent search with context awareness and account balance checking.

Example:
    ```python
    from aisearchapi import AISearchAPIClient
    
    client = AISearchAPIClient(api_key='your-api-key-here')
    
    # Perform a search
    result = client.search(
        prompt='What is machine learning?',
        response_type='markdown'
    )
    
    # Check account balance
    balance = client.balance()
    ```
"""

import json
import requests
from typing import List, Optional, Dict, Any

from .types import (
    ClientConfig, SearchRequest, SearchResponse, BalanceResponse, 
    ChatMessage, ResponseType, AISearchAPIError
)


class AISearchAPIClient:
    """AI Search API Client for Python"""
    
    def __init__(self, api_key: str, base_url: str = "https://api.aisearchapi.io", timeout: int = 30):
        """
        Initialize the AI Search API client
        
        Args:
            api_key: Your API bearer token (without 'Bearer ' prefix)
            base_url: Base URL for the API endpoints
            timeout: Request timeout in seconds
            
        Raises:
            ValueError: If api_key is not provided
        """
        if not api_key:
            raise ValueError("API key is required")
            
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        
        # Setup session for connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'User-Agent': 'aisearchapi-python/1.0.0'
        })
    
    def search(
        self,
        prompt: str,
        context: Optional[List[ChatMessage]] = None,
        response_type: Optional[ResponseType] = None
    ) -> SearchResponse:
        """
        Perform an AI-powered search with optional conversation context
        
        This method sends your search query to the API, which processes it using
        advanced embedding techniques and returns an intelligent response with sources.
        
        Args:
            prompt: The main search query
            context: Optional conversation context to enhance understanding
            response_type: Response format preference ('text' or 'markdown')
            
        Returns:
            SearchResponse containing the answer, sources, and metadata
            
        Raises:
            AISearchAPIError: If the API request fails
            ValueError: If request parameters are invalid
            
        Example:
            ```python
            result = client.search(
                prompt='Explain quantum computing',
                context=[
                    ChatMessage(role='user', content='I am a computer science student')
                ],
                response_type='markdown'
            )
            
            print(result.answer)
            print('Sources:', result.sources)
            print('Processing time:', result.total_time, 'ms')
            ```
        """
        # Validate request parameters
        self._validate_search_request(prompt, context, response_type)
        
        url = f"{self.base_url}/v1/search"
        
        # Build request body
        body = {"prompt": prompt}
        
        if context:
            body["context"] = [{"role": msg.role, "content": msg.content} for msg in context]
        
        if response_type:
            body["response_type"] = response_type
        
        try:
            response = self.session.post(url, json=body, timeout=self.timeout)
            
            if not response.ok:
                self._handle_error_response(response)
            
            data = response.json()
            
            # Convert to SearchResponse dataclass
            return SearchResponse(
                answer=data['answer'],
                sources=data['sources'],
                response_type=data['response_type'],
                total_time=data['total_time']
            )
            
        except requests.exceptions.Timeout:
            raise AISearchAPIError(f"Request timeout after {self.timeout} seconds")
        except requests.exceptions.RequestException as e:
            raise AISearchAPIError(f"Search request failed: {str(e)}")
        except (KeyError, ValueError) as e:
            raise AISearchAPIError(f"Invalid response format: {str(e)}")
    
    def balance(self) -> BalanceResponse:
        """
        Check your current account balance and available API credits
        
        Returns:
            BalanceResponse containing available credits information
            
        Raises:
            AISearchAPIError: If the API request fails
            
        Example:
            ```python
            balance = client.balance()
            print('Available credits:', balance.available_credits)
            
            if balance.available_credits < 10:
                print('Warning: Low credit balance!')
            ```
        """
        url = f"{self.base_url}/v1/balance"
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            
            if not response.ok:
                self._handle_error_response(response)
            
            data = response.json()
            
            # Convert to BalanceResponse dataclass
            return BalanceResponse(available_credits=data['available_credits'])
            
        except requests.exceptions.Timeout:
            raise AISearchAPIError(f"Request timeout after {self.timeout} seconds")
        except requests.exceptions.RequestException as e:
            raise AISearchAPIError(f"Balance request failed: {str(e)}")
        except (KeyError, ValueError) as e:
            raise AISearchAPIError(f"Invalid response format: {str(e)}")
    
    def _validate_search_request(
        self,
        prompt: str,
        context: Optional[List[ChatMessage]] = None,
        response_type: Optional[ResponseType] = None
    ) -> None:
        """Validate search request parameters"""
        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt is required and must be a string")
        
        if context is not None:
            if not isinstance(context, list):
                raise ValueError("Context must be a list of ChatMessage objects")
            
            for message in context:
                if not isinstance(message, ChatMessage):
                    raise ValueError("Each context item must be a ChatMessage object")
                
                if message.role != 'user':
                    raise ValueError('Each context message must have role "user"')
                
                if not message.content or not isinstance(message.content, str):
                    raise ValueError("Each context message must have content as a string")
        
        if response_type and response_type not in ['text', 'markdown']:
            raise ValueError('response_type must be either "text" or "markdown"')
    
    def _handle_error_response(self, response: requests.Response) -> None:
        """Handle and parse API error responses"""
        error_message = f"HTTP {response.status_code}"
        error_data = None
        
        try:
            error_data = response.json()
            # Handle nested error format: { "error": { "description": "message" } }
            if isinstance(error_data, dict):
                if 'error' in error_data:
                    if isinstance(error_data['error'], dict) and 'description' in error_data['error']:
                        error_message = error_data['error']['description']
                    elif isinstance(error_data['error'], str):
                        error_message = error_data['error']
                elif 'message' in error_data:
                    error_message = error_data['message']
        except (json.JSONDecodeError, ValueError):
            # Response body is not JSON or empty
            pass
        
        # Provide helpful error messages for common status codes
        status_messages = {
            401: 'Unauthorized',
            429: 'Too many requests',
            433: 'Account is at or over message quota',
            500: 'Server error',
            503: 'Service unavailable'
        }
        
        if response.status_code in status_messages:
            error_message = status_messages[response.status_code]
        
        raise AISearchAPIError(error_message, response.status_code, error_data)
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close session"""
        self.session.close()
    
    def close(self):
        """Close the underlying session"""
        self.session.close()