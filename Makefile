lint:
	uv run ruff check src/ 

format:
	uv run ruff format src/
	uv run ruff check src/ --fix