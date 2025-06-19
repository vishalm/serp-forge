# Installation Guide

## Prerequisites

- Python 3.8 or higher
- Serper API key ([Get one here](https://serper.dev/))

## Quick Installation

### Using pip

```bash
pip install serp-forge
```

### Using conda

```bash
conda install -c conda-forge serp-forge
```

### From source

```bash
git clone https://github.com/vishalm/serp-forge.git
cd serp-forge
pip install -e .
```

## Environment Setup

### 1. Get Serper API Key

1. Visit [Serper.dev](https://serper.dev/)
2. Sign up for an account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key for use

### 2. Set Environment Variable

#### Option A: Environment Variable
```bash
export SERPER_API_KEY="your_api_key_here"
```

#### Option B: .env File
```bash
# Create .env file
echo "SERPER_API_KEY=your_api_key_here" > .env
```

#### Option C: Python Code
```python
import os
os.environ["SERPER_API_KEY"] = "your_api_key_here"
```

## Verification

Test your installation:

```python
import serp_forge as sf

# Test basic functionality
results = sf.scrape("test query", max_results=1)
print("✅ Installation successful!" if results.success else "❌ Installation failed")
```

## Dependencies

### Required
- `requests` - HTTP library
- `beautifulsoup4` - HTML parsing
- `pydantic` - Data validation
- `python-dotenv` - Environment management

### Optional
- `aiohttp` - Async HTTP (for async features)
- `pandas` - Data analysis
- `streamlit` - Dashboard interface

## Troubleshooting

### Common Issues

#### 1. Import Error
```
ModuleNotFoundError: No module named 'serp_forge'
```
**Solution:** Ensure you're in the correct Python environment and reinstall:
```bash
pip install --upgrade serp-forge
```

#### 2. API Key Error
```
❌ Error: SERPER_API_KEY not found
```
**Solution:** Verify your API key is set correctly:
```bash
echo $SERPER_API_KEY
```

#### 3. Permission Error
```
PermissionError: [Errno 13] Permission denied
```
**Solution:** Use virtual environment or install with `--user`:
```bash
pip install --user serp-forge
```

### Virtual Environment Setup

```bash
# Create virtual environment
python -m venv serp-forge-env

# Activate (Windows)
serp-forge-env\Scripts\activate

# Activate (macOS/Linux)
source serp-forge-env/bin/activate

# Install package
pip install serp-forge
```

## Development Installation

For contributors:

```bash
git clone https://github.com/vishalm/serp-forge.git
cd serp-forge

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## Next Steps

After installation:

1. [Read the Usage Guide](USAGE.md)
2. [Explore Examples](../examples/)
3. [Check Configuration Options](CONFIGURATION.md)
4. [Review API Reference](API.md) 