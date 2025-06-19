# Contributing to Serp Forge

Thank you for your interest in contributing to Serp Forge! This document provides guidelines and information for contributors.

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Git
- A Serper API key (for testing)

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/serp-forge.git
   cd serp-forge
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e .
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   ```bash
   export SERPER_API_KEY="your_api_key_here"
   ```

5. **Run tests to verify setup**
   ```bash
   pytest
   ```

## 📝 Code Style

We use several tools to maintain code quality:

### Formatting
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting

### Pre-commit Hooks
Install pre-commit hooks to automatically format code:
```bash
pip install pre-commit
pre-commit install
```

### Manual Formatting
```bash
# Format code
black serp_forge/ tests/

# Sort imports
isort serp_forge/ tests/

# Lint code
flake8 serp_forge/ tests/
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=serp_forge

# Run specific test file
pytest tests/test_basic.py

# Run with verbose output
pytest -v
```

### Writing Tests
- Follow the existing test structure in `tests/`
- Use descriptive test names
- Mock external dependencies
- Test both success and failure cases
- Aim for high test coverage

### Test Categories
- **Unit tests**: Test individual functions and classes
- **Integration tests**: Test component interactions
- **Functional tests**: Test complete workflows
- **CLI tests**: Test command-line interface

## 🔄 Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the code style guidelines
   - Add tests for new functionality
   - Update documentation if needed

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Use the PR template
   - Describe your changes clearly
   - Link any related issues
   - Ensure all tests pass

### Commit Message Format
We follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Maintenance tasks

## 🚀 Release Process

### For Maintainers

1. **Update version**
   - Update version in `pyproject.toml`
   - Update `__version__` in `serp_forge/__init__.py`

2. **Create a release tag**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

3. **GitHub Actions will automatically**
   - Run tests
   - Build the package
   - Publish to PyPI
   - Create a GitHub release

### Versioning
We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## 🐛 Reporting Issues

When reporting issues, please include:
- Python version
- Operating system
- Error messages and stack traces
- Steps to reproduce
- Expected vs actual behavior

## 📚 Documentation

- Keep documentation up to date
- Add docstrings to new functions
- Update README.md for new features
- Include usage examples

## 🤝 Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please:
- Be respectful and inclusive
- Use welcoming and inclusive language
- Be collaborative and constructive
- Focus on what is best for the community

## 🆘 Getting Help

- Check existing issues and PRs
- Join our discussions
- Create an issue for questions
- Reach out to maintainers

## 📋 Checklist for Contributors

Before submitting your PR, ensure:
- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] No sensitive data in commits
- [ ] Commit messages follow conventional format

Thank you for contributing to Serp Forge! 🚀 