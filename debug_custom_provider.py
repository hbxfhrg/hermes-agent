#!/usr/bin/env python3
"""Debug script to test resolve_runtime_provider with custom provider."""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hermes_cli.runtime_provider import resolve_runtime_provider

def main():
    print("Testing resolve_runtime_provider with custom provider...")
    
    try:
        runtime = resolve_runtime_provider()
        print("\n1. resolve_runtime_provider result:")
        print(f"   Provider: {runtime.get('provider')}")
        print(f"   Base URL: {runtime.get('base_url')}")
        print(f"   API Key: {runtime.get('api_key')}")
        print(f"   Model: {runtime.get('model')}")
        print(f"   API Mode: {runtime.get('api_mode')}")
        print(f"   Source: {runtime.get('source')}")
        
        if runtime.get('provider') == 'custom':
            print("\n✅ SUCCESS: Using custom provider!")
        else:
            print(f"\n❌ FAIL: Using {runtime.get('provider')} instead of custom")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    main()