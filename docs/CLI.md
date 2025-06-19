# CLI Reference

## Overview

Serp Forge provides a powerful command-line interface for web scraping and search operations.

## Installation

```bash
# Install Serp Forge
pip install serp-forge

# Verify installation
serp-forge --version
```

## Basic Commands

### Search Command

```bash
# Basic search
serp-forge search "artificial intelligence"

# Search with options
serp-forge search "AI news 2025" --max-results 20 --include-content

# Search with output file
serp-forge search "machine learning" --output results.json --format json
```

#### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--max-results` | Maximum number of results | 10 |
| `--include-content` | Extract full content | False |
| `--extract-sentiment` | Perform sentiment analysis | False |
| `--extract-keywords` | Extract keywords | False |
| `--extract-summary` | Generate summaries | False |
| `--output` | Output file path | stdout |
| `--format` | Output format (json, csv) | json |
| `--timeout` | Request timeout in seconds | 60 |
| `--language` | Search language | en |
| `--region` | Search region | us |

### News Search

```bash
# News search
serp-forge news "blockchain technology"

# News with sentiment analysis
serp-forge news "cryptocurrency" --extract-sentiment --max-results 15

# News with custom output
serp-forge news "tech news" --output news.csv --format csv
```

### Image Search

```bash
# Image search
serp-forge images "machine learning"

# Image search with size filter
serp-forge images "AI art" --max-results 20 --image-size large

# Image search with type filter
serp-forge images "data visualization" --image-type photo
```

#### Image Options

| Option | Description | Default |
|--------|-------------|---------|
| `--image-size` | Image size (small, medium, large) | medium |
| `--image-type` | Image type (photo, clipart, line) | photo |
| `--image-color` | Image color (color, gray, trans) | color |

### Video Search

```bash
# Video search
serp-forge videos "Python tutorial"

# Video search with duration filter
serp-forge videos "machine learning course" --video-duration long

# Video search with quality filter
serp-forge videos "data science" --video-quality hd
```

#### Video Options

| Option | Description | Default |
|--------|-------------|---------|
| `--video-duration` | Video duration (short, medium, long) | medium |
| `--video-quality` | Video quality (sd, hd, 4k) | hd |
| `--video-type` | Video type (movie, episode, clip) | clip |

## Batch Processing

### Batch Search

```bash
# Create queries file
echo "artificial intelligence" > queries.txt
echo "machine learning" >> queries.txt
echo "data science" >> queries.txt

# Run batch search
serp-forge batch --queries queries.txt

# Batch search with parallel processing
serp-forge batch --queries queries.txt --parallel --max-results-per-query 10

# Batch search with custom output
serp-forge batch --queries queries.txt --output batch_results.json --format json
```

#### Batch Options

| Option | Description | Default |
|--------|-------------|---------|
| `--queries` | File containing queries (one per line) | Required |
| `--parallel` | Enable parallel processing | False |
| `--max-results-per-query` | Maximum results per query | 10 |
| `--output` | Output file path | stdout |
| `--format` | Output format (json, csv) | json |
| `--timeout` | Request timeout in seconds | 60 |

### Interactive Batch Mode

```bash
# Start interactive batch mode
serp-forge batch --interactive

# This will prompt for queries and options
```

## Configuration Management

### Show Configuration

```bash
# Show current configuration
serp-forge config --show

# Show configuration in specific format
serp-forge config --show --format yaml
```

### Load Configuration

```bash
# Load configuration from file
serp-forge config --load config.yaml

# Load configuration and validate
serp-forge config --load config.yaml --validate
```

### Save Configuration

```bash
# Save current configuration
serp-forge config --save my_config.yaml

# Save configuration in specific format
serp-forge config --save my_config.json --format json
```

### Validate Configuration

```bash
# Validate configuration file
serp-forge config --validate config.yaml

# Validate and show errors
serp-forge config --validate config.yaml --verbose
```

## Output Formats

### JSON Output

```bash
# Save to JSON file
serp-forge search "AI news" --output results.json --format json
```

Example JSON output:
```json
{
  "success": true,
  "query": "AI news",
  "total_results": 10,
  "scraped_successfully": 8,
  "execution_time": 2.34,
  "results": [
    {
      "title": "Article Title",
      "url": "https://example.com/article",
      "source": "example.com",
      "content": "Article content...",
      "author": "John Doe",
      "publish_date": "2025-01-15T10:30:00Z",
      "sentiment": "positive",
      "sentiment_score": 0.8,
      "keywords": ["AI", "technology", "news"],
      "word_count": 500,
      "reading_time": 2
    }
  ]
}
```

### CSV Output

```bash
# Save to CSV file
serp-forge search "AI news" --output results.csv --format csv
```

Example CSV output:
```csv
Title,URL,Source,Content,Author,Publish Date,Sentiment,Sentiment Score,Keywords,Word Count,Reading Time
Article Title,https://example.com/article,example.com,Article content...,John Doe,2025-01-15,positive,0.8,"AI,technology,news",500,2
```

## Advanced Options

### Proxy Configuration

```bash
# Use proxy list
serp-forge search "query" --proxy-list proxy1:8080,proxy2:8080

# Use proxy with authentication
serp-forge search "query" --proxy-user user --proxy-pass password

# Enable proxy rotation
serp-forge search "query" --proxy-rotation round_robin
```

### Anti-Detection

```bash
# Enable user agent rotation
serp-forge search "query" --rotate-user-agents

# Enable header randomization
serp-forge search "query" --randomize-headers

# Add random delays
serp-forge search "query" --random-delays 1-5
```

### Content Extraction

```bash
# Extract full content
serp-forge search "query" --include-content

# Set content length limits
serp-forge search "query" --min-content-length 100 --max-content-length 5000

# Set quality threshold
serp-forge search "query" --content-quality-threshold 0.7
```

## Examples

### Basic Usage Examples

```bash
# Simple search
serp-forge search "artificial intelligence"

# News search with sentiment
serp-forge news "blockchain" --extract-sentiment --max-results 15

# Image search
serp-forge images "machine learning" --max-results 20 --image-size large

# Video search
serp-forge videos "Python tutorial" --video-duration long
```

### Advanced Usage Examples

```bash
# Batch processing with parallel execution
serp-forge batch --queries queries.txt --parallel --max-results-per-query 10 --output results.json

# Search with custom configuration
serp-forge search "AI news" \
  --max-results 20 \
  --include-content \
  --extract-sentiment \
  --extract-keywords \
  --min-content-length 200 \
  --output ai_news.json \
  --format json

# News monitoring
serp-forge news "cryptocurrency" \
  --extract-sentiment \
  --max-results 10 \
  --output crypto_news.csv \
  --format csv
```

### Configuration Examples

```bash
# Show current configuration
serp-forge config --show

# Load custom configuration
serp-forge config --load my_config.yaml

# Save configuration
serp-forge config --save config.yaml

# Validate configuration
serp-forge config --validate config.yaml
```

## Environment Variables

### Required

```bash
# Set API key
export SERPER_API_KEY="your_api_key_here"
```

### Optional

```bash
# Set timeout
export SERP_FORGE_TIMEOUT="30"

# Set max retries
export SERP_FORGE_MAX_RETRIES="3"

# Set default language
export SERP_FORGE_LANGUAGE="en"

# Set default region
export SERP_FORGE_REGION="us"
```

## Error Handling

### Common Errors

#### API Key Error
```bash
❌ Error: SERPER_API_KEY not found
```
**Solution:** Set the environment variable
```bash
export SERPER_API_KEY="your_api_key_here"
```

#### Rate Limit Error
```bash
❌ Error: Rate limit exceeded
```
**Solution:** Add delays or use proxy rotation
```bash
serp-forge search "query" --random-delays 2-5
```

#### Network Error
```bash
❌ Error: Network connection failed
```
**Solution:** Check internet connection or use proxy
```bash
serp-forge search "query" --proxy-list proxy1:8080
```

### Debug Mode

```bash
# Enable debug mode
serp-forge search "query" --debug

# Show verbose output
serp-forge search "query" --verbose
```

## Performance Tips

### Optimize for Speed

```bash
# Use parallel processing for batch operations
serp-forge batch --queries queries.txt --parallel

# Reduce content extraction for faster results
serp-forge search "query" --max-results 5 --no-content

# Use shorter timeouts
serp-forge search "query" --timeout 30
```

### Optimize for Quality

```bash
# Extract full content with metadata
serp-forge search "query" --include-content --extract-metadata

# Perform sentiment analysis
serp-forge search "query" --extract-sentiment --extract-keywords

# Set higher quality thresholds
serp-forge search "query" --content-quality-threshold 0.8
```

## Integration Examples

### Shell Script Integration

```bash
#!/bin/bash

# Search and save results
serp-forge search "AI news" --output ai_news.json --format json

# Process results with jq
cat ai_news.json | jq '.results[].title'

# Batch process multiple queries
for query in "AI" "ML" "Data Science"; do
    serp-forge search "$query" --output "${query}_results.json"
done
```

### Python Integration

```python
import subprocess
import json

# Run CLI command from Python
result = subprocess.run([
    "serp-forge", "search", "AI news",
    "--output", "results.json",
    "--format", "json"
], capture_output=True, text=True)

# Load results
with open("results.json") as f:
    data = json.load(f)
```

## Help and Support

### Get Help

```bash
# General help
serp-forge --help

# Command-specific help
serp-forge search --help
serp-forge news --help
serp-forge batch --help
serp-forge config --help
```

### Version Information

```bash
# Show version
serp-forge --version

# Show detailed version info
serp-forge --version --verbose
```

## Next Steps

- [Usage Guide](USAGE.md) for Python examples
- [Configuration Guide](CONFIGURATION.md) for advanced settings
- [API Reference](API.md) for programmatic usage
- [Examples](../examples/) for complete code examples 