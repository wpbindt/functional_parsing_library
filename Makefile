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

.PHONY: deploy
deploy: image
	$(DOCKER_RUN) python3 -m build
	docker run -v $(CURDIR):/srv --env-file=/tmp/.env parsing_library python3 -m twine upload --non-interactive --repository pypi dist/*
