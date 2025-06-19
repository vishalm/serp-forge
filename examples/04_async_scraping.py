#!/usr/bin/env python3
"""
Async Scraping Example
High-performance concurrent scraping with async/await.
"""

import os
import asyncio
import time
from dotenv import load_dotenv
from serp_forge.serper import async_scrape

# Load environment variables
load_dotenv()

async def search_topic(topic: str, max_results: int = 3):
    """Search for a specific topic asynchronously."""
    print(f"🔍 Searching for: {topic}")
    
    result = await async_scrape(
        query=topic,
        search_type="web",
        max_results=max_results,
        include_content=True
    )
    
    if result.success:
        print(f"   ✅ Found {len(result.results)} results")
        print(f"   ⏱️  Response time: {result.execution_time:.2f}s")
        
        # Show first result
        if result.results:
            first = result.results[0]
            print(f"   📰 Top result: {first.title}")
            print(f"   🌐 Source: {first.source}")
            if first.sentiment:
                print(f"   😊 Sentiment: {first.sentiment}")
        
        return result
    else:
        print(f"   ❌ Failed: {result.error_message}")
        return None

async def main():
    """Async scraping example."""
    print("⚡ Async Scraping Example")
    print("=" * 40)
    
    # Check if API key is set
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key or api_key == "your_serper_api_key_here":
        print("❌ Error: Please set your SERPER_API_KEY in the .env file")
        return
    
    # Define topics to search
    topics = [
        "artificial intelligence",
        "blockchain technology", 
        "quantum computing",
        "machine learning",
        "data science"
    ]
    
    print(f"🚀 Starting async search for {len(topics)} topics...")
    print()
    
    start_time = time.time()
    
    # Create tasks for all searches
    tasks = []
    for topic in topics:
        task = search_topic(topic, max_results=2)
        tasks.append(task)
    
    # Execute all searches concurrently
    print("⏳ Executing searches concurrently...")
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    total_time = time.time() - start_time
    
    print(f"\n📊 Summary:")
    print(f"   Total topics: {len(topics)}")
    print(f"   Successful searches: {sum(1 for r in results if r and r.success)}")
    print(f"   Failed searches: {sum(1 for r in results if not r or not r.success)}")
    print(f"   ⏱️  Total execution time: {total_time:.2f}s")
    
    # Calculate total results
    total_results = sum(len(r.results) for r in results if r and r.success)
    print(f"   📰 Total articles found: {total_results}")
    
    # Show performance comparison
    print(f"\n⚡ Performance:")
    print(f"   Sequential time (estimated): {len(topics) * 2:.1f}s")
    print(f"   Async time: {total_time:.2f}s")
    print(f"   Speedup: {len(topics) * 2 / total_time:.1f}x")

if __name__ == "__main__":
    asyncio.run(main()) 