Overview
This project focuses on implementing a load balancer that efficiently distributes requests among multiple servers to ensure balanced resource utilization and improved throughput. The load balancer utilizes consistent hashing for request distribution.

Coding Environment
Operating System: Ubuntu 20.04 LTS or above
Docker Version: 20.10.23 or above
Languages: Python (preferable), C++

Dependencies
Docker

Usage
Deployment
Clone this repository to your local machine.
git clone https://github.com/raymunyi/DS_LoadBalancer.git

Navigate to the project directory.
cd DS_LoadBalancer

Deploy the load balancer and servers within a Docker network.
docker-compose up --build

APIs
Endpoint 1: /api/request
Description: Accepts incoming requests from clients.
Method: POST
Parameters: {request_data}
Example: curl -X POST -d '{"data": "example"}' http://localhost:8000/api/request
Endpoint 2: /api/status
Description: Retrieves the status of servers.
Method: GET
Example: curl http://localhost:8000/api/status

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

Design Choices
Consistent hashing is chosen for request distribution due to its ability to maintain a balanced load even when servers are added or removed from the pool.
Docker is used for containerization to ensure consistency and portability across different environments.
The load balancer is implemented as a separate service to decouple request handling from server management.

Performance Analysis
The performance of the load balancer is evaluated based on metrics such as response time, throughput, and resource utilization.
Scalability tests are conducted to assess the system's ability to handle increasing loads by adding more servers.
Benchmarking tools are used to measure the impact of different configuration settings on performance.

Appendix
Appendix A: Consistent Hashing Algorithm