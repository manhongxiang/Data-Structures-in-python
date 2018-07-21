import sys
sys.path.append("../PriorityQueue")
from AdaptableHeapPriorityQueue import *
from AdjMapGraph import *

INF = float('inf')

def MST_prim(G):
    tree = {}       #key:each vertex,  value:the edge that discovers the vertex
    d = {}          #key:each vertex,  value:the shortest distance between the vertex to the tree
    locator = {}    #key:each vertex,  value:the locator of the vertex
    pq = AdaptableHeapPriorityQueue()
    for v in G.vertices():
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = INF
        locator[v] = pq.add(d[v], (v, None))
    for i in range(len(d)): #add one vertix to tree in each loop
        dist, v_info = pq.remove_min()
        v, e = v_info
        tree[v] = e
        for edge in G.incident_edges(v):
            u = edge.opposite(v)
            if u not in tree and edge.element() < d[u]:
                d[u] = edge.element()
                loc = locator[u]
                pq.update(loc, d[u], (u, edge))
    return tree

if __name__ == "__main__":
    # construct graph
    G = Graph(is_directed=False)    #undirected graph
    vertices = []
    for i in range(1, 6):
        vertices.append(G.insert_vertex(i))
    edges = [(1, 2, 2), (1, 3, 3), (1, 4, 6), (2, 3, 3), (2, 4, 3), (2, 5, 3), (3, 4, 2), (4, 5, 5)]
    for i1, i2, i3 in edges:
        u, v = vertices[i1 - 1], vertices[i2 - 1]
        G.insert_edge(u, v, i3)
    tree = MST_prim(G)
    for v in tree:
        e = tree[v]
        if e is not None:
            print("edge:", [x.element() for x in e.endpoints()])