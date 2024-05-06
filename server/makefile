# Define variables
IMAGE_NAME := load-balancer-server
CONTAINER_NAME := web-server
SERVER_ID := 1

.PHONY: all build run clean

# Default target
all: build run

# Build the Docker image
build:
    docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
    docker run -d -p 5000:5000 --name $(CONTAINER_NAME) -e SERVER_ID=$(SERVER_ID) $(IMAGE_NAME)

# Stop and remove the Docker container
clean:
    docker stop $(CONTAINER_NAME)
    docker rm $(CONTAINER_NAME)
