# AGENTS.md

## Project Overview
Local-first stack to chat with your documents, the agentic way.

This is a Python project created from a cookiecutter template. It uses modern tooling including `uv` for dependency management, `ruff` for formatting, and `ty` for static type checking.

## Development Commands
When working on this project, use these commands via the `Makefile`:

- **Environment Setup**: `make setup` (Installs dependencies and sets up the virtual environment).
- **Format Code**: `make format` (Runs `ruff` to format code).
- **Lint/Type Check**: `make lint` (Runs `ty` and other static analysis).
- **Run Tests**: `make test` (Runs the test suite).

## Agent Workflow
After making any changes to Python code, you **MUST**:

1.  Run `make format` to ensure code style consistency.
2.  Run `make lint` to verify type safety and catch errors.

If either command returns an error or warning, you must fix the issues before considering the task complete.

## Project Structure
- `src/`: Main source code directory.
- `tests/`: Project test suite.
- `pyproject.toml`: Project configuration for `uv`, `ruff`, and `ty`.
- `Makefile`: Entry point for all development tasks.

## Technical Guidance
- **Dependency Management**: Use `uv` commands (e.g., `uv add <package>`) to modify dependencies, then run `make setup`.
- **Typing**: The project uses strict type checking with `ty`. Ensure all new code has proper type hints.
- **Formatting**: `ruff` is used for both linting and formatting. Always run `make format` before completing a task.
- **System Dependencies**:
  - This project uses `nix` and `direnv`. System-level packages should be added to `shell.nix`.

## Workflow Expectations
1.  After modifying code, run `make format` and `make lint`.
2.  Ensure all tests pass by running `make test`.
3.  If adding new dependencies, update `pyproject.toml` and run `make setup`.