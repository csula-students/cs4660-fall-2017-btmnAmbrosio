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

    # adds nodeNumber amount of nodes to the graph.
    for i in range(nodeNumber):
        newNode= Node(i)
        graph.add_node(newNode)
    
    # adds edges to graph
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
        # if node_1 is in the adjacency_list
        if node_1 in self.adjacency_list:
            # for every edge in the list of edges that belongs to node_1 which is adjacency_list[node_1]
            for currentEdge in self.adjacency_list[node_1]:
                #if node_2 is equal to the to_node in the current edge return true
                if(node_2==currentEdge.to_node):
                    return True
            return False
        return False

    def neighbors(self, node):
        neighborList=[]
        # for every edge (currentEdge) in the list of edges that belongs to node1 (adjacencylist[node_1])
        for currentEdge in self.adjacency_list[node]:
            # add the to_node of the current edge to the neighborList
            neighborList.append(currentEdge.to_node)
        return neighborList

    def add_node(self, node):
        # if node is in the adjacency_list return false
        if node in self.adjacency_list:
            return False
        # otherwise add the node to the adjecency list and return true
        else:
            self.adjacency_list[node]=[]
            return True



    def remove_node(self, node):
        # if node is in the adacency list
        if node in self.adjacency_list:
            # delete the node from the adjacency list
            del self.adjacency_list[node]
            # iterate through (currentNode) in the adjacency list and give us its respective list of edges(edgeList)
            for (currentNode, edgeList) in self.adjacency_list.items():
                # iterate through the current list of edges (edgeList)
                for currentEdge in edgeList:
                    # if the current edge's to_node is equal to the node passed in then remove it
                    if currentEdge.to_node==node:
                        edgeList.remove(currentEdge)
            return True
        # node is not in the adjacency list. return false
        return False

    def add_edge(self, edge):
        # if the from_node belonging to the passed in edge is in the adjacency_list
        if edge.from_node in self.adjacency_list:
            # if the edge already exist in the list of edges 
            # belonging to the from_node's list of edges return false
            if edge in self.adjacency_list[edge.from_node]:
                return False
            # otherwise add the edge to the list of edges 
            # belonging to the edge's from_node and return true
            else:
                self.adjacency_list[edge.from_node].append(edge)
                return True
        # the from_node belonging to the edge is not in the adjacency_list so return false
        return False



    def remove_edge(self, edge):
        # iterate through (currentNode) in the adjacency list and give us its respective list of edges(edgeList)
        for (currentNode, edgeList) in self.adjacency_list.items():
            # if the the current node is equal to the from_node belonging the edge passed in
            if currentNode==edge.from_node:
                # then we iterate through the edges of the edge list belonging to the current node
                for currentEdge in edgeList:
                    # if the current edge in the edge list is wual to
                    #  the edge passed in the we remove it and return trur
                    if edge==currentEdge:
                        edgeList.remove(edge)
                        return True
                # return false since there were no edges matching the one passed in
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
        # if node_1 and node_2 are in the graph's list of nodes
        if node_1 in self.nodes and node_2 in self.nodes:
            # then get the indexes of the respective nodes
            outerIndex=self.__get_node_index(node_1)
            innerIndex=self.__get_node_index(node_2)
            # if the value that belongs to the respective nodes'
            # indexes is bigger than 0 the two nodes are adjacent
            # so, true is returned. Otherwise false is returned
            if self.adjacency_matrix[outerIndex][innerIndex]>0:
                return True
            else:
                return False
        # either one or both nodes passed in is not in the 
        # graph's node list so false is returned 
        return False

    def neighbors(self, node):
        neighborsIndexList=[]
        neighborList=[]
        nodeIndex=self.__get_node_index(node)
        
        # iterate through the list belonging to the node passed in adjacency_matrix[nodeIndex]
        for i in range(0,len(self.adjacency_matrix[nodeIndex])):
            # if the value is greater than 0 then it is a neighbor
            # add it the list of indexes of neighbors (neighborIndexList)
            if self.adjacency_matrix[nodeIndex][i]>0:
                neighborsIndexList.append(i)
        # for each index in neighborsListIndex add the matching node to 
        # the node list (neighborList) the return it
        for neighborIndex in neighborsIndexList:
            neighborList.append(self.nodes[neighborIndex])
        return neighborList

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            # add node to graph's list of nodes 
            self.nodes.append(node)
            # get the index of the node that was added in
            nodeIndex=len(self.nodes)-1
            # add a new array to the matrix
            self.adjacency_matrix.append([])
            # add 0s to the new array that match the length of the others
            for i in range(0,nodeIndex+1):
                self.adjacency_matrix[nodeIndex].append(0)
            # add a 0 to all inner arrays
            for i in range(0,nodeIndex):
                self.adjacency_matrix[i].append(0)
            
            return True

    def remove_node(self, node):
        # if node is in the graph's list of nodes
        if node in self.nodes:
            # save the index of the node that was passed in to nodeIndex
            nodeIndex=self.__get_node_index(node)
            # then remove the node from the list of nodes
            self.nodes.pop(nodeIndex)
            # pop all the values in the graph's adjacency matrix that
            # are in the nodeIndex then return true
            for innerArray in self.adjacency_matrix:
                innerArray.pop(nodeIndex)
            return True
        # the node is not in the graph's node list so return false
        return False


    def add_edge(self, edge):
        # if the from_node and to_node belonging to the edge passed in 
        # is in the list of nodes.
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            # then save the indexes of therespective nodes
            outerIndex=self.__get_node_index(edge.from_node)
            innerIndex=self.__get_node_index(edge.to_node)
            # If the value of the indxes is greater than 0 return false
            # because the edge already exists. 
            if self.adjacency_matrix[outerIndex][innerIndex]>0:
                return False
            # otherswise make value equal to the weight of the edge weight.
            else:
                self.adjacency_matrix[outerIndex][innerIndex]=edge.weight
                return True
        return False


    def remove_edge(self, edge):
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            outerIndex=self.__get_node_index(edge.from_node)
            innerIndex=self.__get_node_index(edge.to_node)
            if self.adjacency_matrix[outerIndex][innerIndex]==edge.weight:
                self.adjacency_matrix[outerIndex][innerIndex]=0
                return True
            return False
        return False

    def __get_node_index(self, node):
        """helper method to find node index"""
        return self.nodes.index(node)

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            for currentEdge in self.edges:
                if currentEdge.from_node==node_1 and currentEdge.to_node==node_2:
                    return True
        return False

    def neighbors(self, node):
        neighborsList = []
        for currentEdge in self.edges:
            if currentEdge.from_node==node:
                neighborsList.append(currentEdge.to_node)
        return neighborsList


    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True

    def remove_node(self, node):
        # if the node is in the graph's list of nodes (self.nodes)
        # remove th node  and remove the edges that have from_node
        # and to_node that mathe the node that was passed in
        if node in self.nodes:
            self.nodes.remove(node)
            for currentEdge in self.edges:
                if currentEdge.from_node==node or currentEdge.to_node==node:
                    self.edges.remove(currentEdge)
            return True
        else:
            return False

    def add_edge(self, edge):
        # if the edge that was passed in is the graph's list of edges (self.edges)
        # return false otherwise add the passed in edge to the graph's list of edges and return true.
        if edge in self.edges:
            return False
        else:
            self.edges.append(edge)
            return True

    def remove_edge(self, edge):
        # if the edge that was passed in is the graph's list of edges (self.edges)
        # remove the edge and return true otherwise return false
        if edge in self.edges:
            self.edges.remove(edge)
            return True
        else:
            return False

