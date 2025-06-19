# Testing Guide for serp-forge

This document explains how to run, write, and maintain tests for the `serp-forge` project.

---

## Table of Contents
- [Test Types](#test-types)
- [Environment Setup](#environment-setup)
- [Running Tests](#running-tests)
- [Writing New Tests](#writing-new-tests)
- [Mocking and Patching](#mocking-and-patching)
- [Troubleshooting](#troubleshooting)

---

## Test Types

The project includes several types of tests:

- **Unit Tests:** Test individual functions/classes in isolation (e.g., config, models).
- **Functional Tests:** Test workflows and feature integration (e.g., scraping, batch processing).
- **Integration Tests:** Test integration with external systems and end-to-end flows.
- **CLI Tests:** Test the command-line interface and its options.

Test files are located in the `tests/` directory and are named according to their focus:
- `test_basic.py` — Unit tests
- `test_functional.py` — Functional tests
- `test_integration.py` — Integration tests
- `test_cli.py` — CLI tests

---

## Environment Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

2. **Set up environment variables:**
   - Most tests use mock data and do not require real API keys.
   - For integration tests with real APIs, set the following in your environment or `.env` file:
     ```env
     SERPER_API_KEY=your_api_key_here
     ```

3. **(Optional) Install test tools:**
   - Install `pytest` and plugins if not already installed:
     ```bash
     pip install pytest pytest-cov
     ```

---

## Running Tests

- **Run all tests:**
  ```bash
  pytest -v --maxfail=20
  ```

- **Run a specific test file:**
  ```bash
  pytest tests/test_basic.py
  ```

- **Run a specific test class or function:**
  ```bash
  pytest tests/test_basic.py::TestBasicConfig::test_scraping_config
  ```

- **Show test coverage:**
  ```bash
  pytest --cov=serp_forge
  ```

---

## Writing New Tests

- Place new tests in the appropriate file in `tests/`.
- Use `pytest` style (functions or classes with `test_` prefix).
- For new modules, create a corresponding `test_*.py` file.
- Use fixtures and mocks to isolate units and avoid real network calls.

**Example unit test:**
```python
from serp_forge.serper.models import SearchResult

def test_search_result_url_normalization():
    result = SearchResult(
        title="Test",
        url="https://example.com/",
        snippet="Test",
        position=1,
        source="example.com"
    )
    assert str(result.url) == "https://example.com"
```

---

## Mocking and Patching

- Use `unittest.mock.patch` to mock external dependencies, network calls, or file I/O.
- Example:
  ```python
  from unittest.mock import patch, Mock

  @patch('serp_forge.serper.core.SerperClient')
  def test_scrape_with_mocked_client(mock_client_class):
      mock_client = Mock()
      mock_client.search.return_value = {"organic": []}
      mock_client_class.return_value = mock_client
      # ...
  ```
- For CLI tests, mock `sys.argv`, `sys.stdout`, and file operations as needed.

---

## Troubleshooting

- **Import errors:** Ensure your virtual environment is activated and the package is installed in editable mode (`pip install -e .`).
- **Missing environment variables:** Most tests use mocks, but some integration tests require real API keys.
- **Network/API errors:** Use mocks for unit/functional tests. Only integration tests should hit real APIs.
- **File not found in CLI tests:** Mock `pathlib.Path.exists` and `open` as shown in the CLI test examples.
- **Deprecation warnings:** Some warnings from dependencies (e.g., Pydantic) are expected and do not affect test results.

---

## Additional Resources
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- [Pydantic Testing Guide](https://docs.pydantic.dev/latest/usage/testing/)

---

For any issues or to contribute new tests, please open a pull request or issue on [GitHub](https://github.com/vishal-mishra/serp-forge). 