# DS_LoadBalancer

Load Balancer Implementation
Overview
This focuses on implementing a load balancer that efficiently distributes requests among multiple servers to ensure balanced resource utilization and improved throughput. The load balancer utilizes consistent hashing for request distribution.

Coding Environment
Operating System: Ubuntu 20.04 LTS or above
Docker Version: 20.10.23 or above


Languages: Python (preferable), C++
Dependencies
Docker
Usage

Deployment
Clone this repository to your local machine.
bash
Copy code
git clone https://github.com/raymunyi/DS_LoadBalancer.git
Navigate to the project directory.
bash
Copy code
cd load_balancer_project
Deploy the load balancer and servers within a Docker network.
bash
Copy code
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
Appendix
Appendix A: Consistent Hashing Algorithm
