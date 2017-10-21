"""
utils package is for some quick utility methods

such as parsing
"""

from graph import graph

class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)



def parse_grid_file(graph1, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """

# C:\Users\joeyr_000\Documents\cs4660_AI\cs4660-fall-2017-btmnAmbrosio\cs4660>pyth
# on -m unittest test.test_search.TestAStar.test_a_star_2

    # TODO: read the filepaht line by line to construct nodes & edges

    # TODO: for each node/edge above, add it to graph

    # graph.Node(utils.Tile(3, 0, "@1")),
    actualx=0
    x1=0
    x2=0
    y=0
    plusCount=0
    edges= []
    nodes = []
    lines=[]

    f = open(file_path, encoding='utf-8')

    for rows in f:
        lines.append(rows)
    
    f.close()

    for rows in lines:

        actualx=0
        x1=1
        x2=2
        if rows[0]=='+':
            plusCount+=1
        if plusCount==2:
            continue
        if rows[0]=="|":

            for i in range(int(len(rows)/2)):

                if (rows[x1] != '#' and rows[x2] !='#') and rows[x1] != '|' and rows[x2] !='|':
                   
                    node=graph.Node(Tile(actualx, y, rows[x1]+rows[x2]))
                    
                    nodes.append(node)

                    if rows[x2+1]!='#' and rows[x2+1]!='|':
                        edges.append(graph.Edge(node,graph.Node(Tile(actualx+1, y, rows[x1+2]+rows[x2+2])),1))
                    if rows[x1-1]!='#' and rows[x1-1]!='|':
                        edges.append(graph.Edge(node,graph.Node(Tile(actualx-1, y, rows[x1-2]+rows[x2-2])),1))
                    if lines[y+1][x1]!='#' and lines[y+1][x1]!='-':
                        edges.append(graph.Edge(node,graph.Node(Tile(actualx, y+1, lines[y+1][x1]+lines[y+1][x2])),1))
                    if lines[y-1][x1]!='#' and lines[y-1][x1]!='-':
                        edges.append(graph.Edge(node,graph.Node(Tile(actualx, y-1, lines[y-1][x1]+lines[y-1][x2])),1))

                    
                x1+=2
                x2+=2
                actualx+=1
        
            y+=1


    for currentNode in nodes:
        graph1.add_node(currentNode)

    for currentEdge in edges:
        graph1.add_edge(currentEdge)
    
    return graph1


def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    actions=''

    for edge in edges:
        if edge.from_node.data.y > edge.to_node.data.y:
            actions+='N'
        if edge.from_node.data.x > edge.to_node.data.x:
            actions+='W'
        if edge.from_node.data.y < edge.to_node.data.y:
            actions+='S'
        else:
            actions+='E'
    return actions

