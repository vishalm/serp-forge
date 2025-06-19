#!/bin/bash

# Manual Publishing Script for serp-forge
# Usage: ./scripts/publish.sh [version]

set -e

# Default version
VERSION=${1:-"1.0.0"}

echo "🚀 Publishing serp-forge version $VERSION to PyPI"

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Warning: Virtual environment not detected. Activating..."
    source venv/bin/activate
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Build the package
echo "🔨 Building package..."
python -m build

# Check the built packages
echo "✅ Checking built packages..."
twine check dist/*

# Upload to PyPI
echo "📤 Uploading to PyPI..."
echo "Username: __token__"
echo "Password: [Your PyPI API Token]"
echo ""
echo "Make sure you have set your PyPI API token as an environment variable:"
echo "export TWINE_PASSWORD=your_api_token_here"
echo ""

# Check if API token is set
if [ -z "$TWINE_PASSWORD" ]; then
    echo "❌ Error: TWINE_PASSWORD environment variable not set"
    echo "Please set your PyPI API token:"
    echo "export TWINE_PASSWORD=your_api_token_here"
    exit 1
fi

# Upload
twine upload dist/*

echo "🎉 Successfully published serp-forge $VERSION to PyPI!"
echo "📦 Package available at: https://pypi.org/project/serp-forge/" 