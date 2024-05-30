import os
import json
import random
import string
import requests
from flask import Flask, request, jsonify
from consistent_hash import ConsistentHashMap

class LoadBalancer:
    def __init__(self, replication_factor=3):
        self.app = Flask(__name__)
        self.consistent_hash = ConsistentHashMap()
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/rep', 'get_replicas', self.get_replicas, methods=['GET'])
        self.app.add_url_rule('/add', 'add_replicas', self.add_replicas, methods=['POST'])
        self.app.add_url_rule('/rm', 'remove_replicas', self.remove_replicas, methods=['DELETE'])
        self.app.add_url_rule('/<path:path>', 'forward_request', self.forward_request, methods=['GET'])

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)

    def get_replicas(self):
        replicas = self.ch.get_all_servers()
        return jsonify({
            "message": {
                "N": len(replicas),
                "replicas": replicas
            },
            "status": "successful"
        }), 200

    def add_replicas(self):
        data = request.get_json()
        num_new_instances = data.get('n')
        hostnames = data.get('hostnames', [])

        if len(hostnames) > num_new_instances:
            return jsonify({"error": "Hostnames list length exceeds the number of instances to be added"}), 400

        new_hostnames = hostnames + [self.random_hostname() for _ in range(num_new_instances - len(hostnames))]

        for hostname in new_hostnames:
            self.ch.add_server(hostname)
            # Launch new Docker container for the server
            os.system(f"docker run -d --name {hostname} -e SERVER_ID={hostname} simple-web-server")

        return jsonify({
            "message": {
                "N": len(self.ch.get_all_servers()),
                "replicas": self.ch.get_all_servers()
            },
            "status": "successful"
        }), 200

    def remove_replicas(self):
        data = request.get_json()
        num_instances_to_remove = data.get('n')
        hostnames = data.get('hostnames', [])

        if len(hostnames) > num_instances_to_remove:
            return jsonify({"error": "Hostnames list length exceeds the number of instances to be removed"}), 400

        all_servers = self.ch.get_all_servers()
        removable_hostnames = hostnames + random.sample([s for s in all_servers if s not in hostnames], num_instances_to_remove - len(hostnames))

        for hostname in removable_hostnames:
            self.ch.remove_server(hostname)
            # Remove Docker container for the server
            os.system(f"docker rm -f {hostname}")

        return jsonify({
            "message": {
                "N": len(self.ch.get_all_servers()),
                "replicas": self.ch.get_all_servers()
            },
            "status": "successful"
        }), 200

    def forward_request(self, path):
        all_servers = self.ch.get_all_servers()
        if not all_servers:
            return jsonify({"error": "No replicas available"}), 503

        target_server = self.ch.get_server(path)
        response = requests.get(f"http://{target_server}:5000/{path}")

        return (response.content, response.status_code, response.headers.items())

    def get_server(self, key):
        return self.ch.get_server(key)

    @staticmethod
    def random_hostname(length=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# if __name__ == '__main__':
#     load_balancer = LoadBalancer()
#     load_balancer.run()
