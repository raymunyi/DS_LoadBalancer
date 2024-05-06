import asyncio

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.server_index = 0

    async def handle_request(self, request):
        server = self.servers[self.server_index]
        self.server_index = (self.server_index + 1) % len(self.servers)
        response = await self.send_request(server, request)
        return response

    async def send_request(self, server, request):
        # Simulate network latency
        await asyncio.sleep(0.1)
        return f"Response from {server}: {request}"

async def main():
    servers = ["Server1", "Server2", "Server3"]
    load_balancer = LoadBalancer(servers)
    requests = ["Request1", "Request2", "Request3", "Request4"]

    responses = await asyncio.gather(*[load_balancer.handle_request(request) for request in requests])
    for response in responses:
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
