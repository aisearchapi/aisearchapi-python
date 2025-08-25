# AI Search API Python Client

[![PyPI version](https://badge.fury.io/py/aisearchapi.svg)](https://badge.fury.io/py/aisearchapi-client)
[![Python Support](https://img.shields.io/pypi/pyversions/aisearchapi.svg)](https://pypi.org/project/aisearchapi-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python client library for the AI Search API that provides intelligent search capabilities with context awareness and semantic understanding.

## Features

- **🔍 Intelligent Search**: Leverage advanced embedding techniques for semantic search
- **🎯 Context Awareness**: Provide conversation context to enhance search results
- **⚡ Simple API**: Easy-to-use interface with comprehensive error handling
- **🛡️ Type Safe**: Full type hints support for better development experience
- **🔄 Flexible Responses**: Support for both text and markdown formatted responses
- **💰 Balance Tracking**: Check your API credit usage

## Installation

Install the package using pip:

```bash
pip install aisearchapi-client
```

Or install from source:

```bash
git clone https://github.com/aisearchapi/aisearchapi-python.git
cd aisearchapi-python
pip install -e .
```

<!-- For development with optional dependencies: -->

<!-- ```bash
pip install -e ".[dev,test]"
``` -->

## Quick Start

### Basic Usage

```python
from aisearchapi-client import AISearchAPIClient

# Initialize the client
client = AISearchAPIClient(api_key='your-api-key-here')

# Perform a basic search
result = client.search(
    prompt='What is machine learning and how does it work?',
    response_type='markdown'
)

print("Answer:", result.answer)
print("Sources:", result.sources)
print(f"Total time: {result.total_time}ms")

# Check your account balance
balance = client.balance()
print(f"Available credits: {balance.available_credits}")

# Always close the client when done
client.close()
```

### Using Context Manager (Recommended)

```python
from aisearchapi-client import AISearchAPIClient, ChatMessage

# Use context manager for automatic resource cleanup
with AISearchAPIClient(api_key='your-api-key-here') as client:
    
    # Search with conversation context
    result = client.search(
        prompt='What are the main advantages and disadvantages?',
        context=[
            ChatMessage(role='user', content='I am researching solar energy for my home'),
            ChatMessage(role='user', content='I live in a sunny climate with high electricity costs')
        ],
        response_type='text'
    )
    
    print("Contextual Answer:", result.answer)
```

### Advanced Configuration

```python
from aisearchapi-client import AISearchAPIClient

client = AISearchAPIClient(
    api_key='your-api-key-here',
    base_url='https://api.aisearchapi.io',  # Custom base URL
    timeout=60  # Custom timeout in seconds
)
```

## API Reference

### `AISearchAPIClient`

#### Constructor

```python
AISearchAPIClient(
    api_key: str,
    base_url: str = "https://api.aisearchapi.io",
    timeout: int = 30
)
```

- **api_key** (str): Your API bearer token
- **base_url** (str, optional): Base URL for the API endpoints
- **timeout** (int, optional): Request timeout in seconds

#### Methods

##### `search(prompt, context=None, response_type=None)`

Perform an AI-powered search with optional conversation context.

**Parameters:**
- **prompt** (str): The main search query
- **context** (List[ChatMessage], optional): Conversation context for enhanced understanding
- **response_type** (str, optional): Response format ('text' or 'markdown')

**Returns:**
- **SearchResponse**: Object containing answer, sources, response_type, and total_time

**Example:**
```python
result = client.search(
    prompt='Explain quantum computing',
    context=[ChatMessage(role='user', content='I am a computer science student')],
    response_type='markdown'
)
```

##### `balance()`

Check your current account balance and available API credits.

**Returns:**
- **BalanceResponse**: Object containing available_credits

**Example:**
```python
balance = client.balance()
if balance.available_credits < 10:
    print("Warning: Low credit balance!")
```

### Data Classes

#### `ChatMessage`

```python
@dataclass
class ChatMessage:
    role: str  # Currently only 'user' is supported
    content: str  # The message content
```

#### `SearchResponse`

```python
@dataclass
class SearchResponse:
    answer: str  # AI-generated response
    sources: List[str]  # List of sources used
    response_type: str  # Format of the response
    total_time: int  # Processing time in milliseconds
```

#### `BalanceResponse`

```python
@dataclass
class BalanceResponse:
    available_credits: int  # Number of available API credits
```

## Error Handling

The client provides comprehensive error handling with custom exception types:

```python
from aisearchapi-client import AISearchAPIClient, AISearchAPIError

try:
    with AISearchAPIClient(api_key='your-api-key') as client:
        result = client.search(prompt='Your search query')
        print(result.answer)
        
except AISearchAPIError as e:
    print(f"API Error [{e.status_code}]: {e.description}")
    if e.response:
        print("Response data:", e.response)
        
except ValueError as e:
    print(f"Validation Error: {e}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Error Codes

| Status Code | Error Type | Description |
|------------|------------|-------------|
| 401 | Unauthorized | Invalid API key |
| 429 | Too Many Requests | Rate limit exceeded |
| 433 | Quota Exceeded | Account message quota reached |
| 500 | Server Error | Internal server error |
| 503 | Service Unavailable | API temporarily down |

## Environment Variables

You can set your API key using environment variables:

```bash
export AI_SEARCH_API_KEY="your-api-key-here"
```

Then use it in your code:

```python
import os
from aisearchapi-client import AISearchAPIClient

api_key = os.getenv('AI_SEARCH_API_KEY')
client = AISearchAPIClient(api_key=api_key)
```

## Examples

Check out the [examples](examples/) directory for more comprehensive usage examples:

- [basic_usage.py](examples/basic_usage.py) - Basic search and balance checking
- [contextual_search.py](examples/contextual_search.py) - Using conversation context
- [error_handling.py](examples/error_handling.py) - Comprehensive error handling
- [async_usage.py](examples/async_usage.py) - Async/await patterns

## Requirements

- Python 3.8 or higher
- requests >= 2.25.0
- typing-extensions >= 4.0.0 (for Python < 3.10)

## Development

### Setting up for development

```bash
git clone https://github.com/aisearchapi/aisearchapi-python.git
cd aisearchapi-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev,test]"
```

### Running tests

```bash
pytest
```

### Code formatting

```bash
# Format code
black .
isort .

# Lint code  
flake8 .
mypy .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [https://docs.aisearchapi.io/](https://docs.aisearchapi.io)
- **Issues**: [GitHub Issues](https://github.com/aisearchapi/aisearchapi-python/issues)
- **Email**: admin@aisearchapi.io

## Changelog

## Acknowledgments

- Built with [requests](https://requests.readthedocs.io/) for HTTP handling
- Type hints support with [typing-extensions](https://github.com/python/typing_extensions)
- Inspired by modern API client design patterns