# Publishing to PyPI

This guide explains how to publish Serp Forge to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account on [PyPI](https://pypi.org/account/register/)
2. **TestPyPI Account**: Create an account on [TestPyPI](https://test.pypi.org/account/register/) for testing
3. **API Token**: Generate an API token on PyPI for automated publishing

## Setup

### 1. Install Publishing Tools

```bash
pip install build twine
```

### 2. Configure PyPI Credentials

Create a `~/.pypirc` file:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = your_pypi_api_token_here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = your_testpypi_api_token_here
```

### 3. GitHub Secrets Setup

Add these secrets to your GitHub repository:

- `PYPI_API_TOKEN`: Your PyPI API token
- `TEST_PYPI_API_TOKEN`: Your TestPyPI API token (optional)

## Release Process

### 1. Update Version

Update the version in:
- `pyproject.toml`
- `serp_forge/__init__.py`

### 2. Create Release Tag

```bash
# Commit your changes
git add .
git commit -m "chore: bump version to 1.0.0"

# Create and push tag
git tag v1.0.0
git push origin v1.0.0
```

### 3. Automated Publishing

The GitHub Actions workflow will automatically:
- Run tests
- Build the package
- Publish to PyPI
- Create a GitHub release

### Manual Publishing (if needed)

```bash
# Build the package
python -m build

# Check the build
twine check dist/*

# Upload to TestPyPI (for testing)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## Testing Before Release

### 1. Test on TestPyPI

```bash
# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ serp-forge

# Test the installation
python -c "import serp_forge; print(serp_forge.__version__)"
```

### 2. Test Package

```bash
# Build and check
python -m build
twine check dist/*

# Test installation from local build
pip install dist/*.whl
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify your API token is correct
   - Ensure the token has upload permissions
   - Check your `~/.pypirc` configuration

2. **Version Already Exists**
   - PyPI doesn't allow overwriting existing versions
   - Increment the version number
   - Delete the old tag and create a new one

3. **Build Errors**
   - Check that all dependencies are in `pyproject.toml`
   - Verify the package structure is correct
   - Run `python -m build --help` for options

### Rollback Process

If you need to rollback a release:

1. **Delete the tag locally and remotely**
   ```bash
   git tag -d v1.0.0
   git push origin :refs/tags/v1.0.0
   ```

2. **Note**: PyPI doesn't allow deleting packages, but you can:
   - Release a new version with fixes
   - Mark the problematic version as deprecated

## Best Practices

1. **Always test on TestPyPI first**
2. **Use semantic versioning**
3. **Include comprehensive release notes**
4. **Test the package after publishing**
5. **Keep your API tokens secure**

## Security Notes

- Never commit API tokens to version control
- Use GitHub secrets for CI/CD
- Regularly rotate your API tokens
- Use TestPyPI for testing releases

## Support

If you encounter issues:
1. Check the [PyPI documentation](https://packaging.python.org/tutorials/packaging-projects/)
2. Review the [GitHub Actions logs](https://github.com/vishal-mishra/serp-forge/actions)
3. Create an issue in the repository 