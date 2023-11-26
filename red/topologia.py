import networkx as nx
import simpy
import random

class NetworkTopology:
    def __init__(self, env, num_nodes):
        self.env = env
        self.num_nodes = num_nodes
        self.graph = self.create_network_topology()

    def create_network_topology(self):
        G = nx.erdos_renyi_graph(n=self.num_nodes, p=0.5)
        for node in G.nodes:
            self.env.process(self.node_communication(node, G))
        return G

    def node_communication(self, name, graph):
        while True:
            print(f"El nodo {name} está transmitiendo")
            yield self.env.timeout(random.randint(1, 5))
