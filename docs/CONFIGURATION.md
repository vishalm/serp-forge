# Configuration Guide

## Overview

Serp Forge provides extensive configuration options for customizing search behavior, content extraction, anti-detection measures, and performance optimization.

## Basic Configuration

### Environment Variables

```bash
# Required
export SERPER_API_KEY="your_api_key_here"

# Optional
export SERP_FORGE_TIMEOUT="30"
export SERP_FORGE_MAX_RETRIES="3"
export SERP_FORGE_USER_AGENT="Custom User Agent"
```

### Configuration File

Create `serp_forge_config.yaml`:

```yaml
# API Configuration
api:
  key: "${SERPER_API_KEY}"
  timeout: 30
  max_retries: 3
  base_url: "https://google.serper.dev"

# Search Configuration
search:
  default_type: "web"
  default_max_results: 10
  default_language: "en"
  default_region: "us"

# Content Extraction
content:
  extract_content: true
  extract_metadata: true
  extract_sentiment: true
  extract_keywords: true
  extract_summary: true
  min_content_length: 100
  max_content_length: 5000
  content_quality_threshold: 0.7

# Anti-Detection
anti_detection:
  rotate_headers: true
  rotate_user_agents: true
  randomize_delays: true
  min_delay: 1
  max_delay: 3

# Proxy Configuration
proxy:
  enabled: false
  rotation_strategy: "round_robin"
  proxy_list: []
  max_retries: 3
  timeout: 30

# Performance
performance:
  max_concurrent: 5
  connection_pool_size: 10
  enable_caching: true
  cache_ttl: 3600
```

## Search Configuration

### SearchConfig Class

```python
from serp_forge import SearchConfig

config = SearchConfig(
    # Basic settings
    search_type="web",           # "web", "news", "images", "videos"
    max_results=20,              # Number of results to fetch
    language="en",               # Search language
    region="us",                 # Search region
    
    # Advanced settings
    timeout=60,                  # Request timeout in seconds
    retry_failed=True,           # Retry failed requests
    user_agent_rotation=True,    # Rotate user agents
    header_randomization=True,   # Randomize headers
    
    # Content extraction
    include_content=True,        # Extract full content
    extract_metadata=True,       # Extract metadata
    extract_sentiment=True,      # Perform sentiment analysis
    extract_keywords=True,       # Extract keywords
    extract_summary=True,        # Generate summaries
    
    # Quality filters
    min_content_length=100,      # Minimum content length
    max_content_length=5000,     # Maximum content length
    content_quality_threshold=0.7, # Quality threshold
    
    # Proxy settings
    proxy_config=None,           # ProxyConfig object
    
    # Custom parameters
    custom_params={}             # Additional search parameters
)
```

### Search Types

```python
# Web search (default)
web_config = SearchConfig(search_type="web", max_results=10)

# News search
news_config = SearchConfig(
    search_type="news",
    max_results=15,
    extract_sentiment=True,
    extract_metadata=True
)

# Image search
image_config = SearchConfig(
    search_type="images",
    max_results=20,
    custom_params={
        "image_type": "photo",
        "size": "large"
    }
)

# Video search
video_config = SearchConfig(
    search_type="videos",
    max_results=10,
    custom_params={
        "video_duration": "medium"
    }
)
```

## Content Configuration

### ContentConfig Class

```python
from serp_forge import ContentConfig

content_config = ContentConfig(
    # Extraction options
    extract_content=True,           # Extract full article content
    extract_metadata=True,          # Extract metadata (author, date, etc.)
    extract_sentiment=True,         # Perform sentiment analysis
    extract_keywords=True,          # Extract keywords
    extract_summary=True,           # Generate article summary
    
    # Content filters
    min_content_length=100,         # Minimum content length in characters
    max_content_length=5000,        # Maximum content length in characters
    content_quality_threshold=0.7,  # Quality score threshold (0-1)
    
    # Processing options
    clean_html=True,                # Clean HTML tags
    remove_ads=True,                # Remove advertisement content
    extract_images=True,            # Extract image URLs
    extract_links=True,             # Extract internal/external links
    
    # Language processing
    detect_language=True,           # Detect content language
    translate_to="en",              # Translate to specific language
    
    # AI features
    generate_summary=True,          # Generate AI summary
    extract_entities=True,          # Extract named entities
    classify_content=True,          # Classify content type
    detect_topics=True              # Detect main topics
)
```

## Proxy Configuration

### ProxyConfig Class

```python
from serp_forge import ProxyConfig

# Basic proxy configuration
proxy_config = ProxyConfig(
    enabled=True,
    proxy_list=[
        "http://proxy1:8080",
        "http://proxy2:8080",
        "http://proxy3:8080"
    ],
    rotation_strategy="round_robin",  # "round_robin", "random", "failover"
    max_retries=3,
    timeout=30
)

# Advanced proxy configuration
advanced_proxy_config = ProxyConfig(
    enabled=True,
    proxy_list=[
        "http://user:pass@proxy1:8080",
        "http://user:pass@proxy2:8080"
    ],
    rotation_strategy="random",
    max_retries=5,
    timeout=60,
    health_check=True,              # Check proxy health
    health_check_interval=300,      # Health check interval (seconds)
    failover_enabled=True,          # Enable failover to working proxies
    authentication_required=True    # Require authentication
)
```

## Anti-Detection Configuration

### AntiDetectionConfig Class

```python
from serp_forge import AntiDetectionConfig

anti_detection_config = AntiDetectionConfig(
    # Header rotation
    rotate_headers=True,
    custom_headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    
    # User agent rotation
    rotate_user_agents=True,
    user_agent_list=[
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    ],
    
    # Timing randomization
    randomize_delays=True,
    min_delay=1,                    # Minimum delay between requests
    max_delay=5,                    # Maximum delay between requests
    
    # Browser fingerprinting evasion
    spoof_browser=True,             # Spoof browser characteristics
    randomize_viewport=True,        # Randomize viewport size
    spoof_platform=True,            # Spoof platform information
    
    # Request randomization
    randomize_parameters=True,      # Randomize request parameters
    add_random_headers=True,        # Add random headers
    vary_request_patterns=True      # Vary request patterns
)
```

## Performance Configuration

### PerformanceConfig Class

```python
from serp_forge import PerformanceConfig

performance_config = PerformanceConfig(
    # Concurrency settings
    max_concurrent=10,              # Maximum concurrent requests
    connection_pool_size=20,        # Connection pool size
    max_connections_per_host=5,     # Max connections per host
    
    # Caching
    enable_caching=True,            # Enable response caching
    cache_ttl=3600,                 # Cache TTL in seconds
    cache_max_size=1000,            # Maximum cache entries
    
    # Rate limiting
    rate_limit_enabled=True,        # Enable rate limiting
    requests_per_minute=60,         # Requests per minute
    burst_limit=10,                 # Burst limit
    
    # Timeouts
    connect_timeout=10,             # Connection timeout
    read_timeout=30,                # Read timeout
    total_timeout=60,               # Total timeout
    
    # Retry settings
    max_retries=3,                  # Maximum retry attempts
    retry_backoff_factor=2,         # Exponential backoff factor
    retry_status_codes=[500, 502, 503, 504]  # Status codes to retry
)
```

## Advanced Configuration

### Custom Configuration Builder

```python
from serp_forge import SerpForge, SearchConfig, ContentConfig, ProxyConfig

class CustomSerpForge:
    def __init__(self, api_key: str):
        self.forge = SerpForge(api_key=api_key)
    
    def create_research_config(self) -> SearchConfig:
        """Configuration optimized for research."""
        return SearchConfig(
            search_type="web",
            max_results=50,
            language="en",
            region="us",
            content_config=ContentConfig(
                extract_content=True,
                extract_metadata=True,
                extract_sentiment=True,
                extract_keywords=True,
                extract_summary=True,
                min_content_length=200,
                content_quality_threshold=0.8
            ),
            timeout=120,
            retry_failed=True
        )
    
    def create_monitoring_config(self) -> SearchConfig:
        """Configuration optimized for content monitoring."""
        return SearchConfig(
            search_type="news",
            max_results=20,
            language="en",
            region="us",
            content_config=ContentConfig(
                extract_content=True,
                extract_metadata=True,
                extract_sentiment=True,
                min_content_length=100
            ),
            timeout=60,
            retry_failed=True
        )
    
    def create_bulk_config(self) -> SearchConfig:
        """Configuration optimized for bulk processing."""
        return SearchConfig(
            search_type="web",
            max_results=10,
            language="en",
            region="us",
            content_config=ContentConfig(
                extract_content=True,
                extract_metadata=True,
                min_content_length=50
            ),
            timeout=30,
            retry_failed=False  # Faster processing
        )

# Usage
custom_forge = CustomSerpForge("your_api_key")

# Research configuration
research_results = custom_forge.forge.search(
    "artificial intelligence trends",
    config=custom_forge.create_research_config()
)

# Monitoring configuration
monitoring_results = custom_forge.forge.search(
    "blockchain news",
    config=custom_forge.create_monitoring_config()
)
```

## Configuration Validation

### Validate Configuration

```python
from serp_forge import SearchConfig, validate_config

# Create configuration
config = SearchConfig(
    search_type="web",
    max_results=100,
    timeout=30
)

# Validate configuration
try:
    validate_config(config)
    print("✅ Configuration is valid")
except ValueError as e:
    print(f"❌ Configuration error: {e}")
```

### Configuration Examples

#### Research Configuration
```python
research_config = SearchConfig(
    search_type="web",
    max_results=50,
    language="en",
    region="us",
    content_config=ContentConfig(
        extract_content=True,
        extract_metadata=True,
        extract_sentiment=True,
        extract_keywords=True,
        extract_summary=True,
        min_content_length=200,
        content_quality_threshold=0.8
    ),
    timeout=120,
    retry_failed=True
)
```

#### Monitoring Configuration
```python
monitoring_config = SearchConfig(
    search_type="news",
    max_results=20,
    language="en",
    region="us",
    content_config=ContentConfig(
        extract_content=True,
        extract_metadata=True,
        extract_sentiment=True,
        min_content_length=100
    ),
    timeout=60,
    retry_failed=True
)
```

#### Bulk Processing Configuration
```python
bulk_config = SearchConfig(
    search_type="web",
    max_results=10,
    language="en",
    region="us",
    content_config=ContentConfig(
        extract_content=True,
        extract_metadata=True,
        min_content_length=50
    ),
    timeout=30,
    retry_failed=False
)
```

## Best Practices

1. **Start Simple**: Begin with basic configuration and add complexity as needed
2. **Monitor Performance**: Track execution times and success rates
3. **Use Appropriate Timeouts**: Set realistic timeouts based on your use case
4. **Implement Rate Limiting**: Respect API limits and implement delays
5. **Validate Configurations**: Always validate configurations before use
6. **Cache Results**: Enable caching for repeated queries
7. **Handle Errors**: Implement proper error handling for failed requests

## Next Steps

- [Usage Examples](USAGE.md) for practical configuration usage
- [API Reference](API.md) for complete configuration options
- [Examples](../examples/) for configuration examples 