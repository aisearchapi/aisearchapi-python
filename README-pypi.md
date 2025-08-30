# AI Search API Python Client

[![PyPI version](https://badge.fury.io/py/aisearchapi-client.svg)](https://badge.fury.io/py/aisearchapi-client)
[![Python Support](https://img.shields.io/pypi/pyversions/aisearchapi-client.svg)](https://pypi.org/project/aisearchapi-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **Python client library for the [AI Search API](https://aisearchapi.io?utm_source=pypi)** that provides **semantic search, contextual awareness, and intelligent AI-powered results**.  
This package makes it easy for developers to integrate the [AI Search API](https://docs.aisearchapi.io/) into Python projects.

👉 To start, get your **free API key** from the [AI Search API dashboard](https://app.aisearchapi.io/dashboard).

---

## Features

- **🔍 AI-Powered Semantic Search**: Natural language search powered by embeddings  
- **🎯 Context Awareness**: Include history for smarter results  
- **⚡ Simple API Client**: Clean Python interface with error handling  
- **🛡️ Type Safety**: Strong type hints  
- **🔄 Flexible Output**: Get text or markdown results  
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

1. Sign up at [aisearchapi.io](https://aisearchapi.io?utm_source=pypi).  
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

```bash
export AI_SEARCH_API_KEY="your-api-key-here"
```

Then use in Python:

```python
import os
from aisearchapi_client import AISearchAPIClient

api_key = os.getenv("AI_SEARCH_API_KEY")
client = AISearchAPIClient(api_key=api_key)
```

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

MIT License - see the [LICENSE](https://github.com/aisearchapi/aisearchapi-python/blob/main/LICENSE) file.

---

## Support

- **Get API Key**: [AI Search API Dashboard](https://app.aisearchapi.io/dashboard)  
- **Documentation**: [docs.aisearchapi.io](https://docs.aisearchapi.io/)  
- **Homepage**: [aisearchapi.io](https://aisearchapi.io?utm_source=pypi)  
- **Issues**: [GitHub Issues](https://github.com/aisearchapi/aisearchapi-python/issues)  
