import sys
sys.path.append("../PriorityQueue")
from AdaptableHeapPriorityQueue import *
from AdjMapGraph import *

def MST_kruskal(G):
    tree = []
    header = {} #key:each vertex   value:the header vertex of the tree it belongs to
    small_tree = {} #key: a header vertex;   value:a list of all vertices in this tree
    pq = AdaptableHeapPriorityQueue()
    for edge in G.edges():
        pq.add(edge.element(), edge)
    for v in G.vertices():
        header[v] = v
        small_tree[v] = [v]
    while len(tree) < G.vertex_count() - 1:
        edge = pq.remove_min()[1]
        u, v = edge.endpoints()
        if header[u] is not header[v]:
            tree.append(edge)
            header_u, header_v = header[u], header[v]
            for vertex in small_tree[header_u]:
                header[vertex] = header_v
                small_tree[header_v].append(vertex)
            del small_tree[header_u]
        else:
            print("invalid edge:({}, {})".format(u.element(), v.element()))
    return tree

if __name__ == "__main__":
    # construct graph
    G = Graph(is_directed=False)  # undirected graph
    vertices = []
    for i in range(1, 6):
        vertices.append(G.insert_vertex(i))
    edges = [(1, 2, 2), (1, 3, 3), (1, 4, 6), (2, 3, 3), (2, 4, 3), (2, 5, 3), (3, 4, 2), (4, 5, 5)]
    for i1, i2, i3 in edges:
        u, v = vertices[i1 - 1], vertices[i2 - 1]
        G.insert_edge(u, v, i3)
    tree = MST_kruskal(G)
    for e in tree:
        print("edge:", [x.element() for x in e.endpoints()])