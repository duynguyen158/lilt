# GENERAL
.PHONY: all help

# VARIABLES
# Whether to rebuild the Docker images before running the command
ENVIRONMENT?=prod

all: help
	@echo "Please specify a target."

help: # Show help for each of the Makefile recipes
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

# SETTING UP
.PHONY: login login-% install install-% setup

login-gcloud: # Login to GCP
	@echo "GCP is not enabled in this project."

login: login-gcloud # Login to all services

install-terraform: # Initialize Terraform
	@echo "Terraform infrastructure-as-code is not enabled in this project."

install-python: # Install Python packages
	uv sync --all-groups
	uv tool install ruff --upgrade
	uvx ruff --version
	uv tool install ty --upgrade
	uvx ty --version

install-env: # Install environment variables
	cp .env.example .env

install: install-terraform install-python install-env # Install all dependencies

setup: login install # Setup the project

# DEVELOPMENT
.PHONY: format format-% lint lint-% test test-% start stop

format-terraform: # Format Terraform code
	@echo "Terraform infrastructure-as-code is not enabled in this project."

format-python: # Format Python code
	-uv tool run ruff format
	uv tool run ruff check --fix

format: format-terraform format-python # Format all code

lint-terraform: # Validate Terraform code
	@echo "Terraform infrastructure-as-code is not enabled in this project."

lint-python: # Check for Python type errors
	uv tool run ty check

lint: lint-terraform lint-python # Lint (validate) all code

test-python: # Run Python tests
	uv run pytest

test: test-python # Run all tests

start: # Start all services
	docker compose -p lilt --profile chat up -d

stop: # Stop all services
	docker compose -p lilt down

# DEPLOYMENT
