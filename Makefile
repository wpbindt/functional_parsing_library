DOCKER_RUN = docker run -u 1000:1000 -v $(CURDIR):/srv parsing_library
DOCKER_RUN_WITH_EXPOSED_PORT = docker run -u 1000:1000 -p 8000:8000 -v $(CURDIR):/srv parsing_library

.PHONY: image
image:
	docker build -t parsing_library .

.PHONY: run-tests
run-tests:
	$(DOCKER_RUN) pytest .

.PHONY: mypy
mypy:
	$(DOCKER_RUN) mypy .

.PHONY: build
build: image
	$(DOCKER_RUN) python3 -m build

.PHONY: documentation
documentation: clean
	$(DOCKER_RUN) pdoc --html functional_parsing_library

.PHONY: serve-documentation
serve-documentation: documentation
	$(DOCKER_RUN_WITH_EXPOSED_PORT) python -m http.server 8000 --directory html/functional_parsing_library

.PHONY: clean
clean:
	$(DOCKER_RUN) rm -rf dist functional_parsing_library.egg-info html
