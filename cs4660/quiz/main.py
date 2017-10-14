"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs
import math
from queue import Queue
from queue import PriorityQueue

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    print(empty_room)
    print("--------------")
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))


    class Node(object):
        """Node represents basic unit of graph"""
        def __init__(self, id, x, y,neighbors):
            self.id = id
            self.x = x
            self.y = y
            self.neighbors= neighbors

        def __str__(self):
            return 'Node({})'.format(self.id)
        def __repr__(self):
            return 'Node({})'.format(self.id)

        def __eq__(self, other_node):
            return self.x == other_node.x and self.y == other_node.y and self.id == other_node.id
        def __ne__(self, other):
            return not self.__eq__(other)

        def __hash__(self):
            return hash(str(self.x) + "," + str(self.y) + "," + str(self.id))

    class Edge(object):
        """Edge represents basic unit of graph connecting between two edges"""
        def __init__(self, from_node, to_node):
            self.from_node = from_node
            self.to_node = to_node
            self.weight = math.sqrt((edge.from_node.x - edge.to_node.x)**2 + (edge.from_node.y - edge.to_node.y)**2)
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
            for neighbor in node.neighbors:
                neighborsList.append[Node(node["id"],node["location"]["x"],node["location"]["y"],node["neighbors"])]


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

        def distance(self, node_1, node_2):
            for edge in self.edges:
                if edge.from_node==node_1 and edge.to_node==node_2:
                    return math.sqrt((edge.from_node.x - edge.to_node.x)**2 + (edge.from_node.y - edge.to_node.y)**2)

    # def weight

    def bfs(graph1, initial_node, dest_node):

        graph1.add_node(initial_node)

        destinationFound=False
        distanceList={}
        parentList={}
        nodeList=[]
        results=[]
        endTile=None
    
        #initialize queue 
        nodeQ= Queue()
    
        #add initial_node to list of known nodes (nodeList) 
        nodeList.append(initial_node)
        # add the distance to get to the initial_node which is 0 to the distanceList
        distanceList[initial_node]=0
        #Since the initial_node has no parent set its value in parentList to None 
        parentList[initial_node]=None 
        #add initial node to queue 
        nodeQ.put(initial_node)

        #while the queue is not empty and the destination is not found  
        while ( not nodeQ.empty() and not destinationFound):
            #get the next number from queue and put it in currentNode 
            currentNode= nodeQ.get()
            # get all of the currentNode's neighbors or children
            children = graph1.neighbors(currentNode)
            #for each of the currentNode's "child"
            for child in children:
                childNeighbors=getState(child["id"])
                childNode=Node(child["id"],child["location"]["x"],child["location"]["y"],childNeighbors)

                # if the child is not in the nodeList
                if childNode not in nodeList:
                    
                    graph1.add_node(childNode)

                    #then add the child to the nodeList 
                    nodeList.append(childNode)
                    # add the distance of the parent node to the current child to the distance list
                    distanceList[childNode]=graph1.distance(currentNode, childNode)
                    #add the currentNode as the parent of the child in the parentList 
                    parentList[childNode]=currentNode
                    # add the child to the queue
                    nodeQ.put(childNode)
                # if the child is the destination node
                if childNode==dest_node:
                    #set variable destinationFound to True in order to get out of while loop 
                    destinationFound=True
                    # set the destination node to endTile
                    endTile = childNode
            
    
        #if the destination is found 
        if destinationFound:
            #while the parent of endTile is not None. Note: The first endTile is the destination node
            while(parentList[endTile] is not None):
                # add the edge of the endTile from its parent to the results list
                results.append(graph.Edge(parentList[endTile], endTile, distanceList[endTile]))
                # set the endTile to the parent of the current endTile 
                endTile=parentList[endTile]
            # reverse the results
            results.reverse()
            #return results 
            return results
        #else return -1 when destination was not found 
        else: 
            return -1

    test_node=Node(empty_room["id"],empty_room["location"]["x"],empty_room["location"]["y"],empty_room["neighbors"])
    print('=============')
    print(test_node.x)
    print(test_node.y)
    print(test_node.id)
    print(test_node.neighbors)
    print('=============')
    print(test_node.neighbors[1])