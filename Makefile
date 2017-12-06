clean: ## Clean environment
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log


setup:  ## Create base image
	docker build -t algorithms .


test:  clean ## Run tests
	docker run -e PYTHONDONTWRITEBYTECODE=1 -v $(CURDIR)/:/code algorithms