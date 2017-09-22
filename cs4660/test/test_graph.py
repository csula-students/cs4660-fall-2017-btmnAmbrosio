"""test_graph tests the graph implementation"""

import unittest

from graph import graph

class TestNode(unittest.TestCase):
    """TestNode tests node implementation"""
    def test_node_comparison(self):
        """Test node comparison"""
        self.assertEqual(graph.Node(1), graph.Node(1))
class TestEdge(unittest.TestCase):
    """TestEdge tests edge implementation"""
    def test_edge_comparison(self):
        """Test edge comparison"""
        self.assertEqual(
            graph.Edge(graph.Node(1), graph.Node(2), 1),
            graph.Edge(graph.Node(1), graph.Node(2), 1)
        )

class TestAdjacencyList(unittest.TestCase):
    """Tests adjacency list implementation"""
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1 = graph.construct_graph_from_file(graph.AdjacencyList(), graph_1_path)
        self.graph_2 = graph.construct_graph_from_file(graph.AdjacencyList(), graph_2_path)

    def test_adjacent(self):
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(1), graph.Node(2)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(3), graph.Node(6)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(3), graph.Node(10)))

        self.assertEqual(False, self.graph_1.adjacent(graph.Node(1), graph.Node(6)))
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(4), graph.Node(9)))

        self.assertEqual(True, self.graph_2.adjacent(graph.Node(1), graph.Node(2)))
        self.assertEqual(True, self.graph_2.adjacent(graph.Node(4), graph.Node(5)))

        self.assertEqual(False, self.graph_2.adjacent(graph.Node(1), graph.Node(5)))

    def test_neighbors(self):
        self.assertEqual([graph.Node(2), graph.Node(3)], self.graph_1.neighbors(graph.Node(1)))
        self.assertEqual([graph.Node(5), graph.Node(7)], self.graph_1.neighbors(graph.Node(4)))
        self.assertEqual([graph.Node(0)], self.graph_1.neighbors(graph.Node(5)))
        self.assertEqual([], self.graph_1.neighbors(graph.Node(8)))

        self.assertEqual([graph.Node(1), graph.Node(3), graph.Node(6)], self.graph_2.neighbors(graph.Node(0)))
        self.assertEqual([], self.graph_2.neighbors(graph.Node(5)))

    def test_add_node(self):
        self.assertEqual(False, self.graph_1.add_node(graph.Node(1)))
        self.assertEqual(False, self.graph_1.add_node(graph.Node(6)))

        self.assertEqual(True, self.graph_1.add_node(graph.Node(11)))

    def test_remove_node(self):
        self.assertEqual(True, self.graph_1.remove_node(graph.Node(6)))
        # check if the node is removed and neighbors of 9 is also removed
        self.assertEqual([], self.graph_1.neighbors(graph.Node(9)))
        # Removing a node that doens't exist in the graph should return false as noop
        self.assertEqual(False, self.graph_1.remove_node(graph.Node(1234)))

    def test_add_edge(self):
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(1), graph.Node(4)))

        self.assertEqual(True, self.graph_1.add_edge(graph.Edge(graph.Node(1), graph.Node(4), 1)))
        self.assertEqual([graph.Node(2),graph.Node(3),graph.Node(4)], self.graph_1.neighbors(graph.Node(1)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(1), graph.Node(4)))

        # When adding edge that already existed, should return false
        self.assertEqual(False, self.graph_1.add_edge(graph.Edge(graph.Node(1), graph.Node(2), 1)))


    def test_remove_edge(self):
        # removing edges that doesn't exist should return false
        self.assertEqual(False, self.graph_1.remove_edge(graph.Edge(graph.Node(1), graph.Node(6), 1)))
        self.assertEqual(True, self.graph_1.remove_edge(graph.Edge(graph.Node(6), graph.Node(5), 1)))
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(6), graph.Node(5)))

class TestAdjacencyMatrix(unittest.TestCase):
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1 = graph.construct_graph_from_file(graph.AdjacencyMatrix(), graph_1_path)
        self.graph_2 = graph.construct_graph_from_file(graph.AdjacencyMatrix(), graph_2_path)

    def test_adjacent(self):
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(1), graph.Node(2)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(3), graph.Node(6)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(3), graph.Node(10)))

        self.assertEqual(False, self.graph_1.adjacent(graph.Node(1), graph.Node(6)))
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(4), graph.Node(9)))

        self.assertEqual(True, self.graph_2.adjacent(graph.Node(1), graph.Node(2)))
        self.assertEqual(True, self.graph_2.adjacent(graph.Node(4), graph.Node(5)))

        self.assertEqual(False, self.graph_2.adjacent(graph.Node(1), graph.Node(5)))

    def test_neighbors(self):
        self.assertEqual([graph.Node(2), graph.Node(3)], self.graph_1.neighbors(graph.Node(1)))
        self.assertEqual([graph.Node(5), graph.Node(7)], self.graph_1.neighbors(graph.Node(4)))
        self.assertEqual([graph.Node(0)], self.graph_1.neighbors(graph.Node(5)))
        self.assertEqual([], self.graph_1.neighbors(graph.Node(8)))

        self.assertEqual([graph.Node(1), graph.Node(3), graph.Node(6)], self.graph_2.neighbors(graph.Node(0)))
        self.assertEqual([], self.graph_2.neighbors(graph.Node(5)))

    def test_add_node(self):
        self.assertEqual(False, self.graph_1.add_node(graph.Node(1)))
        self.assertEqual(False, self.graph_1.add_node(graph.Node(6)))

        self.assertEqual(True, self.graph_1.add_node(graph.Node(11)))

    def test_remove_node(self):
        self.assertEqual(True, self.graph_1.remove_node(graph.Node(6)))
        # check if the node is removed and neighbors of 9 is also removed
        self.assertEqual([], self.graph_1.neighbors(graph.Node(9)))
        # Removing a node that doens't exist in the graph should return false as noop
        self.assertEqual(False, self.graph_1.remove_node(graph.Node(1234)))

    def test_add_edge(self):
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(1), graph.Node(4)))

        self.assertEqual(True, self.graph_1.add_edge(graph.Edge(graph.Node(1), graph.Node(4), 1)))
        self.assertEqual([graph.Node(2),graph.Node(3),graph.Node(4)], self.graph_1.neighbors(graph.Node(1)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(1), graph.Node(4)))

        # When adding edge that already existed, should return false
        self.assertEqual(False, self.graph_1.add_edge(graph.Edge(graph.Node(1), graph.Node(2), 1)))


    def test_remove_edge(self):
        # removing edges that doesn't exist should return false
        self.assertEqual(False, self.graph_1.remove_edge(graph.Edge(graph.Node(1), graph.Node(6), 1)))
        self.assertEqual(True, self.graph_1.remove_edge(graph.Edge(graph.Node(6), graph.Node(5), 1)))
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(6), graph.Node(5)))

class TestObjectOriented(unittest.TestCase):
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1 = graph.construct_graph_from_file(graph.ObjectOriented(), graph_1_path)
        self.graph_2 = graph.construct_graph_from_file(graph.ObjectOriented(), graph_2_path)

    def test_adjacent(self):
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(1), graph.Node(2)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(3), graph.Node(6)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(3), graph.Node(10)))

        self.assertEqual(False, self.graph_1.adjacent(graph.Node(1), graph.Node(6)))
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(4), graph.Node(9)))

        self.assertEqual(True, self.graph_2.adjacent(graph.Node(1), graph.Node(2)))
        self.assertEqual(True, self.graph_2.adjacent(graph.Node(4), graph.Node(5)))

        self.assertEqual(False, self.graph_2.adjacent(graph.Node(1), graph.Node(5)))

    def test_neighbors(self):
        self.assertEqual([graph.Node(2), graph.Node(3)], self.graph_1.neighbors(graph.Node(1)))
        self.assertEqual([graph.Node(5), graph.Node(7)], self.graph_1.neighbors(graph.Node(4)))
        self.assertEqual([graph.Node(0)], self.graph_1.neighbors(graph.Node(5)))
        self.assertEqual([], self.graph_1.neighbors(graph.Node(8)))

        self.assertEqual([graph.Node(1), graph.Node(3), graph.Node(6)], self.graph_2.neighbors(graph.Node(0)))
        self.assertEqual([], self.graph_2.neighbors(graph.Node(5)))

    def test_add_node(self):
        self.assertEqual(False, self.graph_1.add_node(graph.Node(1)))
        self.assertEqual(False, self.graph_1.add_node(graph.Node(6)))

        self.assertEqual(True, self.graph_1.add_node(graph.Node(11)))

    def test_remove_node(self):
        self.assertEqual(True, self.graph_1.remove_node(graph.Node(6)))
        # check if the node is removed and neighbors of 9 is also removed
        self.assertEqual([], self.graph_1.neighbors(graph.Node(9)))
        # Removing a node that doens't exist in the graph should return false as noop
        self.assertEqual(False, self.graph_1.remove_node(graph.Node(1234)))

    def test_add_edge(self):
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(1), graph.Node(4)))

        self.assertEqual(True, self.graph_1.add_edge(graph.Edge(graph.Node(1), graph.Node(4), 1)))
        self.assertEqual([graph.Node(2),graph.Node(3),graph.Node(4)], self.graph_1.neighbors(graph.Node(1)))
        self.assertEqual(True, self.graph_1.adjacent(graph.Node(1), graph.Node(4)))

        # When adding edge that already existed, should return false
        self.assertEqual(False, self.graph_1.add_edge(graph.Edge(graph.Node(1), graph.Node(2), 1)))


    def test_remove_edge(self):
        # removing edges that doesn't exist should return false
        self.assertEqual(False, self.graph_1.remove_edge(graph.Edge(graph.Node(1), graph.Node(6), 1)))
        self.assertEqual(True, self.graph_1.remove_edge(graph.Edge(graph.Node(6), graph.Node(5), 1)))
        self.assertEqual(False, self.graph_1.adjacent(graph.Node(6), graph.Node(5)))
