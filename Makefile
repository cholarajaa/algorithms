setup:  ## Create base image
	docker build -t algorithms .


test:  ## Run tests
	docker run -v $(CURDIR)/:/code algorithms