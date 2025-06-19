# Usage Guide

## Basic Usage

### Simple Search

```python
import serp_forge as sf

# Basic web search
results = sf.scrape("artificial intelligence news", max_results=10)

if results.success:
    for article in results.results:
        print(f"Title: {article.title}")
        print(f"URL: {article.url}")
        print(f"Content: {article.content[:200]}...")
        print("---")
```

### News Search

```python
# Search for news articles
news = sf.search_news("blockchain technology", max_results=5)

for article in news.results:
    print(f"📰 {article.title}")
    print(f"📅 {article.publish_date}")
    print(f"😊 Sentiment: {article.sentiment}")
    print("---")
```

### Image Search

```python
# Search for images
images = sf.search_images("machine learning", max_results=10)

for image in images.results:
    print(f"🖼️ {image.title}")
    print(f"🔗 {image.url}")
    print(f"📏 {image.width}x{image.height}")
    print("---")
```

### Video Search

```python
# Search for videos
videos = sf.search_videos("machine learning tutorial", max_results=5)

for video in videos.results:
    print(f"Title: {video.title}")
    print(f"URL: {video.url}")
    print(f"Snippet: {video.snippet}")
```

## Advanced Usage

### Batch Processing

```python
# Process multiple queries efficiently
queries = [
    "AI trends 2025",
    "machine learning applications",
    "data science projects"
]

batch_results = sf.batch_scrape(
    queries=queries,
    search_type="web",
    max_results_per_query=5,
    parallel=True,
    save_to="results.json"
)

print(f"Processed {batch_results.total_queries} queries")
print(f"Found {batch_results.total_results} results")
```

### Async Scraping

```python
import asyncio
from serp_forge.serper import async_scrape

async def search_multiple():
    tasks = []
    queries = ["AI", "ML", "Data Science"]
    
    for query in queries:
        task = async_scrape(query, max_results=3)
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    return results

# Run async search
results = asyncio.run(search_multiple())
```

### Custom Configuration

```python
from serp_forge import SearchConfig, ContentConfig

# Create custom configuration
config = SearchConfig(
    search_type="web",
    max_results=20,
    language="en",
    region="us",
    content_config=ContentConfig(
        extract_content=True,
        extract_sentiment=True,
        extract_keywords=True,
        min_content_length=100
    )
)

# Use custom config
results = sf.scrape("quantum computing", config=config)
```

## Data Processing

### Filtering Results

```python
# Filter by content length
long_articles = [a for a in results.results if a.word_count > 500]

# Filter by sentiment
positive_articles = [a for a in results.results if a.sentiment == "positive"]

# Filter by source
tech_sources = [a for a in results.results if "tech" in a.source.lower()]
```

### Export Data

```python
import json
import csv

# Export to JSON
with open("results.json", "w") as f:
    json.dump([article.model_dump() for article in results.results], f, indent=2)

# Export to CSV
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "URL", "Source", "Sentiment", "Word Count"])
    
    for article in results.results:
        writer.writerow([
            article.title,
            article.url,
            article.source,
            article.sentiment or "",
            article.word_count
        ])
```

### Analysis

```python
# Sentiment analysis
sentiments = [a.sentiment for a in results.results if a.sentiment]
sentiment_counts = {}
for sentiment in sentiments:
    sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1

print("Sentiment distribution:", sentiment_counts)

# Source analysis
sources = [a.source for a in results.results]
source_counts = {}
for source in sources:
    source_counts[source] = source_counts.get(source, 0) + 1

print("Top sources:", dict(sorted(source_counts.items(), key=lambda x: x[1], reverse=True)[:5]))
```

## Error Handling

### Basic Error Handling

```python
try:
    results = sf.scrape("test query", max_results=10)
    
    if results.success:
        print(f"Found {len(results.results)} results")
    else:
        print(f"Search failed: {results.error_message}")
        
except Exception as e:
    print(f"Error occurred: {e}")
```

### Retry Logic

```python
import time

def search_with_retry(query, max_retries=3):
    for attempt in range(max_retries):
        try:
            results = sf.scrape(query, max_results=5)
            if results.success:
                return results
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
    
    return None
```

## Performance Optimization

### Concurrent Processing

```python
from concurrent.futures import ThreadPoolExecutor

def search_query(query):
    return sf.scrape(query, max_results=5)

queries = ["AI", "ML", "Data Science", "Python"]

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(search_query, queries))
```

### Rate Limiting

```python
import time

def rate_limited_search(queries, delay=1):
    results = []
    for query in queries:
        result = sf.scrape(query, max_results=5)
        results.append(result)
        time.sleep(delay)  # Rate limiting
    return results
```

## Real-World Examples

### Content Monitoring

```python
def monitor_topic(topic, max_results=10):
    """Monitor a topic for new content."""
    results = sf.search_news(topic, max_results=max_results)
    
    if results.success:
        print(f"📊 Monitoring: {topic}")
        print(f"📰 Found {len(results.results)} recent articles")
        
        for article in results.results:
            print(f"  • {article.title}")
            print(f"    📅 {article.publish_date}")
            print(f"    😊 {article.sentiment}")
    
    return results

# Monitor multiple topics
topics = ["artificial intelligence", "blockchain", "quantum computing"]
for topic in topics:
    monitor_topic(topic)
```

### Research Assistant

```python
def research_topic(topic, depth=3):
    """Conduct comprehensive research on a topic."""
    print(f"🔍 Researching: {topic}")
    
    # Initial search
    initial_results = sf.scrape(topic, max_results=10)
    
    if not initial_results.success:
        return []
    
    # Extract keywords for deeper search
    all_keywords = []
    for article in initial_results.results:
        if article.keywords:
            all_keywords.extend(article.keywords[:3])
    
    # Search with keywords
    keyword_results = []
    for keyword in set(all_keywords[:5]):
        results = sf.scrape(f"{topic} {keyword}", max_results=5)
        if results.success:
            keyword_results.extend(results.results)
    
    # Combine and deduplicate
    all_articles = initial_results.results + keyword_results
    unique_articles = list({article.url: article for article in all_articles}.values())
    
    print(f"📚 Found {len(unique_articles)} unique articles")
    return unique_articles

# Research example
articles = research_topic("machine learning applications")
```

## Best Practices

1. **Use appropriate search types** for your needs (web, news, images)
2. **Implement rate limiting** to avoid API limits
3. **Handle errors gracefully** with try-catch blocks
4. **Filter results** to get relevant content
5. **Use batch processing** for multiple queries
6. **Cache results** when possible to avoid repeated requests
7. **Monitor API usage** to stay within limits

## Next Steps

- [Explore Examples](../examples/) for more detailed use cases
- [Check Configuration](CONFIGURATION.md) for advanced settings
- [Review API Reference](API.md) for complete documentation 