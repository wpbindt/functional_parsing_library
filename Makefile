image:
	docker build -t parsing_library .

run-tests:
	docker run -v $(CURDIR):/srv parsing_library pytest /srv
