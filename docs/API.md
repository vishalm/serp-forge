# API Reference

## Core Classes

### SerpForge

Main class for interacting with Serp Forge.

```python
from serp_forge import SerpForge

forge = SerpForge(api_key="your_api_key")
```

#### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | `str` | Required | Serper API key |
| `config` | `SearchConfig` | `None` | Default search configuration |

#### Methods

##### `search(query: str, config: SearchConfig = None) -> SearchResult`

Perform a search with the given query and configuration.

**Parameters:**
- `query` (str): Search query
- `config` (SearchConfig, optional): Search configuration

**Returns:**
- `SearchResult`: Search results object

**Example:**
```python
results = forge.search("artificial intelligence", config=search_config)
```

##### `scrape(query: str, **kwargs) -> SearchResult`

Convenience method for web scraping with default configuration.

**Parameters:**
- `query` (str): Search query
- `**kwargs`: Configuration parameters

**Returns:**
- `SearchResult`: Search results object

**Example:**
```python
results = forge.scrape("AI news", max_results=10, include_content=True)
```

### SearchConfig

Configuration class for search parameters.

```python
from serp_forge import SearchConfig

config = SearchConfig(
    search_type="web",
    max_results=10,
    language="en",
    region="us"
)
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `search_type` | `str` | `"web"` | Search type: "web", "news", "images", "videos" |
| `max_results` | `int` | `10` | Maximum number of results |
| `language` | `str` | `"en"` | Search language |
| `region` | `str` | `"us"` | Search region |
| `timeout` | `int` | `60` | Request timeout in seconds |
| `retry_failed` | `bool` | `True` | Retry failed requests |
| `user_agent_rotation` | `bool` | `True` | Rotate user agents |
| `header_randomization` | `bool` | `True` | Randomize headers |
| `include_content` | `bool` | `False` | Extract full content |
| `extract_metadata` | `bool` | `False` | Extract metadata |
| `extract_sentiment` | `bool` | `False` | Perform sentiment analysis |
| `extract_keywords` | `bool` | `False` | Extract keywords |
| `extract_summary` | `bool` | `False` | Generate summaries |
| `min_content_length` | `int` | `100` | Minimum content length |
| `max_content_length` | `int` | `5000` | Maximum content length |
| `content_quality_threshold` | `float` | `0.7` | Quality threshold (0-1) |
| `proxy_config` | `ProxyConfig` | `None` | Proxy configuration |
| `custom_params` | `dict` | `{}` | Additional search parameters |

### ContentConfig

Configuration for content extraction settings.

```python
from serp_forge import ContentConfig

content_config = ContentConfig(
    extract_content=True,
    extract_metadata=True,
    extract_sentiment=True
)
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `extract_content` | `bool` | `True` | Extract full article content |
| `extract_metadata` | `bool` | `True` | Extract metadata (author, date, etc.) |
| `extract_sentiment` | `bool` | `False` | Perform sentiment analysis |
| `extract_keywords` | `bool` | `False` | Extract keywords |
| `extract_summary` | `bool` | `False` | Generate article summary |
| `min_content_length` | `int` | `100` | Minimum content length in characters |
| `max_content_length` | `int` | `5000` | Maximum content length in characters |
| `content_quality_threshold` | `float` | `0.7` | Quality score threshold (0-1) |
| `clean_html` | `bool` | `True` | Clean HTML tags |
| `remove_ads` | `bool` | `True` | Remove advertisement content |
| `extract_images` | `bool` | `False` | Extract image URLs |
| `extract_links` | `bool` | `False` | Extract internal/external links |
| `detect_language` | `bool` | `False` | Detect content language |
| `translate_to` | `str` | `None` | Translate to specific language |
| `generate_summary` | `bool` | `False` | Generate AI summary |
| `extract_entities` | `bool` | `False` | Extract named entities |
| `classify_content` | `bool` | `False` | Classify content type |
| `detect_topics` | `bool` | `False` | Detect main topics |

### ProxyConfig

Configuration for proxy settings.

```python
from serp_forge import ProxyConfig

proxy_config = ProxyConfig(
    enabled=True,
    proxy_list=["http://proxy1:8080", "http://proxy2:8080"],
    rotation_strategy="round_robin"
)
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `enabled` | `bool` | `False` | Enable proxy usage |
| `proxy_list` | `List[str]` | `[]` | List of proxy URLs |
| `rotation_strategy` | `str` | `"round_robin"` | Rotation strategy: "round_robin", "random", "failover" |
| `max_retries` | `int` | `3` | Maximum retry attempts |
| `timeout` | `int` | `30` | Proxy timeout in seconds |
| `health_check` | `bool` | `False` | Check proxy health |
| `health_check_interval` | `int` | `300` | Health check interval in seconds |
| `failover_enabled` | `bool` | `True` | Enable failover to working proxies |
| `authentication_required` | `bool` | `False` | Require authentication |

## Data Models

### SearchResult

Result object returned by search operations.

```python
class SearchResult:
    success: bool                    # Whether the search was successful
    query: str                       # Original search query
    total_results: int               # Total number of results found
    scraped_successfully: int        # Number of results successfully scraped
    execution_time: float            # Execution time in seconds
    results: List[Article]           # List of article objects
    error_message: Optional[str]     # Error message if failed
    metadata: Dict[str, Any]         # Additional metadata
```

### Article

Individual article/result object.

```python
class Article:
    title: str                       # Article title
    url: str                         # Article URL
    source: str                      # Source domain
    content: Optional[str]           # Article content
    author: Optional[str]            # Article author
    publish_date: Optional[datetime] # Publication date
    sentiment: Optional[str]         # Sentiment: "positive", "negative", "neutral"
    sentiment_score: Optional[float] # Sentiment score (-1 to 1)
    keywords: Optional[List[str]]    # Extracted keywords
    summary: Optional[str]           # Generated summary
    word_count: int                  # Word count
    reading_time: int                # Estimated reading time in minutes
    quality_score: Optional[float]   # Content quality score (0-1)
    metadata: Dict[str, Any]         # Additional metadata
```

### BatchResult

Result object for batch processing operations.

```python
class BatchResult:
    success: bool                    # Whether batch processing was successful
    total_queries: int               # Total number of queries processed
    successful_queries: int          # Number of successful queries
    failed_queries: int              # Number of failed queries
    total_results: int               # Total number of results across all queries
    total_scraped: int               # Total number of results successfully scraped
    total_execution_time: float      # Total execution time in seconds
    results_by_query: Dict[str, SearchResult]  # Results organized by query
    error_message: Optional[str]     # Error message if failed
```

## Convenience Functions

### Main Functions

#### `scrape(query: str, **kwargs) -> SearchResult`

Convenience function for web scraping.

```python
import serp_forge as sf

results = sf.scrape("AI news", max_results=10, include_content=True)
```

#### `search_news(query: str, **kwargs) -> SearchResult`

Convenience function for news search.

```python
news = sf.search_news("blockchain", max_results=5, extract_sentiment=True)
```

#### `search_images(query: str, **kwargs) -> SearchResult`

Convenience function for image search.

```python
images = sf.search_images("machine learning", max_results=20)
```

#### `search_videos(query: str, **kwargs) -> SearchResult`

Convenience function for video search.

```python
videos = sf.search_videos("tutorial", max_results=10)
```

#### `batch_scrape(queries: List[str], **kwargs) -> BatchResult`

Convenience function for batch processing.

```python
queries = ["AI trends", "ML news", "tech updates"]
batch_results = sf.batch_scrape(queries, parallel=True, max_results_per_query=5)
```

### Async Functions

#### `async_scrape(query: str, **kwargs) -> SearchResult`

Async version of scrape function.

```python
import asyncio
from serp_forge.serper import async_scrape

async def main():
    result = await async_scrape("quantum computing", max_results=10)
    return result

results = asyncio.run(main())
```

## CLI Commands

### Basic Commands

```bash
# Search and scrape
serp-forge search "query" [options]

# News search
serp-forge news "query" [options]

# Image search
serp-forge images "query" [options]

# Video search
serp-forge videos "query" [options]

# Batch processing
serp-forge batch --queries file.txt [options]
```

### Common Options

| Option | Description | Default |
|--------|-------------|---------|
| `--max-results` | Maximum number of results | 10 |
| `--include-content` | Extract full content | False |
| `--extract-sentiment` | Perform sentiment analysis | False |
| `--extract-keywords` | Extract keywords | False |
| `--output` | Output file path | stdout |
| `--format` | Output format (json, csv) | json |
| `--parallel` | Enable parallel processing | False |
| `--timeout` | Request timeout in seconds | 60 |

## Error Handling

### Common Exceptions

#### `SerpForgeError`

Base exception for Serp Forge errors.

```python
from serp_forge import SerpForgeError

try:
    results = sf.scrape("query")
except SerpForgeError as e:
    print(f"Serp Forge error: {e}")
```

#### `APIError`

Exception for API-related errors.

```python
from serp_forge import APIError

try:
    results = sf.scrape("query")
except APIError as e:
    print(f"API error: {e}")
```

#### `ConfigurationError`

Exception for configuration errors.

```python
from serp_forge import ConfigurationError

try:
    config = SearchConfig(invalid_param="value")
except ConfigurationError as e:
    print(f"Configuration error: {e}")
```

### Error Codes

| Code | Description |
|------|-------------|
| `API_KEY_MISSING` | Serper API key not provided |
| `API_KEY_INVALID` | Invalid API key |
| `RATE_LIMIT_EXCEEDED` | Rate limit exceeded |
| `QUERY_TOO_LONG` | Search query too long |
| `INVALID_SEARCH_TYPE` | Invalid search type |
| `TIMEOUT_ERROR` | Request timeout |
| `NETWORK_ERROR` | Network connection error |
| `CONTENT_EXTRACTION_FAILED` | Content extraction failed |

## Utility Functions

### Validation Functions

#### `validate_config(config: SearchConfig) -> bool`

Validate search configuration.

```python
from serp_forge import validate_config

config = SearchConfig(max_results=100)
try:
    validate_config(config)
    print("Configuration is valid")
except ValueError as e:
    print(f"Invalid configuration: {e}")
```

#### `validate_api_key(api_key: str) -> bool`

Validate API key format.

```python
from serp_forge import validate_api_key

if validate_api_key("your_api_key"):
    print("API key format is valid")
```

### Helper Functions

#### `get_supported_languages() -> List[str]`

Get list of supported languages.

```python
from serp_forge import get_supported_languages

languages = get_supported_languages()
print(f"Supported languages: {languages}")
```

#### `get_supported_regions() -> List[str]`

Get list of supported regions.

```python
from serp_forge import get_supported_regions

regions = get_supported_regions()
print(f"Supported regions: {regions}")
```

## Examples

### Basic Usage

```python
import serp_forge as sf

# Simple search
results = sf.scrape("artificial intelligence", max_results=10)

if results.success:
    for article in results.results:
        print(f"Title: {article.title}")
        print(f"URL: {article.url}")
        print("---")
```

### Advanced Usage

```python
from serp_forge import SerpForge, SearchConfig, ContentConfig

# Create custom configuration
config = SearchConfig(
    search_type="web",
    max_results=20,
    content_config=ContentConfig(
        extract_content=True,
        extract_sentiment=True,
        extract_keywords=True,
        min_content_length=200
    )
)

# Use custom configuration
forge = SerpForge("your_api_key")
results = forge.search("machine learning", config=config)
```

### Error Handling

```python
import serp_forge as sf
from serp_forge import SerpForgeError, APIError

try:
    results = sf.scrape("test query", max_results=10)
    
    if results.success:
        print(f"Found {len(results.results)} results")
    else:
        print(f"Search failed: {results.error_message}")
        
except APIError as e:
    print(f"API error: {e}")
except SerpForgeError as e:
    print(f"Serp Forge error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Next Steps

- [Usage Guide](USAGE.md) for practical examples
- [Configuration Guide](CONFIGURATION.md) for advanced settings
- [Examples](../examples/) for complete code examples 