.PHONY: build up down logs shell

build:
	docker compose -f deploy/docker-compose.yml build

up:
	docker compose -f deploy/docker-compose.yml up --build

# down:
#     docker compose -f deploy/docker-compose.yml down

# logs:
#     docker compose -f deploy/docker-compose.yml logs -f

# shell:
#     docker compose -f deploy/docker-compose.yml exec rasa /bin/bash