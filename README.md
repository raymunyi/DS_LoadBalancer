# DS Load Balancer

## Overview
This project focuses on implementing a load balancer that efficiently distributes requests among multiple servers to ensure balanced resource utilization and improved throughput. The load balancer utilizes consistent hashing for request distribution.

## Coding Environment
- **Operating System**: Ubuntu 20.04 LTS or above
- **Docker Version**: 20.10.23 or above
- **Languages**: Python (preferable), C++

## Dependencies
- **Docker**

## Usage

### Deployment
1. **Clone this repository to your local machine:**
   ```bash
   git clone https://github.com/raymunyi/DS_LoadBalancer.git

Navigate to the project directory:
cd DS_LoadBalancer

Deploy the load balancer and servers within a Docker network:
docker-compose up --build

APIs
Endpoint 1: /api/request
Description: Accepts incoming requests from clients.
Method: POST
Parameters: {request_data}
Example:

curl -X POST -d '{"data": "example"}' http://localhost:8000/api/request

Endpoint 2: /api/status
Description: Retrieves the status of servers.
Method: GET
Example:
curl http://localhost:8000/api/status

Fault Tolerance
The load balancer ensures fault tolerance by spawning new replicas of servers in case of failure.

Assumptions
Clients send requests to the load balancer using the provided APIs.
Servers are capable of processing incoming requests asynchronously.
Servers are homogeneous in terms of hardware and software configuration.

Testing
Unit tests are provided to ensure the correctness of individual components.
Integration tests validate the behavior of the load balancer and servers in a simulated environment.
Load testing is performed to assess the system's performance under various traffic conditions.

![testing server 1](https://github.com/raymunyi/DS_LoadBalancer/assets/109039274/5670f8fa-7250-4be8-bab6-0bfcd90c66df)


![testing2](https://github.com/raymunyi/DS_LoadBalancer/assets/109039274/96baad31-72a6-4590-b981-ef0bfea84332)


![testing3](https://github.com/raymunyi/DS_LoadBalancer/assets/109039274/1fdbb2dc-e545-4494-ab55-98204eb8c4be)

![testing 4](https://github.com/raymunyi/DS_LoadBalancer/assets/109039274/97450082-e805-4449-a23d-9904f831cc78)

![testing5](https://github.com/raymunyi/DS_LoadBalancer/assets/109039274/c7c44f92-ca14-4f91-8ac0-8d6afd49dd90)


![testing6](https://github.com/raymunyi/DS_LoadBalancer/assets/109039274/8eeb7396-bfbe-4d59-a2ae-56af80ac28b3)


Design Choices
Consistent hashing is chosen for request distribution due to its ability to maintain a balanced load even when servers are added or removed from the pool.
Docker is used for containerization to ensure consistency and portability across different environments.
The load balancer is implemented as a separate service to decouple request handling from server management.


Performance Analysis
The performance of the load balancer is evaluated based on metrics such as response time, throughput, and resource utilization.
Scalability tests are conducted to assess the system's ability to handle increasing loads by adding more servers.
Benchmarking tools are used to measure the impact of different configuration settings on performance.

Detailed Implementation
Virtual Servers
Instead of placing a single instance of a physical server in the circular hash-map structure, more than one replica of a physical server is mapped into the structure. Two variables i and j represent a virtual server S(i,j) and are used as inputs to the hash function Φ to map the servers with minimum conflicts. Here, i represents the server ID, and j represents the virtual server replica ID of server Si. Thus, a virtual server slot number slotn ← Φ(i, j)%M.

Docker Setup
Docker: latest [version 20.10.23, build 7155243]


sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io


Docker-compose standalone [version v2.15.1]

sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose


Privileged Containers
A privileged container is a container that has all the capabilities of the host machine, lifting all the limitations regular containers have. This means that privileged containers can perform almost every action that can be performed directly on the host. Privileged containers can spawn other containers, manage the host network card, remove containers, etc.

Example docker-compose file with privileged containers:

version: '3.8'
services:
  privileged_service:
    image: your_image
    privileged: true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    network_mode: host


Authors
George Stephen
Shaleen Ndirangu
Charity Claire
Raymond Munyi

License
This project is licensed under the MIT License-see the LICENSE file for details.
