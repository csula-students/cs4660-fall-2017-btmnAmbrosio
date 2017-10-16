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

    class Node(object):
        """Node represents basic unit of graph"""
        def __init__(self, id, name, neighbors):
            self.id = id
            self.name = name
            self.neighbors= neighbors

        def __str__(self):
            return '{}({})'.format(self.name, self.id )
        def __repr__(self):
            return '{}({})'.format(self.name, self.id )

        def __eq__(self, other_node):
            return self.name == other_node.name  and self.id == other_node.id
        def __ne__(self, other):
            return not self.__eq__(other)

        def __hash__(self):
            return hash( str(self.name) + "," + str(self.id))

    class Edge(object):
        """Edge represents basic unit of graph connecting between two edges"""
        def __init__(self, from_node, to_node):
            self.from_node = from_node
            self.to_node = to_node
            self.weight = transition_state(from_node.id, to_node.id)['event']['effect']
        def __str__(self):
            return '{} : {} :{}'.format(self.from_node, self.to_node, self.weight)
        def __repr__(self):
            return '{} : {} :{}'.format(self.from_node, self.to_node, self.weight)

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
            if not node.neighbors:  
                neighborsList = []
                nodeHolder=get_state(node.id)
                node=Node(nodeHolder["id"],nodeHolder["location"]["name"],nodeHolder["neighbors"])
                for neighbor in node.neighbors:
                    neighborsList.append(Node(neighbor["id"],neighbor["location"]["name"],neighbor["neighbors"]))
                return neighborsList
            return node.neighbors

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
                    return transition_state(node_1.id, node_2.id)['event']['effect']



    def bfs(graph1, initial_node, dest_node):
        destinationFound=False
        distanceList={}
        parentList={}
        nodeList=[]
        results=[]
        endTile=None


        graph1.add_node(initial_node)
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
                # if the child is not in the nodeList
                if child not in nodeList:
                    graph1.add_node(child)
                    # currentEdge=Edge(currentNode,childNode)
                    # graph1.add_edge(currentEdge)
                    #then add the child to the nodeList 
                    nodeList.append(child)
                    # add the distance of the parent node to the current child to the distance list
                    # distanceList[childNode]=currentEdge.weight
                    #add the currentNode as the parent of the child in the parentList 
                    parentList[child]=currentNode
                    # add the child to the queue
                    nodeQ.put(child)
                if child==dest_node:
                    #set variable destinationFound to True in order to get out of while loop 
                    destinationFound=True
                    # set the destination node to endTile
                    endTile = child
            
    
        #if the destination is found 
        if destinationFound:
            #while the parent of endTile is not None. Note: The first endTile is the destination node
            while(parentList[endTile] is not None):
                # add the edge of the endTile from its parent to the results list
                results.append(Edge(parentList[endTile], endTile))
                # set the endTile to the parent of the current endTile 
                endTile=parentList[endTile]
            # reverse the results
            results.reverse()
            #return results 
            return results
        #else return -1 when destination was not found 
        else: 
            return -1



    def dijkstra_search(graph1, initial_node, dest_node):
    
        # This class is used in order to put a node along side its' priority
        # and still get both back when OurPriorityQueue.get(). Also allows to compare node priority. 
        class PriorityNode(object):
            def __init__(self, priority, node):
                self.priority = priority
                self.node = node
            #commented out because doesnt work with python 3. 
            # Keeping just in case it will still works with python 2 
            # def __cmp__(self, other):
            #     return cmp(self.priority, other.priority)

            #campares the priority of this node to the other 
            def __lt__(self, other):
                return self.priority > other.priority


        distanceList={}
        parentList={}
        distanceList[initial_node]=0
        nodeList=[]
        destinationFound=False
        nodePriorityQ= PriorityQueue()
        endTile=None
        results=[]
        children=[]
        visited=[]



        graph1.add_node(initial_node)
        # add the distance to get to the initial_node, which is 0 to the distanceList
        distanceList[initial_node]=0
        #Since the initial_node has no parent set its value in parentList is None 
        parentList[initial_node]=None
        #add initial_node to list of known nodes (nodeList)
        nodeList.append(initial_node)
        # create the "priority node" which is a class containing a node and its priority 
        pNode = PriorityNode(distanceList[initial_node],initial_node)
        # add the "priority node" to the queue 
        nodePriorityQ.put(pNode)

        visited={}
        visited[initial_node]=False
    
        # while the priority queue is not empty
        while  not nodePriorityQ.empty():


            # A "priority node" which has the highest priority value is removed from the priority queue
            # and set to the variable current_node_holder.
            current_node_holder = nodePriorityQ.get()
            if not visited[current_node_holder.node]:
                visited[current_node_holder.node]=True
                # get all of the currentNode's neighbors or children
                children = graph1.neighbors(current_node_holder.node)
            
                #for each of the currentNode's "children"
                for child in children:
                # if the current child is not in the nodeList
                    if child not in nodeList:
                        # print(child)
                        #set its value in distanceList to "infinity" 
                        distanceList[child]=float('-inf')
                    
                        # add the node to the list of known nodes
                        nodeList.append(child)
                        visited[child]=False
                        
                        

                    # set variable alt, equal to the distance from the currentNode and the current child of that node
                    # plus the distance from the initial_node to the current node
                    alt=distanceList[current_node_holder.node]+graph1.distance(current_node_holder.node, child)
    
                    #if the variable alt is greater the distance of current child from the initial node 
                    if alt > distanceList[child] and not visited[child]:
                        # then set value of the child in the distanceList to alt.
                        # This is the current known shortest path from initial node to this node 
                        distanceList[child]=alt
                        # set the parent of this current child as the current node in the parentList
                        parentList[child]=current_node_holder.node
                        # add the current child and its proirity, which is the distance from the initial
                        # node to itself, to the priority queue.
                        nodePriorityQ.put(PriorityNode(distanceList[child],child))
                
                    # if the destination is found set the destinationFound variable to true and 
                    # set the endTile variable  to the destination node
                    if child==dest_node:
                        destinationFound=True
                        endTile=dest_node
                        parentList[endTile]=current_node_holder.node

        #if the destination is found 
        if destinationFound:
            
            #while the parent of endTile is not None. Note: The first endTile is the destination node
            while(parentList[endTile] is not None):
                edge=Edge(parentList[endTile], endTile)
                # add the edge of the endTile from its parent to the results list
                results.append(edge)
                # set the endTile to the parent of the current endTile 
                endTile=parentList[endTile]
            # reverse the results the return
            results.reverse()
            return results
        # the destination was not found so return -1 
        else:
            return -1


    initial = get_state('7f3dc077574c013d98b2de8f735058b4')
    destination = get_state('f1f131f647621a4be7c71292e79613f9')
    initialNode= Node(initial["id"],initial["location"]["name"],initial["neighbors"])
    destinationNode = Node(destination["id"],destination["location"]["name"],destination["neighbors"])

    tempNeighborsList=[]
    for neighbor in initialNode.neighbors:
            tempNeighborsList.append(Node(neighbor["id"],neighbor["location"]["name"],neighbor["neighbors"]))
    initialNode.neighbors=tempNeighborsList
    
    
    bfsHp=0
    print('BFS search in progress')
    results=bfs(ObjectOriented(),initialNode, destinationNode )
    print('BFS search complete')
    for edge in results:
        bfsHp=+edge.weight
    print(results)
    print( "HP : ", bfsHp)

    dijHp=0
    print('Dijkstra search in progress')
    results=dijkstra_search(ObjectOriented(),initialNode, destinationNode )
    print('Dijkstra search complete')
    for edge in results:
        dijHp+=edge.weight
    print(results)
    print( "HP : ", dijHp)