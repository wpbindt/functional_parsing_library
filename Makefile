.PHONY: image
image:
	docker build -t parsing_library .

.PHONY: run-tests
run-tests:
	docker run -v $(CURDIR):/srv parsing_library pytest /srv

.PHONY: mypy
mypy:
	docker run -v $(CURDIR):/srv parsing_library mypy /srv

.PHONY: flake
flake:
	docker run -v $(CURDIR):/srv parsing_library flake8 /srv
