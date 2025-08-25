"""
Basic usage examples for the AI Search API Python client.

Make sure to set your API key in the environment variable AI_SEARCH_API_KEY
or replace the api_key parameter with your actual API key.
"""

import os
import asyncio
from aisearchapi import AISearchAPIClient, ChatMessage, AISearchAPIError


def main():
    """Run basic usage examples"""
    
    # Initialize client with your API key
    api_key = 'as-dev-cf095c8ceba157637313709fe9dce4e9'
    
    # Use context manager to automatically close the session
    with AISearchAPIClient(api_key=api_key) as client:
        
        try:
            # Example 1: Basic search
            print('🔍 Performing basic search...')
            basic_result = client.search(
                prompt='What is machine learning and how does it work?',
                response_type='markdown'
            )
            
            print('Answer:', basic_result.answer)
            print('Sources:', basic_result.sources)
            print(f'Processing time: {basic_result.total_time}ms\n')
            
            # Example 2: Search with context
            print('🎯 Performing contextual search...')
            contextual_result = client.search(
                prompt='What are the main advantages and disadvantages?',
                context=[
                    ChatMessage(role='user', content='I am researching solar energy for my home'),
                    ChatMessage(role='user', content='I live in a sunny climate with high electricity costs')
                ],
                response_type='text'
            )
            
            print('Contextual Answer:', contextual_result.answer)
            print('Sources:', contextual_result.sources)
            print(f'Processing time: {contextual_result.total_time}ms\n')
            
            # Example 3: Check account balance
            print('💰 Checking account balance...')
            balance = client.balance()
            print(f'Available credits: {balance.available_credits}')
            
            if balance.available_credits < 10:
                print('⚠️ Warning: Low credit balance!')
            
        except AISearchAPIError as error:
            print(f'❌ API Error [{error.status_code if error.status_code else "N/A"}]: {error.description}')
            if error.response:
                print('Response data:', error.response)
        except Exception as error:
            print(f'❌ Unexpected error: {error}')


async def async_example():
    """
    Example showing how to use the client in async context.
    
    Note: The current client is synchronous, but this shows how you might
    structure code for async usage if needed.
    """
    api_key = os.getenv('AI_SEARCH_API_KEY', 'as-dev-your-api-key-here')
    
    # For async usage, you'd want to run the sync client in a thread pool
    import concurrent.futures
    import asyncio
    
    def sync_search():
        with AISearchAPIClient(api_key=api_key) as client:
            return client.search(prompt='What is Python programming?')
    
    # Run sync client in thread pool to avoid blocking
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, sync_search)
        print('Async result:', result.answer[:100] + '...')


def error_handling_example():
    """Example showing various error handling scenarios"""
    
    print('\n📚 Error handling examples...')
    
    # Example 1: Invalid API key
    try:
        client = AISearchAPIClient(api_key='invalid-key')
        client.search(prompt='test')
    except AISearchAPIError as e:
        print(f'Invalid API key error: {e}')
    
    # Example 2: Invalid parameters
    try:
        api_key = os.getenv('AI_SEARCH_API_KEY', 'as-dev-your-api-key-here')
        with AISearchAPIClient(api_key=api_key) as client:
            # This will raise ValueError due to empty prompt
            client.search(prompt='')
    except ValueError as e:
        print(f'Validation error: {e}')
    
    # Example 3: Invalid response type
    try:
        api_key = os.getenv('AI_SEARCH_API_KEY', 'as-dev-your-api-key-here')
        with AISearchAPIClient(api_key=api_key) as client:
            client.search(prompt='test', response_type='invalid')  # type: ignore
    except ValueError as e:
        print(f'Invalid response type error: {e}')

if __name__ == '__main__':
    # Run basic examples
    main()
    
    # Run error handling examples
    error_handling_example()
    
    # Run async example (commented out as it requires event loop)
    # asyncio.run(async_example())
    
    print('\n✨ All examples completed!')