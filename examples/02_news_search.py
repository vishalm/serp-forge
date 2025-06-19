#!/usr/bin/env python3
"""
News Search Example
Search for news articles with sentiment analysis.
"""

import os
from dotenv import load_dotenv
import serp_forge as sf

# Load environment variables
load_dotenv()

def main():
    """News search example."""
    print("📰 News Search Example")
    print("=" * 40)
    
    # Check if API key is set
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key or api_key == "your_serper_api_key_here":
        print("❌ Error: Please set your SERPER_API_KEY in the .env file")
        return
    
    # Search for news
    queries = [
        "blockchain technology",
        "artificial intelligence trends",
        "quantum computing"
    ]
    
    for query in queries:
        print(f"\n🔍 Searching for: {query}")
        print("-" * 30)
        
        news = sf.search_news(query, max_results=2, include_content=True)
        
        if news.success:
            print(f"✅ Found {len(news.results)} news articles")
            
            for article in news.results:
                print(f"\n📰 {article.title}")
                print(f"   📅 Published: {article.publish_date}")
                print(f"   👤 Author: {article.author or 'Unknown'}")
                print(f"   🌐 Source: {article.source}")
                print(f"   🔗 URL: {article.url}")
                
                if article.sentiment:
                    print(f"   😊 Sentiment: {article.sentiment} ({article.sentiment_score:.2f})")
                
                if article.keywords:
                    print(f"   🏷️  Keywords: {', '.join(article.keywords[:5])}")
                
                if article.summary:
                    print(f"   📝 Summary: {article.summary[:150]}...")
                
                print(f"   📊 Word count: {article.word_count}")
                print(f"   ⏱️  Reading time: {article.reading_time}")
        else:
            print(f"❌ Search failed: {news.error_message}")

if __name__ == "__main__":
    main() 