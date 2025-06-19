#!/usr/bin/env python3
"""
Custom Configuration Example
Advanced usage with custom configuration, proxy rotation, and error handling.
"""

import os
import time
import logging
from typing import List, Dict, Any
from dotenv import load_dotenv
from serp_forge import SerpForge, SearchConfig, ProxyConfig, ContentConfig
from serp_forge.models import SearchResult, Article

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CustomSerpForge:
    """Custom Serp Forge implementation with advanced features."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.forge = SerpForge(api_key=api_key)
        self.search_history = []
        self.error_count = 0
        self.success_count = 0
    
    def create_custom_config(self, 
                           search_type: str = "web",
                           max_results: int = 10,
                           language: str = "en",
                           region: str = "us",
                           use_proxies: bool = False,
                           retry_failed: bool = True) -> SearchConfig:
        """Create custom search configuration."""
        
        # Proxy configuration
        proxy_config = None
        if use_proxies:
            proxy_config = ProxyConfig(
                enabled=True,
                rotation_strategy="round_robin",
                proxy_list=[
                    "http://proxy1:8080",
                    "http://proxy2:8080",
                    "http://proxy3:8080"
                ],
                max_retries=3,
                timeout=30
            )
        
        # Content extraction configuration
        content_config = ContentConfig(
            extract_content=True,
            extract_metadata=True,
            extract_sentiment=True,
            extract_keywords=True,
            extract_summary=True,
            min_content_length=100,
            max_content_length=5000,
            content_quality_threshold=0.7
        )
        
        # Search configuration
        search_config = SearchConfig(
            search_type=search_type,
            max_results=max_results,
            language=language,
            region=region,
            proxy_config=proxy_config,
            content_config=content_config,
            retry_failed=retry_failed,
            timeout=60,
            user_agent_rotation=True,
            header_randomization=True
        )
        
        return search_config
    
    def search_with_retry(self, 
                         query: str, 
                         config: SearchConfig,
                         max_retries: int = 3) -> SearchResult:
        """Search with automatic retry on failure."""
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Searching '{query}' (attempt {attempt + 1}/{max_retries})")
                
                start_time = time.time()
                result = self.forge.search(query, config)
                execution_time = time.time() - start_time
                
                if result.success:
                    self.success_count += 1
                    logger.info(f"✅ Search successful: {len(result.results)} results in {execution_time:.2f}s")
                    
                    # Log search history
                    self.search_history.append({
                        "query": query,
                        "timestamp": time.time(),
                        "results_count": len(result.results),
                        "execution_time": execution_time,
                        "success": True
                    })
                    
                    return result
                else:
                    self.error_count += 1
                    logger.warning(f"❌ Search failed: {result.error_message}")
                    
                    # Log failed attempt
                    self.search_history.append({
                        "query": query,
                        "timestamp": time.time(),
                        "error": result.error_message,
                        "success": False
                    })
                    
                    if attempt < max_retries - 1:
                        wait_time = 2 ** attempt  # Exponential backoff
                        logger.info(f"⏳ Retrying in {wait_time}s...")
                        time.sleep(wait_time)
                    
            except Exception as e:
                self.error_count += 1
                logger.error(f"❌ Exception during search: {str(e)}")
                
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    logger.info(f"⏳ Retrying in {wait_time}s...")
                    time.sleep(wait_time)
        
        # All retries failed
        return SearchResult(
            success=False,
            error_message=f"All {max_retries} attempts failed",
            results=[],
            execution_time=0
        )
    
    def filter_results(self, 
                      results: List[Article], 
                      min_word_count: int = 100,
                      min_quality_score: float = 0.5,
                      required_keywords: List[str] = None,
                      exclude_domains: List[str] = None) -> List[Article]:
        """Filter results based on custom criteria."""
        
        filtered = []
        
        for article in results:
            # Check word count
            if article.word_count < min_word_count:
                continue
            
            # Check quality score
            if article.quality_score and article.quality_score < min_quality_score:
                continue
            
            # Check required keywords
            if required_keywords:
                article_text = f"{article.title} {article.content}".lower()
                if not any(keyword.lower() in article_text for keyword in required_keywords):
                    continue
            
            # Check excluded domains
            if exclude_domains:
                if any(domain in article.url.lower() for domain in exclude_domains):
                    continue
            
            filtered.append(article)
        
        return filtered
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get search statistics."""
        total_searches = len(self.search_history)
        successful_searches = sum(1 for s in self.search_history if s.get("success", False))
        failed_searches = total_searches - successful_searches
        
        avg_execution_time = 0
        if successful_searches > 0:
            execution_times = [s.get("execution_time", 0) for s in self.search_history if s.get("success", False)]
            avg_execution_time = sum(execution_times) / len(execution_times)
        
        return {
            "total_searches": total_searches,
            "successful_searches": successful_searches,
            "failed_searches": failed_searches,
            "success_rate": (successful_searches / total_searches * 100) if total_searches > 0 else 0,
            "average_execution_time": avg_execution_time,
            "error_count": self.error_count,
            "success_count": self.success_count
        }

def main():
    """Custom configuration example."""
    print("⚙️  Custom Configuration Example")
    print("=" * 50)
    
    # Check if API key is set
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key or api_key == "your_serper_api_key_here":
        print("❌ Error: Please set your SERPER_API_KEY in the .env file")
        return
    
    # Initialize custom Serp Forge
    custom_forge = CustomSerpForge(api_key)
    
    # Create custom configurations for different use cases
    print("🔧 Creating custom configurations...")
    
    # Configuration 1: High-quality content extraction
    high_quality_config = custom_forge.create_custom_config(
        search_type="web",
        max_results=15,
        language="en",
        region="us",
        use_proxies=False,
        retry_failed=True
    )
    
    # Configuration 2: News search with sentiment analysis
    news_config = custom_forge.create_custom_config(
        search_type="news",
        max_results=10,
        language="en",
        region="us",
        use_proxies=False,
        retry_failed=True
    )
    
    # Define search queries
    queries = [
        "artificial intelligence breakthroughs 2025",
        "machine learning applications in healthcare",
        "quantum computing developments",
        "cybersecurity best practices",
        "sustainable technology innovations"
    ]
    
    print(f"🚀 Starting searches with custom configurations...")
    print()
    
    all_results = []
    
    # Search with high-quality configuration
    print("📊 High-Quality Content Search:")
    print("-" * 40)
    
    for query in queries[:3]:
        result = custom_forge.search_with_retry(query, high_quality_config, max_retries=2)
        
        if result.success:
            # Filter results
            filtered_results = custom_forge.filter_results(
                result.results,
                min_word_count=200,
                min_quality_score=0.6,
                required_keywords=["AI", "technology", "innovation"],
                exclude_domains=["spam.com", "low-quality.com"]
            )
            
            print(f"🔍 '{query}':")
            print(f"   📰 Found: {len(result.results)} articles")
            print(f"   ✅ Filtered: {len(filtered_results)} high-quality articles")
            
            if filtered_results:
                best_article = max(filtered_results, key=lambda x: x.quality_score or 0)
                print(f"   ⭐ Best: {best_article.title[:60]}...")
                print(f"   📊 Quality: {best_article.quality_score:.2f}")
                print(f"   📝 Words: {best_article.word_count}")
            
            all_results.extend(filtered_results)
            print()
    
    # Search with news configuration
    print("📰 News Search with Sentiment:")
    print("-" * 40)
    
    for query in queries[3:]:
        result = custom_forge.search_with_retry(query, news_config, max_retries=2)
        
        if result.success:
            print(f"🔍 '{query}':")
            print(f"   📰 Found: {len(result.results)} news articles")
            
            # Analyze sentiment distribution
            sentiments = {}
            for article in result.results:
                if article.sentiment:
                    sentiments[article.sentiment] = sentiments.get(article.sentiment, 0) + 1
            
            if sentiments:
                print(f"   😊 Sentiment: {sentiments}")
            
            # Show top article
            if result.results:
                top_article = result.results[0]
                print(f"   📰 Top: {top_article.title[:60]}...")
                print(f"   🌐 Source: {top_article.source}")
                if top_article.sentiment:
                    print(f"   😊 Sentiment: {top_article.sentiment}")
            
            all_results.extend(result.results)
            print()
    
    # Display statistics
    print("📊 Search Statistics:")
    print("=" * 50)
    
    stats = custom_forge.get_statistics()
    print(f"   Total searches: {stats['total_searches']}")
    print(f"   Successful: {stats['successful_searches']}")
    print(f"   Failed: {stats['failed_searches']}")
    print(f"   Success rate: {stats['success_rate']:.1f}%")
    print(f"   Average execution time: {stats['average_execution_time']:.2f}s")
    
    # Final results summary
    print(f"\n📋 Final Results Summary:")
    print(f"   Total articles collected: {len(all_results)}")
    
    if all_results:
        # Quality analysis
        quality_scores = [a.quality_score for a in all_results if a.quality_score]
        if quality_scores:
            avg_quality = sum(quality_scores) / len(quality_scores)
            print(f"   Average quality score: {avg_quality:.2f}")
        
        # Sentiment analysis
        sentiments = [a.sentiment for a in all_results if a.sentiment]
        if sentiments:
            sentiment_counts = {}
            for sentiment in sentiments:
                sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
            print(f"   Sentiment distribution: {sentiment_counts}")
        
        # Source analysis
        sources = [a.source for a in all_results]
        unique_sources = len(set(sources))
        print(f"   Unique sources: {unique_sources}")
        
        # Word count analysis
        word_counts = [a.word_count for a in all_results if a.word_count > 0]
        if word_counts:
            avg_words = sum(word_counts) / len(word_counts)
            print(f"   Average word count: {avg_words:.0f}")
    
    print(f"\n✅ Custom configuration example completed!")

if __name__ == "__main__":
    main() 