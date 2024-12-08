IMAGE = parsing_library
DOCKER_RUN_PREFIX = docker run -v $(CURDIR):/srv
DOCKER_RUN = $(DOCKER_RUN_PREFIX) $(IMAGE)
DOCKER_RUN_WITH_EXPOSED_PORT = $(DOCKER_RUN_PREFIX) -p 8000:8000 $(IMAGE)

.PHONY: image
image:
	docker build -t $(IMAGE) .

.PHONY: run-tests
run-tests:
	$(DOCKER_RUN) pytest .

.PHONY: mypy
mypy:
	$(DOCKER_RUN) mypy --show-traceback .

.PHONY: build
build: image
	$(DOCKER_RUN) python3 -m build

.PHONY: documentation
documentation: clean
	$(DOCKER_RUN) pdoc --html functional_parsing_library

.PHONY: serve-documentation
serve-documentation: documentation
	$(DOCKER_RUN_WITH_EXPOSED_PORT) python -m http.server 8000 --directory html/functional_parsing_library

.PHONY: ruff
ruff:
	$(DOCKER_RUN) ruff check .

.PHONY: clean
clean: image
	$(DOCKER_RUN) rm -rf dist functional_parsing_library.egg-info html

.PHONY: all-checks
all-checks: image ruff mypy run-tests
