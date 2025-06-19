#!/usr/bin/env python3
"""
Batch Processing Example
Process multiple queries efficiently with parallel execution.
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
import serp_forge as sf

# Load environment variables
load_dotenv()

def main():
    """Batch processing example."""
    print("📚 Batch Processing Example")
    print("=" * 40)
    
    # Check if API key is set
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key or api_key == "your_serper_api_key_here":
        print("❌ Error: Please set your SERPER_API_KEY in the .env file")
        return
    
    # Define queries for different topics
    queries = [
        "Python programming tutorials",
        "Data science projects",
        "Machine learning algorithms",
        "Web development frameworks",
        "Cloud computing services"
    ]
    
    print(f"🚀 Processing {len(queries)} queries in parallel...")
    print("Queries:", ", ".join(queries))
    print()
    
    # Process queries in batch
    batch_results = sf.batch_scrape(
        queries=queries,
        search_type="web",
        max_results_per_query=3,
        parallel=True,
        save_to="batch_results.json"
    )
    
    if batch_results.success:
        print("✅ Batch processing completed!")
        print(f"📊 Statistics:")
        print(f"   Total queries: {batch_results.total_queries}")
        print(f"   Successful: {batch_results.successful_queries}")
        print(f"   Failed: {batch_results.failed_queries}")
        print(f"   Total results: {batch_results.total_results}")
        print(f"   Total scraped: {batch_results.total_scraped}")
        print(f"   ⏱️  Execution time: {batch_results.total_execution_time:.2f}s")
        print()
        
        # Show results by query
        print("📋 Results by Query:")
        print("-" * 50)
        
        for query, query_result in batch_results.results_by_query.items():
            if query_result.success:
                print(f"\n🔍 '{query}':")
                print(f"   ✅ {len(query_result.results)} results scraped")
                
                # Show first result
                if query_result.results:
                    first_result = query_result.results[0]
                    print(f"   📰 Top result: {first_result.title}")
                    print(f"   🌐 Source: {first_result.source}")
                    if first_result.sentiment:
                        print(f"   😊 Sentiment: {first_result.sentiment}")
            else:
                print(f"\n🔍 '{query}':")
                print(f"   ❌ Failed: {query_result.error_message}")
        
        # Save detailed results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        detailed_file = f"detailed_results_{timestamp}.json"
        
        with open(detailed_file, 'w') as f:
            json.dump(batch_results.model_dump(), f, indent=2, default=str)
        
        print(f"\n💾 Detailed results saved to: {detailed_file}")
        
    else:
        print(f"❌ Batch processing failed: {batch_results.error_message}")

if __name__ == "__main__":
    main() 