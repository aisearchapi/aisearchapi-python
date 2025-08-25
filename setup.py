"""
Setup script for AI Search API Python client library.

This is a fallback setup.py for compatibility with older systems.
Modern installations should use pyproject.toml with pip.
"""

from setuptools import setup, find_packages
import pathlib

# Read the contents of README file
this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="aisearchapi",
    version="1.0.0",
    author="AI Search API",
    author_email="support@aisearchapi.io",
    description="Python client library for AI Search API - search and retrieve intelligent responses with context awareness",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aisearchapi/aisearchapi-python",
    project_urls={
        "Documentation": "https://aisearchapi.readthedocs.io/",
        "Source": "https://github.com/aisearchapi/aisearchapi-python",
        "Tracker": "https://github.com/aisearchapi/aisearchapi-python/issues",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "aisearchapi": ["py.typed"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Typing :: Typed",
    ],
    keywords=[
        "ai", "search", "api", "llm", "embeddings", "semantic-search",
        "machine-learning", "natural-language-processing"
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "typing-extensions>=4.0.0; python_version<'3.10'",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0", 
            "black>=22.0",
            "isort>=5.0",
            "flake8>=4.0",
            "mypy>=0.900",
            "types-requests>=2.25.0",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
        "test": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "pytest-asyncio>=0.18.0",
            "responses>=0.18.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)