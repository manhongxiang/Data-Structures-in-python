from AdjMapGraph import *
from copy import deepcopy

def transitive_closure(orig_G):
    G = deepcopy(orig_G)
    for vertex in G.vertices():
        for edge in G.incident_edges(vertex, outgoing=False):
            u = edge.opposite(vertex)
            for out_edge in G.incident_edges(vertex, outgoing=True):
                v = out_edge.opposite(vertex)
                if G.get_edge(u, v) is None:
                    print("insert:", u.element(), v.element())
                    G.insert_edge(u, v)
    return G

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
    G_tc = transitive_closure(G)
    print("edge count:", G_tc.edge_count())
    print("vertex count:", G_tc.vertex_count())
    for edge in G.edges():
        u, v  = edge.endpoints()
        print(u.element(), v.element())