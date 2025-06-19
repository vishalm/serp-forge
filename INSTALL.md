# Installation Guide

This guide will help you install and set up Serp Forge on your system.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)
- Serper API key ([Get one here](https://serper.dev))

## Quick Installation

### Using pip (Recommended)

```bash
pip install serp-forge
```

### From Source

```bash
# Clone the repository
git clone https://github.com/vishalm/serp-forge.git
cd serp-forge

# Install in development mode
pip install -e .
```

## Environment Setup

### 1. Set Environment Variables

```bash
# Required: Serper API key
export SERPER_API_KEY="your_api_key_here"

# Optional: Proxy configuration
export SERP_FORGE_PROXY_LIST="proxy1:port,proxy2:port,proxy3:port"

# Optional: Custom user agents file
export SERP_FORGE_USER_AGENTS="custom_agents.txt"
```

### 2. Verify Installation

```bash
# Test basic functionality
python -c "import serp_forge; print('✅ Serp Forge installed successfully!')"
```

## Configuration

The application uses a YAML configuration file. A default configuration is provided in `serp_forge_config.yaml`.

### Basic Configuration

```bash
# Edit the configuration file
nano serp_forge_config.yaml
```

### Using CLI Configuration

```bash
# Show current configuration
serp-forge config show

# Update configuration
serp-forge config update --key scraping.max_concurrent --value 15
```

## Usage Examples

### Basic Usage

```python
from serp_forge.serper import scrape

# Simple search
results = scrape("artificial intelligence news")

# Advanced search with options
results = scrape(
    "blockchain technology",
    search_type="news",
    max_results=20,
    include_content=True
)
```

### CLI Usage

```bash
# Basic search
serp-forge "artificial intelligence news"

# News search with content extraction
serp-forge "blockchain technology" --search-type news --max-results 20 --include-content

# Batch processing
serp-forge batch --queries queries.txt --max-results-per-query 5

# Save results to file
serp-forge "climate change" --save-to results.json --format json
```

### Advanced Usage

```python
from serp_forge.serper import batch_scrape
from serp_forge.config import Config

# Batch processing
queries = ["AI trends", "ML news", "tech updates"]
results = batch_scrape(queries, max_results_per_query=10)

# Custom configuration
config = Config()
config.scraping.max_concurrent = 10
config.content_extraction.sentiment_analysis = True
```

## Development Setup

### Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=serp_forge

# Run specific test file
pytest tests/test_serper.py
```

### Code Quality

```bash
# Format code
black serp_forge/

# Sort imports
isort serp_forge/

# Type checking
mypy serp_forge/
```

## Docker Installation

### Build Docker Image

```bash
docker build -t serp-forge .
```

### Run with Docker

```bash
# Basic usage
docker run -e SERPER_API_KEY=your_key serp-forge "test query"

# With custom configuration
docker run -v $(pwd)/serp_forge_config.yaml:/app/serp_forge_config.yaml \
    -e SERPER_API_KEY=your_key \
    serp-forge "test query"
```

## Troubleshooting

### Common Issues

#### 1. Import Error
```
ModuleNotFoundError: No module named 'serp_forge'
```

**Solution:** Ensure the package is installed correctly:
```bash
pip install serp-forge
# or for development
pip install -e .
```

#### 2. API Key Error
```
Error: SERPER_API_KEY not found
```

**Solution:** Set the environment variable:
```bash
export SERPER_API_KEY="your_api_key_here"
```

#### 3. Network Issues
```
ConnectionError: Failed to connect
```

**Solution:** Check your internet connection and proxy settings.

### Performance Optimization

#### Proxy Configuration
```bash
# Set proxy list
export SERP_FORGE_PROXY_LIST=user:pass@proxy.company.com:8080

# Enable proxy rotation in config
proxy:
  enabled: true
  rotation_strategy: "round_robin"
```

#### Rate Limiting
```bash
# Adjust rate limits in config
serper:
  max_requests_per_minute: 30
```

## Support

- **Documentation**: [https://serp-forge.readthedocs.io](https://serp-forge.readthedocs.io)
- **Issues**: [https://github.com/vishalm/serp-forge/issues](https://github.com/vishalm/serp-forge/issues)
- **Discord**: [https://discord.gg/serp-forge](https://discord.gg/serp-forge) 