
'''
1.consostent hashing
https://www.youtube.com/watch?v=--4UgUPCuFM
https://www.youtube.com/watch?v=0X2PDMFLflY
https://www.youtube.com/watch?v=4IPE0UvmeG0
https://www.youtube.com/watch?v=jznJKL0CrxM
https://www.toptal.com/big-data/consistent-hashing
https://ihong5.wordpress.com/2014/08/19/consistent-hashing-algorithm/
http://www.tom-e-white.com/2007/11/consistent-hashing.html

To find a node for an object (the get method), the hash value of the object is used to look in the map. Most of the time there will not be a node stored at this hash value (since the hash value space is typically much larger than the number of nodes, even with replicas), so the next node is found by looking for the first key in the tail map. If the tail map is empty then we wrap around the circle by getting the first key in the circle.

https://gist.github.com/reorx/8470123
'''

from hashlib import md5
from bisect import bisect


class Ring(object):

    def __init__(self, server_list, num_replicas=3):
        nodes = self.generate_nodes(server_list, num_replicas)
        hnodes = [self.hash(node) for node in nodes]
        hnodes.sort()

        self.num_replicas = num_replicas
        self.nodes = nodes
        self.hnodes = hnodes
        # this will store map of Hash(Node) => Name of Server(nodes.append("{0}-{1}".format(i, server)))
        self.nodes_map = {self.hash(node): node.split("-")[1] for node in nodes}

    @staticmethod
    def hash(val):
        m = md5(val)
        return int(m.hexdigest(), 16)

    @staticmethod
    def generate_nodes(server_list, num_replicas):
        nodes = []
        for i in xrange(num_replicas):
            for server in server_list:
                nodes.append("{0}-{1}".format(i, server))
        return nodes

    def get_node(self, val):
        pos = bisect(self.hnodes, self.hash(val))
        if pos == len(self.hnodes):
            return self.nodes_map[self.hnodes[0]]
        else:
            return self.nodes_map[self.hnodes[pos]]


server_list = ["127.0.0.1", "127.0.0.2", "127.0.0.3"]
ring = Ring(server_list)
print ring.get_node("KNKLn")
print ring.get_node("12213")
print ring.get_node("2434")
print ring.get_node("1")


# Will Print:
# 127.0.0.2
# 127.0.0.2
# 127.0.0.1
# 127.0.0.3