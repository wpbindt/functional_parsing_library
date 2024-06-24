DOCKER_RUN = docker run -v $(CURDIR):/srv parsing_library

.PHONY: image
image:
	docker build -t parsing_library .

.PHONY: run-tests
run-tests:
	$(DOCKER_RUN) pytest .

.PHONY: mypy
mypy:
	$(DOCKER_RUN) mypy .

.PHONY: flake
flake:
	$(DOCKER_RUN) flake8 .

.PHONY: build
build: image
	$(DOCKER_RUN) python3 -m build
