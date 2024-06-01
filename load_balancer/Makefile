# Define variables
COMPOSE_FILE := docker-compose.yaml

.PHONY: build up down clean

# Default target
all: build up

# Build the Docker images
build:	docker-compose -f	$(COMPOSE_FILE)	build

# Start the containers
up:	docker-compose -f	$(COMPOSE_FILE)	up -d

# Stop and remove the containers
down:	docker-compose -f	$(COMPOSE_FILE)	down

# Clean up the Docker environment
clean: down	docker system prune -f
