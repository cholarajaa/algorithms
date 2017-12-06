clean: ## Clean environment
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log


setup:  ## Create base image
	docker build -t algorithms .


test:  ## Run tests
	docker run -v $(CURDIR)/:/code algorithms