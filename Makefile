build:
	docker-compose build

run:
	docker-compose run --rm -d --service-ports photo_server

shell:
	docker-compose run -u worker photo_server bash

debug:
	docker-compose run --rm --service-ports photo_server

