# Serp Forge Examples 📚

This folder contains comprehensive examples demonstrating different usage patterns and complexity levels of Serp Forge.

## Setup

1. **Copy the environment file:**
   ```bash
   cp env.example .env
   ```

2. **Add your Serper API key:**
   ```bash
   # Edit .env file and replace with your actual API key
   SERPER_API_KEY=your_actual_serper_api_key_here
   ```

3. **Install dependencies:**
   ```bash
   pip install serp-forge python-dotenv
   ```

## Examples Overview

### 🟢 Simple Examples

#### `01_simple_search.py`
- **Level:** Beginner
- **Purpose:** Basic web scraping with Serp Forge
- **Features:** Simple search, result display, error handling
- **Usage:** `python 01_simple_search.py`

#### `02_news_search.py`
- **Level:** Beginner
- **Purpose:** News-specific search with sentiment analysis
- **Features:** News search, sentiment detection, metadata extraction
- **Usage:** `python 02_news_search.py`

### 🟡 Intermediate Examples

#### `03_batch_processing.py`
- **Level:** Intermediate
- **Purpose:** Process multiple queries efficiently
- **Features:** Batch processing, parallel execution, result aggregation
- **Usage:** `python 03_batch_processing.py`

#### `04_async_scraping.py`
- **Level:** Intermediate
- **Purpose:** High-performance concurrent scraping
- **Features:** Async/await, concurrent execution, performance metrics
- **Usage:** `python 04_async_scraping.py`

### 🔴 Advanced Examples

#### `05_advanced_analysis.py`
- **Level:** Advanced
- **Purpose:** Complex data analysis and reporting
- **Features:** Content analysis, sentiment distribution, quality metrics, CSV export
- **Usage:** `python 05_advanced_analysis.py`

#### `06_custom_config.py`
- **Level:** Advanced
- **Purpose:** Custom configuration and advanced features
- **Features:** Custom configs, proxy rotation, retry logic, result filtering
- **Usage:** `python 06_custom_config.py`

## Example Outputs

Each example generates different types of output:

- **Console output:** Real-time progress and results
- **JSON files:** Detailed results and analysis reports
- **CSV files:** Structured data for further analysis
- **Logs:** Execution details and error information

## Customization

Feel free to modify the examples:

1. **Change queries:** Update the search terms in each example
2. **Adjust parameters:** Modify `max_results`, `search_type`, etc.
3. **Add features:** Extend with your own analysis or processing logic
4. **Configure proxies:** Add proxy configuration for production use

## Troubleshooting

### Common Issues

1. **API Key Error:**
   ```
   ❌ Error: Please set your SERPER_API_KEY in the .env file
   ```
   **Solution:** Ensure your `.env` file exists and contains a valid API key

2. **Import Errors:**
   ```
   ModuleNotFoundError: No module named 'serp_forge'
   ```
   **Solution:** Install the package: `pip install serp-forge`

3. **Rate Limiting:**
   ```
   ❌ Search failed: Rate limit exceeded
   ```
   **Solution:** Add delays between requests or use proxy rotation

### Performance Tips

- Use `parallel=True` for batch processing
- Implement exponential backoff for retries
- Filter results early to reduce processing time
- Use async examples for high-volume scraping

## Next Steps

After running the examples:

1. **Explore the API:** Check the [API Reference](../docs/API.md)
2. **Configure settings:** See [Configuration Guide](../docs/CONFIGURATION.md)
3. **Build your own:** Use these examples as templates for your projects
4. **Join the community:** Contribute examples or report issues

## Support

- 📖 [Documentation](../docs/)
- 🐛 [Report Issues](https://github.com/vishalm/serp-forge/issues)
- 💬 [Discussions](https://github.com/vishalm/serp-forge/discussions) 