image:
	docker build -t parsing_library .

run-tests:
	docker run -v $(CURDIR):/srv parsing_library pytest /srv

mypy:
	docker run -v $(CURDIR):/srv parsing_library mypy /srv

flake:
	docker run -v $(CURDIR):/srv parsing_library flake8 /srv
