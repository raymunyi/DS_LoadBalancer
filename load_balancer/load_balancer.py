# Load balancer code (load_balancer.py)
import os
import json
import random
import string
import requests
from flask import Flask, request, jsonify
from consistent_hash import ConsistentHashMap

class LoadBalancer:
    def __init__(self, num_containers, num_slots, num_virtual_servers):
        self.app = Flask(__name__)
        self.chm = ConsistentHashMap(num_containers, num_slots, num_virtual_servers)
        self.servers = [f"server{i+1}" for i in range(num_containers)]
        for server in self.servers:
            self.chm.add_server(server)
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/<path:path>', 'forward_request', self.forward_request, methods=['GET'])

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)

    def forward_request(self, path):
        server = self.chm.get_server_for_object(path)
        try:
            response = requests.get(f"http://{server}:5000/{path}", timeout=5)
            return (response.content, response.status_code, response.headers.items())
        except requests.exceptions.RequestException as e:
            return (str(e), 500)

if __name__ == '__main__':
    num_containers = 3
    num_slots = 512
    num_virtual_servers = 20  # K = 20

    load_balancer = LoadBalancer(num_containers, num_slots, num_virtual_servers)
    load_balancer.run()
