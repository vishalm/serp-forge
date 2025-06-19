# Serp Forge Makefile
# Common development and deployment tasks

.PHONY: help install install-dev test test-cov lint format type-check clean build docker-build docker-run docker-shell logs debug test-performance security backup

# Default target
help:
	@echo "🚀 Serp Forge - Available Commands"
	@echo "========================================"
	@echo ""
	@echo "📦 Installation:"
	@echo "  install      - Install production dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  install-dash - Install with dashboard dependencies"
	@echo ""
	@echo "🧪 Testing:"
	@echo "  test         - Run all tests"
	@echo "  test-cov     - Run tests with coverage"
	@echo "  test-unit    - Run unit tests only"
	@echo "  test-int     - Run integration tests only"
	@echo ""
	@echo "🔧 Development:"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black and isort"
	@echo "  type-check   - Run type checking with mypy"
	@echo "  clean        - Clean build artifacts"
	@echo ""
	@echo "📚 Documentation:"
	@echo "  docs         - Build documentation"
	@echo "  serve-docs   - Serve documentation locally"
	@echo ""
	@echo "🚀 Deployment:"
	@echo "  build        - Build package"
	@echo "  install-cli  - Install CLI tool"
	@echo "  docker-build - Build Docker image"
	@echo ""
	@echo "🛠️  Utilities:"
	@echo "  verify       - Verify installation"
	@echo "  config       - Show current configuration"
	@echo "  example      - Run example script"
	@echo "  logs         - View logs"
	@echo "  debug        - Debug mode"
	@echo "  test-performance - Performance testing"
	@echo "  security     - Security checks"
	@echo "  backup       - Backup configuration"

# Installation targets
install:
	pip install -r requirements.txt

install-dev:
	pip install -e ".[dev]"
	pre-commit install

install-dash:
	pip install -e ".[dashboard]"

# Testing targets
test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=serp_forge --cov-report=html --cov-report=term-missing

test-unit:
	pytest tests/ -m unit -v

test-int:
	pytest tests/ -m integration -v

# Development targets
lint:
	flake8 serp_forge/ tests/
	black --check serp_forge/ tests/
	isort --check-only serp_forge/ tests/

format:
	black serp_forge/ tests/
	isort serp_forge/ tests/

type-check:
	mypy serp_forge/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Documentation targets
docs:
	sphinx-build -b html docs/ docs/_build/html

serve-docs:
	cd docs/_build/html && python -m http.server 8000

# Deployment targets
build:
	python setup.py sdist bdist_wheel

install-cli:
	pip install -e .

docker-build:
	docker build -t serp-forge .

# Utility targets
verify:
	python test_installation.py

config:
	python -c "from serp_forge.config import config; import yaml; print(yaml.dump(config.to_dict(), default_flow_style=False))"

example:
	python examples/basic_usage.py

# Quick start
quick-start: install
	@echo "✅ Serp Forge installed successfully!"
	@echo "💡 Next steps:"
	@echo "   1. Set your SERPER_API_KEY environment variable"
	@echo "   2. Try: serp-forge 'test query'"
	@echo "   3. Check examples/basic_usage.py for usage examples"

# Development workflow
dev-setup: install-dev format lint test
	@echo "✅ Development environment setup complete!"

# CI/CD targets
ci: lint type-check test-cov
	@echo "✅ CI checks passed!"

# Release preparation
release-prep: clean build test-cov lint type-check
	@echo "✅ Release preparation complete!"

# Docker targets
docker-run:
	docker run -e SERPER_API_KEY=$$SERPER_API_KEY serp-forge "test query"

docker-dev:
	docker run -it --rm -v $(PWD):/app -w /app serp-forge bash

# Monitoring and debugging
logs:
	tail -f logs/serp_forge.log

debug:
	python -m pdb -m serp_forge.cli "test query"

# Environment setup
env-setup:
	cp env.example .env
	@echo "✅ Environment file created. Please edit .env with your settings."

# Database targets (if using database)
db-init:
	alembic upgrade head

db-migrate:
	alembic revision --autogenerate -m "$(message)"

db-upgrade:
	alembic upgrade head

# Cache targets (if using Redis)
redis-start:
	redis-server --daemonize yes

redis-stop:
	redis-cli shutdown

# Proxy testing
test-proxy:
	python -c "from serp_forge.serper import scrape; print(scrape('test', proxy_rotation=True))"

# Performance testing
benchmark:
	python -c "import time; from serp_forge.serper import scrape; start=time.time(); scrape('test', max_results=10); print(f'Time: {time.time()-start:.2f}s')"

# Security checks
security-check:
	bandit -r serp_forge/
	safety check

# Dependencies management
update-deps:
	pip install --upgrade -r requirements.txt

freeze-deps:
	pip freeze > requirements-frozen.txt

# Backup and restore
backup-config:
	cp serp_forge_config.yaml backup_config_$(shell date +%Y%m%d_%H%M%S).yaml

restore-config:
	@echo "Available backups:"
	@ls -la backup_config_*.yaml 2>/dev/null || echo "No backups found"

# Help for specific targets
help-install:
	@echo "Installation Commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install with development tools"
	@echo "  make quick-start  - Complete setup for development"

help-test:
	@echo "Testing Commands:"
	@echo "  make test         - Run all tests"
	@echo "  make test-cov     - Run tests with coverage report"
	@echo "  make test-unit    - Run only unit tests"
	@echo "  make test-int     - Run only integration tests"

help-dev:
	@echo "Development Commands:"
	@echo "  make format       - Format code with black and isort"
	@echo "  make lint         - Check code quality"
	@echo "  make type-check   - Run type checking"
	@echo "  make dev-setup    - Complete development setup"

# Quick start commands
quick-test: install-dev
	@echo "🧪 Running quick test..."
	python -c "from serp_forge.serper import scrape; print(scrape('test', proxy_rotation=True))"

# Development workflow
dev-test: lint type-check test

dev-format: format
	@echo "✅ Code formatted successfully"

# Production deployment
prod-build: clean build
	@echo "✅ Production build completed"

prod-test: test-cov security
	@echo "✅ Production tests passed"

# Monitoring and debugging
monitor:
	@echo "📊 Monitoring Serp Forge..."
	python -c "from serp_forge.utils.logging import get_logger; logger = get_logger('monitor'); logger.info('Monitoring started')"

profile:
	@echo "📈 Profiling Serp Forge..."
	python -c "import cProfile; import pstats; from serp_forge.serper import scrape; profiler = cProfile.Profile(); profiler.enable(); scrape('test query'); profiler.disable(); stats = pstats.Stats(profiler); stats.sort_stats('cumulative'); stats.print_stats(10)"

# Docker targets
docker-shell:
	docker run -it --rm -v $(PWD):/app -w /app serp-forge bash

# New targets
test-performance:
	@echo "Testing performance..."
	python -c "import time; from serp_forge.serper import scrape; start=time.time(); scrape('test', max_results=10); print(f'Time: {time.time()-start:.2f}s')"

security:
	bandit -r serp_forge/
	safety check

backup:
	cp serp_forge_config.yaml backup_config_$(shell date +%Y%m%d_%H%M%S).yaml

# New quick start
quick-start: install
	@echo "✅ Serp Forge installed successfully!"
	@echo "💡 Next steps:"
	@echo "   1. Set your SERPER_API_KEY environment variable"
	@echo "   2. Try: serp-forge 'test query'"
	@echo "   3. Check examples/basic_usage.py for usage examples"

# New development workflow
dev-setup: install-dev
	pre-commit install

dev-test: lint type-check test

dev-format: format
	@echo "✅ Code formatted successfully"

# New production deployment
prod-build: clean build
	@echo "✅ Production build completed"

prod-test: test-cov security
	@echo "✅ Production tests passed"

# New monitoring and debugging
monitor:
	@echo "📊 Monitoring Serp Forge..."
	python -c "from serp_forge.utils.logging import get_logger; logger = get_logger('monitor'); logger.info('Monitoring started')"

profile:
	@echo "📈 Profiling Serp Forge..."
	python -c "import cProfile; import pstats; from serp_forge.serper import scrape; profiler = cProfile.Profile(); profiler.enable(); scrape('test query'); profiler.disable(); stats = pstats.Stats(profiler); stats.sort_stats('cumulative'); stats.print_stats(10)" 