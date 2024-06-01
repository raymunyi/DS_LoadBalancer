# Define variables
IMAGE_NAME := load-balancer-server

.PHONY: all build run clean

# Default target
all: build run

# Build the Docker image
build:
    docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
    docker run -d -p 5000:5000 --name web-server -e SERVER_ID=1 $(IMAGE_NAME)



# Stop and remove the Docker container
clean:
    docker stop web-server
    docker rm web-server
