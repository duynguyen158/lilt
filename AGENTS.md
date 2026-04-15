# AGENTS.md

## Project Overview

Local-first stack to chat with your documents, the agentic way.

The stack runs [LibreChat](https://www.librechat.ai/) as the chat UI, backed by [Docker Model Runner](https://docs.docker.com/desktop/features/model-runner/) to serve LLMs locally (default: `ai/gemma4:E2B`). Supporting services (MongoDB, Meilisearch, pgvector, RAG API) are orchestrated via Docker Compose.

This is a Python project using `uv` for dependency management, `ruff` for formatting, and `ty` for static type checking.

## Development Commands

When working on this project, use these commands via the `Makefile`:

- **Environment Setup**: `make setup` (Installs dependencies, sets up the virtual environment, and copies `.env.example` to `.env`).
- **Format Code**: `make format` (Runs `ruff` to format code).
- **Lint/Type Check**: `make lint` (Runs `ty` and other static analysis).
- **Run Tests**: `make test` (Runs the test suite).
- **Start Services**: `make start` (Brings up the full Docker Compose stack).
- **Stop Services**: `make stop` (Tears down all Docker Compose services).

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
- `compose.yaml`: Docker Compose stack (LibreChat + supporting services + Docker Model Runner model config).
- `librechat.yaml`: LibreChat configuration (endpoints, UI settings). The active endpoint is `Docker` (Docker Model Runner). An `LM Studio` endpoint is also defined but commented out.
- `.env` / `.env.example`: Environment variables for LibreChat and the stack. `make setup` copies `.env.example` to `.env` automatically.

## Technical Guidance

- **Dependency Management**: Use `uv` commands (e.g., `uv add <package>`) to modify dependencies, then run `make setup`.
- **Typing**: The project uses strict type checking with `ty`. Ensure all new code has proper type hints.
- **Formatting**: `ruff` is used for both linting and formatting. Always run `make format` before completing a task.
- **System Dependencies**: This project uses `nix` and `direnv`. System-level packages should be added to `shell.nix`.
- **Model Configuration**: The active LLM is `ai/gemma4:E2B` via Docker Model Runner. To change the model, update the `models` section in `compose.yaml` and the `titleModel`/`default` model list in the `Docker` endpoint block in `librechat.yaml`.
- **Adding Endpoints**: To enable a different provider (e.g., LM Studio), uncomment the relevant block in `librechat.yaml` under `endpoints.custom` and add the endpoint name to `ENDPOINTS` in `.env`.

## Workflow Expectations

1.  After modifying code, run `make format` and `make lint`.
2.  Ensure all tests pass by running `make test`.
3.  If adding new dependencies, update `pyproject.toml` and run `make setup`.
