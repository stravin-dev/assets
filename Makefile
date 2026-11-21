.PHONY: help install assets test build serve check clean

UV ?= uv
PRE_COMMIT ?= pre-commit

help: ## Show available make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

install: ## Sync Python dependencies with uv
	$(UV) sync

assets: ## Generate canonical SVGs, raster assets, and docs-ready copies
	$(UV) run stravin-assets build

test: ## Run automated pytest suite
	$(UV) run pytest

build: assets ## Build the Zensical static site in strict mode
	$(UV) run zensical build --strict

serve: assets ## Serve the Zensical site locally with live reload
	$(UV) run zensical serve

check: assets build test ## Run asset build, strict site build, tests, ruff, and pre-commit
	$(UV) run ruff check .
	$(PRE_COMMIT) run --all-files

clean: ## Remove generated build artifacts and cache
	rm -rf site .cache dist docs/assets/generated
