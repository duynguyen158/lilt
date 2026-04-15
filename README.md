# lilt

[![Python version](https://img.shields.io/badge/python_version-3.13-blue)](https://github.com/psf/black)

Local-first stack to chat with your documents, the agentic way.

## Usage

This project runs a local-first AI chat stack using [LibreChat](https://www.librechat.ai/) as the UI and [Docker Model Runner](https://docs.docker.com/desktop/features/model-runner/) to serve models locally.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Model Runner enabled
- [uv](https://docs.astral.sh/uv/)

### Quick start

1. Copy the example environment file and fill in any required values:
   ```zsh
   make setup
   ```
2. Start all services:
   ```zsh
   make start
   ```
3. Open LibreChat at [http://localhost:3080](http://localhost:3080).

To stop all services:

```zsh
make stop
```

### Model

The default model is `ai/gemma4:E2B`, served by Docker Model Runner at `http://model-runner.docker.internal/v1`. To switch models, update the `models` section in `compose.yaml` and the `Docker` endpoint in `librechat.yaml`.

An [LM Studio](https://lmstudio.ai/) endpoint is also preconfigured in `librechat.yaml` (commented out by default). To enable it, uncomment the `LM Studio` block under `endpoints.custom` and add `LM Studio` to `ENDPOINTS` in your `.env`.

## Development

This project uses [uv](https://docs.astral.sh/uv/) to manage Python dependencies.

Frequently used commands or groups of commands are defined as `Makefile` recipes. Run `make help` to see a list of available recipes.

### Setting up system dependencies

**If you don't use `direnv` and Nix**, take a look at `shell.nix` and install the listed system dependencies however you wish. _Then, skip to the next section (setting up project dependencies)._

If you use `direnv` and Nix, run `direnv allow` to enable direnv for this project, if you haven't already. Edit the list of system dependencies in `shell.nix`. When you're ready, `cd` again into the project directory. All system dependencies will be installed in a sealed environment specific to your project. This environment will unload if you `cd` out of the project directory, and reload if you `cd` back in. Any changes you make to `shell.nix`, including adding or removing dependencies from the declared `packages` list automatically sync to your environment every time you hit Enter on the command line.

### Setting up project dependencies

It's literally as easy as

```zsh
make setup
```

### Running tests

Run

```zsh
make test
```

to run all unit and (if available) integration tests.

### Code formatting

Applies to Python and (if applicable) Terraform code.

```zsh
make format
```

We use [Ruff](https://docs.astral.sh/ruff/) as the formatter for Python. Rules are specified in `pyproject.toml`.

### Code linting

Here, "linting" refers to the process of static-type checking in Python and (if applicable) validation of Terraform configurations.

```zsh
make lint
```

We use [ty](https://github.com/microsoft/ty) as the Python static type checker. Rules are also specified in `pyproject.toml`.

## Deployment

The stack is fully containerized. Run `make start` to bring up all services via Docker Compose (LibreChat, MongoDB, Meilisearch, pgvector, and the RAG API). All services run under the `lilt` Compose project with the `chat` profile.

---

This project was created using [Duy Nguyen's cookiecutter template](https://github.com/duynguyen158/cookiecutter-python). It includes an `AGENTS.md` file to provide context and instructions for AI coding agents.
