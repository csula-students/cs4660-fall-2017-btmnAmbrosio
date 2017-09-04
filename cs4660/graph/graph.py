"""graph module defines the knowledge representations files"""

"""
Commonly a Graph would need to have following methods:

* adjacent
* neighbors
* addNode
* removeNode
* addEdge
* removeEdge
* distance
* getNode
"""

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    return graph

class Node(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data

class Edge(object):
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight

class AdjacencyList(object):
    def __init__(self):
        pass

    def adjacent(self, node_1, node_2):
        pass

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

    def distance(self, node_1, node_2):
        pass

    def get_node(self, node_data):
        pass

class AdjacencyMatrix(object):
    def __init__(self):
        pass

    def adjacent(self, node_1, node_2):
        pass

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

    def distance(self, node_1, node_2):
        pass

    def get_node(self, node_data):
        pass

class ObjectOriented(object):
    def __init__(self):
        pass

    def adjacent(self, node_1, node_2):
        pass

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

    def distance(self, node_1, node_2):
        pass

    def get_node(self, node_data):
        pass
