
run:
    @uv run hashtree.py testing/happy_path

setup:
    @uv sync

clean:
    rm -rf .venv
    rm -rf dist
    rm -rf htmlcov
    rm -rf .pytest_cache
    rm -rf .ruff_cache
    rm -rf tests/__pycache__
    rm -rf hashtree/__pycache__
    rm -f .coverage

update_deps: clean
    @uv sync --upgrade

test:
    @uv run pytest

coverage:
    @uv run pytest --cov hashtree --cov-report html

lint:
    uv run mypy .
    uv run ruff check .

build: clean setup test lint
    @uv build
    @echo Build successful!

install: build
    @pip install .
