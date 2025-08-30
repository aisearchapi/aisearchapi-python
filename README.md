# AI Search API Python Client

[![PyPI version](https://badge.fury.io/py/aisearchapi-client.svg)](https://badge.fury.io/py/aisearchapi-client)
[![Python Support](https://img.shields.io/pypi/pyversions/aisearchapi-client.svg)](https://pypi.org/project/aisearchapi-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **Python client library for the [AI Search API](https://aisearchapi.io/)** that provides **semantic search, contextual awareness, and intelligent AI-powered results**.  
This package makes it easy for developers to integrate the [AI Search API](https://docs.aisearchapi.io/) into Python projects.

👉 To start, get your **free API key** from the [AI Search API dashboard](https://app.aisearchapi.io/dashboard).

---

## Features

- **🔍 AI-Powered Semantic Search**: Leverage advanced embeddings for natural language search
- **🎯 Context Awareness**: Add conversation history for smarter results
- **⚡ Simple API Client**: Clean and Pythonic interface with strong error handling
- **🛡️ Type Safety**: Full type hints for modern development
- **🔄 Flexible Output**: Choose between plain text or markdown responses
- **💰 Usage Tracking**: Monitor your [API credit balance](https://app.aisearchapi.io/dashboard) anytime

---

## Installation

Install from [PyPI](https://pypi.org/project/aisearchapi-client/):

```bash
pip install aisearchapi-client
```

Or install from source:

```bash
git clone https://github.com/aisearchapi/aisearchapi-python.git
cd aisearchapi-python
pip install -e .
```

---

## Quick Start

### Get Your API Key

1. Sign up at [aisearchapi.io](https://aisearchapi.io/).  
2. Log in to the [dashboard](https://app.aisearchapi.io/login).  
3. Copy your API key.  

Use this key when creating a client:

```python
from aisearchapi_client import AISearchAPIClient

client = AISearchAPIClient(api_key="your-api-key-here")
```

### Basic Usage Example

```python
from aisearchapi_client import AISearchAPIClient

client = AISearchAPIClient(api_key="your-api-key-here")

result = client.search(
    prompt="What is machine learning and how does it work?",
    response_type="markdown"
)

print("Answer:", result.answer)
print("Sources:", result.sources)
print(f"Total time: {result.total_time}ms")

balance = client.balance()
print(f"Available credits: {balance.available_credits}")
client.close()
```

---

## Advanced Usage

### Contextual Search

```python
from aisearchapi_client import AISearchAPIClient, ChatMessage

with AISearchAPIClient(api_key="your-api-key-here") as client:
    result = client.search(
        prompt="What are the main advantages and disadvantages?",
        context=[
            ChatMessage(role="user", content="I am researching solar energy for my home"),
            ChatMessage(role="user", content="I live in a sunny climate with high electricity costs")
        ],
        response_type="text"
    )
    print("Contextual Answer:", result.answer)
```

### Custom Configuration

```python
client = AISearchAPIClient(
    api_key="your-api-key-here",
    base_url="https://api.aisearchapi.io",
    timeout=60
)
```

---

## API Reference

Full API reference is available in the [official documentation](https://docs.aisearchapi.io/).

### `AISearchAPIClient`

#### Constructor

```python
AISearchAPIClient(
    api_key: str,
    base_url: str = "https://api.aisearchapi.io",
    timeout: int = 30
)
```

- **api_key**: Get yours from the [dashboard](https://app.aisearchapi.io/dashboard)
- **base_url**: Optional custom endpoint
- **timeout**: Timeout in seconds

#### Methods

- **search(prompt, context=None, response_type=None)** → Perform an AI-powered semantic search
- **balance()** → Check current credit usage

For more, see [API docs](https://docs.aisearchapi.io/).

---

## Error Handling

```python
from aisearchapi_client import AISearchAPIClient, AISearchAPIError

try:
    with AISearchAPIClient(api_key="your-api-key") as client:
        result = client.search(prompt="Your query")
        print(result.answer)
except AISearchAPIError as e:
    print(f"API Error [{e.status_code}]: {e.description}")
```

---

## Environment Variables

You can set your API key globally:

```bash
export AI_SEARCH_API_KEY="your-api-key-here"
```

Then use:

```python
import os
from aisearchapi_client import AISearchAPIClient

api_key = os.getenv("AI_SEARCH_API_KEY")
client = AISearchAPIClient(api_key=api_key)
```

---

## Examples

Find more examples in the [examples/ folder](examples/) or check the [documentation](https://docs.aisearchapi.io/):

- Basic search and balance checking  
- Contextual search with history  
- Async usage  
- Error handling  

---

## Requirements

- Python 3.8+
- requests >= 2.25.0
- typing-extensions >= 4.0.0 (if Python < 3.10)

---

## Development

```bash
git clone https://github.com/aisearchapi/aisearchapi-python.git
cd aisearchapi-python
python -m venv venv
source venv/bin/activate
pip install -e ".[dev,test]"
pytest
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file.

---

## Support & Links

- **Get API Key**: [AI Search API Dashboard](https://app.aisearchapi.io/dashboard)  
- **Documentation**: [docs.aisearchapi.io](https://docs.aisearchapi.io/)  
- **Homepage**: [aisearchapi.io](https://aisearchapi.io/)  
- **Issues**: [GitHub Issues](https://github.com/aisearchapi/aisearchapi-python/issues)  
- **Email**: admin@aisearchapi.io  

---

## SEO Keywords

*AI search API Python client, semantic search Python, contextual AI search, AI API key, AI dashboard, intelligent search SDK*  
