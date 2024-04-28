import asyncio

class LoadBalancer:
    def __init__(self, servers):
        # Initialize the load balancer with a list of servers
        self.servers = servers
        self.server_index = 0

    async def handle_request(self, request):
        # Handle incoming requests by distributing them among servers
        server = self.servers[self.server_index]
        self.server_index = (self.server_index + 1) % len(self.servers)
        response = await self.send_request(server, request)
        return response

    async def send_request(self, server, request):
        # Simulate network latency before sending request to server
        await asyncio.sleep(0.1)
        # Construct response from server
        return f"Response from {server}: {request}"

async def main():
    # Define list of servers
    servers = ["Server1", "Server2", "Server3"]
    # Initialize load balancer with servers
    load_balancer = LoadBalancer(servers)
    # Define list of requests
    requests = ["Request1", "Request2", "Request3", "Request4"]

    # Send requests to load balancer and gather responses asynchronously
    responses = await asyncio.gather(*[load_balancer.handle_request(request) for request in requests])
    # Print responses received from servers
    for response in responses:
        print(response)

if __name__ == "__main__":
    # Run the main function using asyncio
    asyncio.run(main())
