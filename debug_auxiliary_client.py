#!/usr/bin/env python3
"""Debug script to test auxiliary client provider chain."""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent.auxiliary_client import _get_provider_chain, _try_custom_endpoint

def main():
    print("Testing auxiliary client provider chain...")
    
    # Print provider chain order
    chain = _get_provider_chain()
    print("\n1. Provider chain order:")
    for i, (name, _) in enumerate(chain, 1):
        print(f"   {i}. {name}")
    
    # Test _try_custom_endpoint
    print("\n2. Testing _try_custom_endpoint...")
    try:
        client, default_model = _try_custom_endpoint()
        if client is not None:
            print(f"   ✅ SUCCESS: Found custom endpoint")
            print(f"   Default model: {default_model}")
        else:
            print(f"   ❌ FAIL: No custom endpoint found")
    except Exception as e:
        print(f"   ❌ ERROR: {e}")

if __name__ == "__main__":
    main()