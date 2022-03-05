build:
	docker-compose build

run:
	docker-compose run --rm --service-ports photo_server

interactive:
	docker-compose run -u worker photo_server bash

