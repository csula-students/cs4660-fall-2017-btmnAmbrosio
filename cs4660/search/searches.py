"""
Searches module defines all different search algorithms
"""
import sys
from graph import graph
from queue import Queue
from queue import PriorityQueue
import math


def bfs(graph1, initial_node, dest_node):
    
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
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
            # if the child is not in the nodeList
            if child not in nodeList:
                #then add the child to the nodeList 
                nodeList.append(child)
                # add the distance of the parent node to the current child to the distance list
                distanceList[child]=graph1.distance(currentNode, child)
                #add the currentNode as the parent of the child in the parentList 
                parentList[child]=currentNode
                # add the child to the queue
                nodeQ.put(child)
            # if the child is the destination node
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



def dfs(graph1, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    results = []
    parentsList ={}
    currentBackTraceNode=dest_node

    def DFSstart(current):
       return DFS(current, {initial_node:1})

    def DFS(current, parents):
        
        if current == dest_node:
            return parents

        children = graph1.neighbors(current)
        for child in children:
            if child not in parents:
                parents[child] = current
                DFS(child , parents)

    parentsList = DFSstart(initial_node)
    parentsList[initial_node]=1

    while(parentsList[currentBackTraceNode] != 1):
            # add the edge of the endTile from its parent to the results list
            results.append(graph.Edge(parentsList[currentBackTraceNode], currentBackTraceNode, graph1.distance(parentsList[currentBackTraceNode],currentBackTraceNode)))
            # set the endTile to the parent of the current endTile 
            currentBackTraceNode=parentsList[currentBackTraceNode]
    # reverse the results the return
    results.reverse()
    return results

def dijkstra_search(graph1, initial_node, dest_node):

    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
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
            return self.priority < other.priority


    distanceList={}
    parentList={}
    distanceList[initial_node]=0
    nodeList=[]
    destinationFound=False
    nodePriorityQ= PriorityQueue()
    endTile=None
    results=[]
    children=[]

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
    
    # while the priority queue is not empty
    while  not nodePriorityQ.empty():
        # A "priority node" which has the lowest priority value is removed from the priority queue
        # and set to the variable current_node_holder.
        current_node_holder = nodePriorityQ.get()
        # get all of the currentNode's neighbors or children
        children = graph1.neighbors(current_node_holder.node)
        #for each of the currentNode's "children"
        for child in children:
            # if the current child is not in the nodeList
            if child not in nodeList:
                #set its value in distanceList to "infinity" 
                distanceList[child]=float('inf')
                # add the node to the list of known nodes
                nodeList.append(child)
            # set variable alt, equal to the distance from the currentNode and the current child of that node
            # plus the distance from the initial_node to the current node
            alt=distanceList[current_node_holder.node]+graph1.distance(current_node_holder.node, child)
            #if the variable alt is smaller the distance of current child from the initial node 
            if alt < distanceList[child]:
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

    
    # feel free to ignore this
    #     for child in children:
    #         if child not in nodeList:
    #             nodeList.append(child)
    #             distanceList[child]=graph1.distance(current_node_holder.node, child)
    #             parentList[child]=current_node_holder.node
    #             nodePriorityQ.put(PriorityNode(distanceList[child],child))
    #         if child==dest_node:
    #             destinationFound=True
    #             endTile = child


    #if the destination is found 
    if destinationFound:
        #while the parent of endTile is not None. Note: The first endTile is the destination node
        while(parentList[endTile] is not None):
            # add the edge of the endTile from its parent to the results list
            results.append(graph.Edge(parentList[endTile], endTile, graph1.distance(parentList[endTile],endTile)))
            # set the endTile to the parent of the current endTile 
            endTile=parentList[endTile]
        # reverse the results the return
        results.reverse()
        return results
    # the destination was not found so return -1 
    else:
        return -1

def a_star_search(graph1, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
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
            return self.priority < other.priority


    nodePriorityQ = PriorityQueue()
    parentList={}
    distanceList={}
    neighborsList=[]
    results=[]
    destinationFound=False
    
    # add the distance to get to the initial_node, which is 0 to the distanceList
    distanceList[initial_node]=0
    #Since the initial_node has no parent set its value in parentList is None 
    parentList[initial_node]=None
    # create the "priority node" which is a class containing a node and its priority 
    pNode = PriorityNode(distanceList[initial_node],initial_node)
    
    # while the priority queue is not empty
    while  not nodePriorityQ.empty():
        # A "priority node" which has the lowest priority value is removed from the priority queue
        # and set to the variable current_node_holder.
        current_node_holder = nodePriorityQ.get()
        currentNode=current_node_holder.node

        # if the current node is equal to the destination node
        if currentNode == dest_node:
            destinationFound=True
            break

        neighborsList=graph1.neighbors(currentNode)

        for neighbor in neighborsList:
            newCost = distanceList[currentNode] + graph1.distance(currentNode, neighbor)
            if neighbor not in distanceList or newCost < distanceList[neighbor]:
                distanceList[neighbor] = newCost
                priority = newCost 
                nodePriorityQ.put(PriorityNode(priority, neighbor))
                parentList[neighbor] = currentNode


    #if the destination is found 
    if destinationFound:
        endTile=dest_node
        #while the parent of endTile is not None. Note: The first endTile is the destination node
        while(parentList[endTile] is not None):
            # add the edge of the endTile from its parent to the results list
            results.append(graph.Edge(parentList[endTile], endTile, graph1.distance(parentList[endTile],endTile)))
            # set the endTile to the parent of the current endTile 
            endTile=parentList[endTile]
        # reverse the results the return
        results.reverse()
        return results
    # the destination was not found so return -1 
    else:
        return -1