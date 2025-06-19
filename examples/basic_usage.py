#!/usr/bin/env python3
"""
Basic usage examples for Serp Forge.
"""

import asyncio
import json
from pathlib import Path

from serp_forge import scrape, batch_scrape, search_news, search_images, search_videos
from serp_forge.config import Config


def basic_search_example():
    """Basic search and scrape example."""
    print("=== Basic Search Example ===")
    
    # Simple search
    result = scrape("AI news 2025", max_results=5)
    
    if result.success:
        print(f"Found {len(result.results)} articles")
        for i, article in enumerate(result.results, 1):
            print(f"\n{i}. {article.title}")
            print(f"   URL: {article.url}")
            print(f"   Source: {article.source}")
            print(f"   Content: {article.content[:100]}...")
            if article.sentiment:
                print(f"   Sentiment: {article.sentiment}")
    else:
        print(f"Search failed: {result.error_message}")


def news_search_example():
    """News search example."""
    print("\n=== News Search Example ===")
    
    result = search_news("blockchain technology", max_results=3, include_content=True)
    
    if result.success:
        print(f"Found {len(result.results)} news articles")
        for article in result.results:
            print(f"\n- {article.title}")
            print(f"  Published: {article.publish_date}")
            print(f"  Author: {article.author}")
            print(f"  Summary: {article.summary[:150]}..." if article.summary else "No summary")
    else:
        print(f"News search failed: {result.error_message}")


def image_search_example():
    """Image search example."""
    print("\n=== Image Search Example ===")
    
    result = search_images("artificial intelligence", max_results=5)
    
    if result.success:
        print(f"Found {len(result.results)} images")
        for image in result.results:
            print(f"\n- {image.title}")
            print(f"  URL: {image.url}")
            if image.image_url:
                print(f"  Image: {image.image_url}")
    else:
        print(f"Image search failed: {result.error_message}")


def video_search_example():
    """Video search example."""
    print("\n=== Video Search Example ===")
    
    result = search_videos("machine learning tutorial", max_results=3)
    
    if result.success:
        print(f"Found {len(result.results)} videos")
        for video in result.results:
            print(f"\n- {video.title}")
            print(f"  URL: {video.url}")
            print(f"  Snippet: {video.snippet}")
    else:
        print(f"Video search failed: {result.error_message}")


def batch_processing_example():
    """Batch processing example."""
    print("\n=== Batch Processing Example ===")
    
    queries = [
        "Python programming",
        "Data science trends",
        "Web development 2025"
    ]
    
    result = batch_scrape(
        queries=queries,
        search_type="web",
        max_results_per_query=3,
        parallel=True,
        save_to="batch_results.json"
    )
    
    if result.success:
        print(f"Batch processing completed:")
        print(f"  Total queries: {result.total_queries}")
        print(f"  Successful: {result.successful_queries}")
        print(f"  Failed: {result.failed_queries}")
        print(f"  Total results: {result.total_results}")
        print(f"  Total scraped: {result.total_scraped}")
        print(f"  Execution time: {result.total_execution_time:.2f}s")
        
        # Show results for each query
        for query, query_result in result.results_by_query.items():
            print(f"\nQuery: {query}")
            print(f"  Results: {len(query_result.results)}")
            for article in query_result.results[:2]:  # Show first 2 results
                print(f"    - {article.title}")
    else:
        print(f"Batch processing failed: {result.error_message}")


def configuration_example():
    """Configuration management example."""
    print("\n=== Configuration Example ===")
    
    # Load configuration from file
    config = Config.load_from_file("serp_forge_config.yaml")
    
    # Show current configuration
    print("Current Configuration:")
    config_dict = config.to_dict()
    print(json.dumps(config_dict, indent=2, default=str))
    
    # Update configuration
    config.scraping.max_concurrent = 10
    config.content_extraction.sentiment_analysis = True
    
    # Save updated configuration
    config.save_to_file("updated_config.yaml")
    print("\nUpdated configuration saved to updated_config.yaml")


def save_results_example():
    """Example of saving results to different formats."""
    print("\n=== Save Results Example ===")
    
    # Perform search
    result = scrape("climate change research", max_results=3, include_content=True)
    
    if result.success:
        # Save as JSON
        with open("results.json", "w") as f:
            json.dump(result.model_dump(), f, indent=2, default=str)
        print("Results saved to results.json")
        
        # Save as CSV
        import csv
        with open("results.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "URL", "Source", "Content", "Author", "Sentiment"])
            for article in result.results:
                writer.writerow([
                    article.title,
                    article.url,
                    article.source,
                    article.content[:200] + "..." if len(article.content) > 200 else article.content,
                    article.author or "",
                    article.sentiment or ""
                ])
        print("Results saved to results.csv")
    else:
        print(f"Search failed: {result.error_message}")


async def async_example():
    """Async scraping example."""
    print("\n=== Async Scraping Example ===")
    
    from serp_forge.serper import async_scrape
    
    # Async search
    result = await async_scrape("quantum computing", max_results=3, include_content=True)
    
    if result.success:
        print(f"Async search completed: {len(result.results)} results")
        for article in result.results:
            print(f"\n- {article.title}")
            print(f"  Response time: {article.response_time:.2f}s")
            print(f"  Word count: {article.word_count}")
    else:
        print(f"Async search failed: {result.error_message}")


def main():
    """Run all examples."""
    print("Serp Forge - Basic Usage Examples")
    print("=" * 50)
    
    # Check if API key is set
    config = Config()
    if not config.serper.api_key or config.serper.api_key == "${SERPER_API_KEY}":
        print("⚠️  Warning: SERPER_API_KEY not set!")
        print("Please set your Serper API key in the environment or config file.")
        print("Examples will run but may fail without a valid API key.")
        print()
    
    try:
        # Run examples
        basic_search_example()
        news_search_example()
        image_search_example()
        video_search_example()
        batch_processing_example()
        configuration_example()
        save_results_example()
        
        # Run async example
        asyncio.run(async_example())
        
    except Exception as e:
        print(f"Error running examples: {e}")
        print("Make sure you have set up your Serper API key correctly.")


if __name__ == "__main__":
    main() 