#!/usr/bin/env python3
"""
Simple Search Example
Basic usage of Serp Forge for web scraping.
"""

import os
from dotenv import load_dotenv
import serp_forge as sf

# Load environment variables
load_dotenv()

def main():
    """Simple search example."""
    print("🔍 Simple Search Example")
    print("=" * 40)
    
    # Check if API key is set
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key or api_key == "your_serper_api_key_here":
        print("❌ Error: Please set your SERPER_API_KEY in the .env file")
        print("   Copy env.example to .env and add your API key")
        return
    
    # Simple search
    print("Searching for 'AI news 2025'...")
    results = sf.scrape("AI news 2025", max_results=3)
    
    if results.success:
        print(f"✅ Found {len(results.results)} articles")
        print(f"⏱️  Execution time: {results.execution_time:.2f}s")
        print()
        
        for i, article in enumerate(results.results, 1):
            print(f"{i}. {article.title}")
            print(f"   📰 Source: {article.source}")
            print(f"   🔗 URL: {article.url}")
            print(f"   📝 Content: {article.content[:100]}...")
            if article.sentiment:
                print(f"   😊 Sentiment: {article.sentiment}")
            print()
    else:
        print(f"❌ Search failed: {results.error_message}")

if __name__ == "__main__":
    main() 