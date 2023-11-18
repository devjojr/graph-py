class Node:
    def __init__(self, key):
        self.key = key
        self.incoming_edges = 0
        self.adj_nodes = {}
        self.adj_weights = {}

    def __repr__(self):
        return str(self.key)

    def add_neighbor(self, neighbor, weight=0):
        if neighbor is None or weight is None:
            raise TypeError("neighbor or weight cannot be None")
        neighbor.incoming_edges += 1
        self.adj_nodes[neighbor.key] = neighbor
        self.adj_weights[neighbor.key] = weight

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError("neighbor cannot be None")
        if neighbor.key not in self.adj_nodes:
            raise KeyError("neighbor not found")
        neighbor.incoming_edges -= 1
        del self.adj_nodes[neighbor.key]
        del self.adj_weights[neighbor.key]


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        if key is None:
            raise TypeError("key cannot be None")
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_directed_edge(self, source, destination, weight=0):
        if source is None or destination is None:
            raise TypeError("source or destination cannot be None")
        if source not in self.nodes:
            self.add_node(source)
        if destination not in self.nodes:
            self.add_node(destination)
        self.nodes[source].add_neighbor(self.nodes[destination], weight)

    def add_undirected_edge(self, source, destination, weight=0):
        if source is None or destination is None:
            raise TypeError("source or destination cannot be None")
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def print_graph(self):
        for key in sorted(list(self.nodes.keys())):
            print(str(key) + str(list(self.nodes[key].adj_nodes)))


# graph = Graph()
# for key in range(ord("A"), ord("K")):
#     graph.add_node(chr(key))
# graph.add_directed_edge("A", "D")
# graph.add_directed_edge("A", "J")
# graph.add_directed_edge("B", "D")
# graph.add_directed_edge("B", "C")
# graph.add_directed_edge("C", "A")
# graph.add_directed_edge("C", "E")
# graph.add_directed_edge("C", "I")
# graph.add_directed_edge("D", "A")
# graph.add_directed_edge("D", "E")
# graph.add_directed_edge("D", "G")
# graph.add_directed_edge("D", "H")
# graph.add_directed_edge("E", "C")
# graph.add_directed_edge("E", "H")
# graph.add_directed_edge("F", "A")
# graph.add_directed_edge("F", "I")
# graph.add_directed_edge("G", "I")
# graph.add_directed_edge("G", "J")
# graph.add_directed_edge("G", "F")
# graph.add_directed_edge("H", "E")
# graph.add_directed_edge("I", "H")
# graph.add_directed_edge("I", "C")
# graph.add_directed_edge("J", "E")
# graph.print_graph()
# graph.nodes["D"].remove_neighbor(graph.nodes["E"])
# print("\n")
# graph.print_graph()
