import hashlib

class ConsistentHashMap:
    def __init__(self, num_containers, num_slots, num_virtual_servers):
        self.num_containers = num_containers
        self.num_slots = num_slots
        self.num_virtual_servers = num_virtual_servers
        self.hash_ring = {}  

    def hash_function(self, identifier):
        return (identifier + 2 * identifier + 17**2) % self.num_slots

    def add_server(self, server_id):
        for i in range(self.num_virtual_servers):
            virtual_server_id = f"{server_id}_v{i}"
            position = self.hash_function(hash(virtual_server_id))
            self.hash_ring[position] = server_id

    def get_server_for_object(self, object_id):
        position = self.hash_function(hash(object_id))
        while position not in self.hash_ring:
            position = (position + 1) % self.num_slots
        return self.hash_ring[position]

if __name__ == "__main__":
    num_containers = 3
    num_slots = 512
    num_virtual_servers = 20  # K = 20

    chm = ConsistentHashMap(num_containers, num_slots, num_virtual_servers)
    for container_id in range(num_containers):
        chm.add_server(f"Server_{container_id}")

    # Map objects to servers
    objects = ["Object1", "Object2", "Object3", "Object4"]
    for obj in objects:
        server = chm.get_server_for_object(obj)
        print(f"Object '{obj}' is mapped to server '{server}'")
