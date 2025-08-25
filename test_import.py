import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from aisearchapi import AISearchAPIClient, ChatMessage
    print("✅ Import successful!")
    
    # Quick test
    client = AISearchAPIClient(api_key='test')
    print("✅ Client created successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
