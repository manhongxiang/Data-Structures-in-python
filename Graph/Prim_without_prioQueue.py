from AdjMapGraph import *
INF = float('inf')

def MST_prim(G):
    tree = {}
    for v in G.vertices():
        tree[v] = None
        break
    for i in range(G.vertex_count() - 1):
        min_v = None
        min_dist = INF
        min_edge = None
        for u in tree:
            for edge in G.incident_edges(u):
                v = edge.opposite(u)
                if v not in tree and edge.element() <= min_dist:
                    min_dist = edge.element()
                    min_v = v
                    min_edge = edge
        if min_v is None:
            print("Graph is not connected")
            return
        tree[min_v] = min_edge
        print("edge added:", [x.element() for x in min_edge.endpoints()])
    return tree

if __name__ == "__main__":
    # construct graph
    G = Graph(is_directed=False)
    vertices = []
    for i in range(1, 6):
        vertices.append(G.insert_vertex(i))
    edges = [(1,2,2), (1,3,3), (1,4,6), (2,4,4), (2,5,3), (3,4,2), (4,5,5)]
    for i1, i2, i3 in edges:
        u, v = vertices[i1 - 1], vertices[i2 - 1]
        G.insert_edge(u, v, i3)
    tree = MST_prim(G)
