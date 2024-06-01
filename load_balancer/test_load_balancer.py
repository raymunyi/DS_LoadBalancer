# test_load_balancer.py
import asyncio
import aiohttp
import random
import matplotlib.pyplot as plt
import json

LOAD_BALANCER_URL = 'http://localhost:5000/'

async def send_request(session, path):
    async with session.get(f'{LOAD_BALANCER_URL}/{path}') as response:
        return await response.text()

async def launch_requests(num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            path = 'home'
            tasks.append(send_request(session, path))
        responses = await asyncio.gather(*tasks)
    return responses

def count_responses(responses):
    counts = {}
    for response in responses:
        server_id = json.loads(response).get('message').split(': ')[-1]
        if server_id in counts:
            counts[server_id] += 1
        else:
            counts[server_id] = 1
    return counts

def plot_bar_chart(data, title):
    plt.bar(data.keys(), data.values())
    plt.xlabel('Server ID')
    plt.ylabel('Number of Requests')
    plt.title(title)
    plt.show()

async def run_experiment(num_requests):
    responses = await launch_requests(num_requests)
    counts = count_responses(responses)
    print(f'Server request counts: {counts}')
    plot_bar_chart(counts, 'Request Distribution among Servers')

def main():
    num_requests = 10000
    asyncio.run(run_experiment(num_requests))

if __name__ == '__main__':
    main()
