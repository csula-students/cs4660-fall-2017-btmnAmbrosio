"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter



def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that graph object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """


    nodeNumber=0

    fromNode=""
    toNode=""
    edgeWeight=""

    numbers = []
    f = open(file_path, encoding='utf-8')
    for rows in f:
        numbers.append(rows.split())
    f.close()
    nodeNumber=int(itemgetter(0)(numbers[0]))


    for i in range(nodeNumber):
        newNode= Node(i)

        graph.add_node(newNode)
    

    for i in range(1,len(numbers)):
        fromNode,toNode,edgeWeight=numbers[i][0].split(':')
        newEdge= Edge(Node(int(fromNode)),Node(int(toNode)),int(edgeWeight))

        graph.add_edge(newEdge)

    
    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        if node_1 in self.adjacency_list:
            for currentEdge in self.adjacency_list[node_1]:
                if(node_2==currentEdge.to_node):
                    return True
            return False

    def neighbors(self, node):
        neighborList=[]
        for currentEdge in self.adjacency_list[node]:
            neighborList.append(currentEdge.to_node)
        return neighborList

    def add_node(self, node):
        isInAdjacencyList = False

        for currentNode in self.adjacency_list:

            if currentNode==node:
                isInAdjacencyList=True
        


        if isInAdjacencyList:
            return False
        else:
            self.adjacency_list[node] = []
            return True

    def remove_node(self, node):
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for (currentNode, edgeList) in self.adjacency_list.items():
                for currentEdge in edgeList:
                    if currentEdge.to_node==node:
                        edgeList.remove(currentEdge)
            return True
        return False

    def add_edge(self, edge):
        isInAdjacencyList = False
        if len(self.adjacency_list)<1:
            return False

        for (currentNode, edgesList) in self.adjacency_list.items():

            if currentNode==edge.from_node:
             
                for currentEdge in edgesList:
                    if currentEdge == edge:
                        isInAdjacencyList=True
                if isInAdjacencyList:
                    return False
                else:
                    edgesList.append(edge)
                    return True
            
        return False




    def remove_edge(self, edge):
        for (currentNode, edgeList) in self.adjacency_list.items():

            if currentNode==edge.from_node:
                for currentEdge in edgeList:
                    if edge==currentEdge:
                        edgeList.remove(edge)
                        return True
                return False

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

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

    def __get_node_index(self, node):
        """helper method to find node index"""
        pass

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

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

