# AI Search API Python Client - Development Makefile

.PHONY: help install install-dev test test-cov lint format type-check clean build upload docs

# Default target
help:
	@echo "Available targets:"
	@echo "  install      Install package in production mode"
	@echo "  install-dev  Install package in development mode with all dependencies"
	@echo "  test         Run tests"
	@echo "  test-cov     Run tests with coverage report"
	@echo "  lint         Run linting (flake8)"
	@echo "  format       Format code (black, isort)"
	@echo "  type-check   Run type checking (mypy)"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build distribution packages"
	@echo "  upload       Upload to PyPI"
	@echo "  docs         Build documentation"
	@echo "  all          Run format, lint, type-check, and test"

# Installation targets
install:
	pip install .

install-dev:
	pip install -e ".[dev,test,docs]"

# Testing targets
test:
	pytest

test-cov:
	pytest --cov=aisearchapi --cov-report=term-missing --cov-report=html

# Code quality targets
lint:
	flake8 src/ tests/ examples/

format:
	black src/ tests/ examples/
	isort src/ tests/ examples/

type-check:
	mypy src/

# Build and distribution targets
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

upload: build
	python -m twine upload dist/*

upload-test: build
	python -m twine upload --repository testpypi dist/*

# Documentation
docs:
	cd docs && make html

docs-serve:
	cd docs/_build/html && python -m http.server 8000

# Comprehensive check
all: format lint type-check test

# Development setup
setup-dev:
	python -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "  source venv/bin/activate  # On Unix/Mac"
	@echo "  venv\\Scripts\\activate     # On Windows"
	@echo "Then run: make install-dev"

# Check if virtual environment is active
check-venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Warning: No virtual environment detected. Consider using 'make setup-dev'"; \
	fi

# Example usage
example:
	python examples/basic_usage.py

# Security check
security:
	safety check
	bandit -r src/

# Pre-commit hooks setup
pre-commit-install:
	pre-commit install

pre-commit-run:
	pre-commit run --all-files