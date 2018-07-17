import sys
sys.path.append("../PriorityQueue")
from AdaptableHeapPriorityQueue import *
from AdjMapGraph import *

def topo_ordering(G):
    result = []     #list of vertices in topological order
    locator = {}    #maintain the locators of all vertices for following update
    in_degree = {}  #the in-degree of all vertices. The values keep being updated while removing vertices
    Q = AdaptableHeapPriorityQueue()
    for v in G.vertices():
        in_degree[v] = G.degree(v, False)
        locator[v] = Q.add(in_degree[v], v)
    while not Q.is_empty():
        degree, u = Q.remove_min()
        if degree != 0:
            return
        result.append(u)
        for edge in G.incident_edges(u):
            v = edge.opposite(u)
            in_degree[v] -= 1       #the in-degree of all successive vertices of the removed vertex decreaces by 1( instead of changing the structure of G)
            Q.update(locator[v], in_degree[v], v)
    return result

if __name__ == "__main__":
    #construct graph
    G = Graph(is_directed=True)
    vertices = []
    for i in range(1, 9):
        vertices.append(G.insert_vertex(i))
    edges = [(1,2), (1,3), (1,4), (2,4), (2,5), (3,4), (4,5), (6,7), (7,8)]
    for i1, i2 in edges:
        u, v = vertices[i1-1], vertices[i2-1]
        G.insert_edge(u, v)
    seq = topo_ordering(G)
    print(", ".join([str(x.element()) for x in seq]))