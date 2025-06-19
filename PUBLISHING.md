# Publishing Guide for serp-forge

This guide covers both automated and manual publishing methods for the serp-forge package.

## 🚀 Automated Publishing (Recommended)

### GitHub Actions Workflow

The project includes an automated publishing workflow that triggers on:

1. **Tag-based releases**: Push a version tag (e.g., `v1.0.0`)
2. **Manual triggers**: Use the GitHub Actions UI to manually trigger the workflow

### Setup for Automated Publishing

1. **Add PyPI API Token to GitHub Secrets**:
   - Go to your GitHub repository → Settings → Secrets and variables → Actions
   - Add a new repository secret named `PYPI_API_TOKEN`
   - Set the value to your PyPI API token

2. **Create and push a version tag**:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

3. **Or trigger manually**:
   - Go to Actions tab in your GitHub repository
   - Select "Publish to PyPI" workflow
   - Click "Run workflow"
   - Enter the version number
   - Click "Run workflow"

### Workflow Features

- ✅ Automatic package building
- ✅ Package validation with `twine check`
- ✅ Secure token-based authentication
- ✅ Automatic GitHub release creation
- ✅ Support for both tag-based and manual triggers

## 🔧 Manual Publishing

### Prerequisites

1. **Install required tools**:
   ```bash
   pip install build twine
   ```

2. **Get PyPI API Token**:
   - Go to [PyPI Account Settings](https://pypi.org/manage/account/)
   - Create an API token with "Entire account" scope
   - Copy the token (starts with `pypi-`)

### Method 1: Using the Publish Script

1. **Set your API token**:
   ```bash
   export TWINE_PASSWORD=your_pypi_api_token_here
   ```

2. **Run the publish script**:
   ```bash
   ./scripts/publish.sh [version]
   ```

### Method 2: Manual Commands

1. **Clean previous builds**:
   ```bash
   rm -rf dist/ build/ *.egg-info/
   ```

2. **Build the package**:
   ```bash
   python -m build
   ```

3. **Check the built packages**:
   ```bash
   twine check dist/*
   ```

4. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

### Method 3: Using Environment Variables

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=your_pypi_api_token_here
twine upload dist/*
```

## 📋 Pre-Publishing Checklist

Before publishing, ensure:

- [ ] All tests pass: `pytest`
- [ ] Code is linted and formatted
- [ ] Version number is updated in `pyproject.toml`
- [ ] CHANGELOG.md is updated (if applicable)
- [ ] README.md is up to date
- [ ] All dependencies are correctly specified
- [ ] Package builds successfully: `python -m build`
- [ ] Package passes validation: `twine check dist/*`

## 🔄 Version Management

### Updating Version

1. **Update version in `pyproject.toml`**:
   ```toml
   [project]
   version = "1.0.1"
   ```

2. **Commit the change**:
   ```bash
   git add pyproject.toml
   git commit -m "Bump version to 1.0.1"
   ```

3. **Create and push a tag**:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

### Semantic Versioning

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.0.0)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## 🛠️ Troubleshooting

### Common Issues

1. **Authentication Error**:
   - Ensure your PyPI API token is correct
   - Check that the token has the right permissions

2. **Package Already Exists**:
   - Version numbers must be unique
   - Increment the version number before re-publishing

3. **Build Errors**:
   - Check that all dependencies are installed
   - Verify `pyproject.toml` syntax
   - Ensure all required files are included in `MANIFEST.in`

4. **Validation Errors**:
   - Run `twine check dist/*` to identify issues
   - Check README.md formatting
   - Verify package metadata

### Getting Help

- Check the [PyPI documentation](https://packaging.python.org/tutorials/packaging-projects/)
- Review [twine documentation](https://twine.readthedocs.io/)
- Check GitHub Actions logs for detailed error messages

## 🔐 Security Notes

- Never commit API tokens to version control
- Use GitHub Secrets for automated workflows
- Use environment variables for manual publishing
- Regularly rotate your PyPI API tokens

## 📊 Publishing Statistics

After successful publishing, you can:

- View your package on PyPI: https://pypi.org/project/serp-forge/
- Check download statistics
- Monitor package health
- Respond to user feedback and issues 