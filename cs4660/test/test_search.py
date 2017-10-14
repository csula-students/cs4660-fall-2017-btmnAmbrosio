"""test_search tests the search implementation in simple graph"""

import unittest
import time

from search import searches
from graph import utils
from graph import graph

class TestBFS(unittest.TestCase):
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_2s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_1s = list(map(construct_graph(graph_1_path), self.graph_1s))
        self.graph_2s = list(map(construct_graph(graph_2_path), self.graph_2s))

    def test_bfs_1(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1),
                    graph.Edge(graph.Node(10), graph.Node(8), 1)
                ],
                searches.bfs(g, graph.Node(1), graph.Node(8))
            )

    def test_bfs_2(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1)
                ],
                searches.bfs(g, graph.Node(1), graph.Node(10))
            )

    def test_bfs_3(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ],
                searches.bfs(g, graph.Node(1), graph.Node(5))
            )

    def test_bfs_4(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(5), 11)
                ],
                searches.bfs(g, graph.Node(0), graph.Node(5))
            )

    def test_bfs_5(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7)
                ],
                searches.bfs(g, graph.Node(0), graph.Node(2))
            )

class TestDFS(unittest.TestCase):
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_2s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_1s = list(map(construct_graph(graph_1_path), self.graph_1s))
        self.graph_2s = list(map(construct_graph(graph_2_path), self.graph_2s))

    def test_dfs_1(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1),
                    graph.Edge(graph.Node(5), graph.Node(0), 1),
                    graph.Edge(graph.Node(0), graph.Node(7), 1),
                    graph.Edge(graph.Node(7), graph.Node(8), 1)
                ],
                searches.dfs(g, graph.Node(1), graph.Node(8))
            )

    def test_dfs_2(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1),
                    graph.Edge(graph.Node(5), graph.Node(0), 1),
                    graph.Edge(graph.Node(0), graph.Node(7), 1),
                    graph.Edge(graph.Node(7), graph.Node(10), 1)
                ],
                searches.dfs(g, graph.Node(1), graph.Node(10))
            )

    def test_dfs_3(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ],
                searches.dfs(g, graph.Node(1), graph.Node(5))
            )

    def test_dfs_4(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7),
                    graph.Edge(graph.Node(2), graph.Node(5), 2)
                ],
                searches.dfs(g, graph.Node(0), graph.Node(5))
            )

    def test_dfs_5(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7)
                ],
                searches.dfs(g, graph.Node(0), graph.Node(2))
            )

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_2s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_1s = list(map(construct_graph(graph_1_path), self.graph_1s))
        self.graph_2s = list(map(construct_graph(graph_2_path), self.graph_2s))

    def test_dijkstra_1(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1),
                    graph.Edge(graph.Node(10), graph.Node(8), 1)
                ],
                searches.dijkstra_search(g, graph.Node(1), graph.Node(8))
            )

    def test_dijkstra_2(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1)
                ],
                searches.dijkstra_search(g, graph.Node(1), graph.Node(10))
            )

    def test_dijkstra_3(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ],
                searches.dijkstra_search(g, graph.Node(1), graph.Node(5))
            )

    def test_dijkstra_4(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 5)
                ],
                searches.dijkstra_search(g, graph.Node(1), graph.Node(5))
            )

    def test_dijkstra_5(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(6), 3),
                    graph.Edge(graph.Node(6), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 5)
                ],
                searches.dijkstra_search(g, graph.Node(0), graph.Node(5))
            )

class TestAStar(unittest.TestCase):
    def setUp(self):
        grid_1_path = './test/fixtures/grid-1.txt'
        grid_2_path = './test/fixtures/grid-2.txt'
        grid_3_path = './test/fixtures/grid-3.txt'
        grid_4_path = './test/fixtures/grid-4.txt'
        grid_5_path = './test/fixtures/grid-5.txt'
        self.graph_1s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_2s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_3s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_1s = list(map(construct_grid_graph(grid_1_path), self.graph_1s))
        self.graph_2s = list(map(construct_grid_graph(grid_2_path), self.graph_2s))
        self.graph_3s = list(map(construct_grid_graph(grid_3_path), self.graph_3s))
        self.graph_4 = utils.parse_grid_file(graph.AdjacencyList(), grid_4_path)
        self.graph_5 = utils.parse_grid_file(graph.AdjacencyList(), grid_5_path)

    def test_a_star_1(self):
        start_time = time.time()
        for g in self.graph_1s:
            self.assertEqual(
                "SSSSE",
                utils.convert_edge_to_grid_actions(
                    searches.a_star_search(
                        g,
                        graph.Node(utils.Tile(3, 0, "@1")),
                        graph.Node(utils.Tile(4, 4, "@6"))
                    )
                )
            )
        print("A_star_1: %.6f seconds" % (time.time() - start_time))

    def test_a_star_2(self):
        start_time = time.time()
        for g in self.graph_2s:
            path = utils.convert_edge_to_grid_actions(
                searches.a_star_search(
                    g,
                    graph.Node(utils.Tile(3, 0, "@1")),
                    graph.Node(utils.Tile(13, 0, "@8"))
                )
            )
            self.assertTrue(string_equal_without_order(path, "SSSSEEEEEEEEEEEEENNWNWNW"))
        print("A_star_2: %.6f seconds" % (time.time() - start_time))

    def test_a_star_3(self):
        start_time = time.time()
        for g in self.graph_3s:
            path = utils.convert_edge_to_grid_actions(
                searches.a_star_search(
                    g,
                    graph.Node(utils.Tile(3, 0, "@1")),
                    graph.Node(utils.Tile(2, 7, "@2"))
                )
            )
            self.assertTrue(string_equal_without_order(path, "SSSSEESESSWWWW"))
        print("A_star_3: %.6f seconds" % (time.time() - start_time))

    def test_a_star_4(self):
        start_time = time.time()
        expected_path = "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSESE"
        path = utils.convert_edge_to_grid_actions(
            searches.a_star_search(
                self.graph_4,
                graph.Node(utils.Tile(4, 0, "@1")),
                graph.Node(utils.Tile(6, 201, "@4"))
            )
        )
        self.assertTrue(string_equal_without_order(path, expected_path))
        print("A_star_4: %.6f seconds" % (time.time() - start_time))

    def test_a_star_5(self):
        start_time = time.time()
        expected_path = "SSSSSSSSSSEESSEESESESSEESSEESESESESESSEESESESESESESSESEESESESSESEESSEESSEESESESESESSESEESSESESEESSESEESESSESEESESESESESSEESESESESESESESESESSEESESESESESESSEESSEESESSESEESSEESESSEESESESESESESSEESESESSEESESSESEESSEESESESESSEESSESEESESSESESESESEESSEESESESESESESESESESESESESESESESSEESESSEESSEESESESESSEESESESSEESESESSEESESESESESESESESESESESESESSESEESSEESESSEESESSEESSEESESSEESESESESESESESESESESSEESEEEESSSSSE"
        path = utils.convert_edge_to_grid_actions(
            searches.a_star_search(
                self.graph_5,
                graph.Node(utils.Tile(4, 0, "@1")),
                graph.Node(utils.Tile(201, 206, "@5"))
            )
        )
        print("A_star_5: %.6f seconds" % (time.time() - start_time))
        self.assertTrue(string_equal_without_order(path, expected_path))

def construct_graph(graph_path):
    """Helper function to construct graph given graph_path"""
    return lambda g: graph.construct_graph_from_file(g, graph_path)

def construct_grid_graph(file_path):
    """Helper function to construct graph given graph_path"""
    return lambda g: utils.parse_grid_file(g, file_path)

def string_equal_without_order(string_1, string_2):
    return ''.join(sorted(string_1)) == ''.join(sorted(string_2))
