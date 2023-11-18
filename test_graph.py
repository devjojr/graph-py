import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def test_add_node(self):
        graph = Graph()
        node = graph.add_node(1)
        self.assertEqual(node.key, 1)

    def test_add_duplicate_node(self):
        graph = Graph()
        graph.add_node(1)
        node = graph.add_node(1)
        self.assertEqual(node.key, 1)

    def test_add_directed_edge(self):
        graph = Graph()
        graph.add_directed_edge(1, 2, 3)
        self.assertIn(2, graph.nodes[1].adj_nodes)
        self.assertEqual(graph.nodes[1].adj_weights[2], 3)

    def test_add_undirected_edge(self):
        graph = Graph()
        graph.add_undirected_edge(1, 2, 3)
        self.assertIn(2, graph.nodes[1].adj_nodes)
        self.assertIn(1, graph.nodes[2].adj_nodes)
        self.assertEqual(graph.nodes[1].adj_weights[2], 3)
        self.assertEqual(graph.nodes[2].adj_weights[1], 3)

    def test_remove_nonexistent_neighbor(self):
        graph = Graph()
        with self.assertRaises(KeyError):
            graph.nodes[1].remove_neighbor(graph.nodes[2])


if __name__ == "__main__":
    unittest.main()
