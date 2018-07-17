import sys
sys.path.append("../PriorityQueue")
from AdjMapGraph import *
INF = float('inf')

def dijkstra(G, s):
    cloud = {}
    dist = {}
    for v in G.vertices():
        dist[v] = 0 if v is s else INF
    for i in range(len(dist)):
        min_v = None
        min_dist = INF
        for v in G.vertices():
            if v not in cloud and dist[v] <= min_dist:
                min_v = v
                min_dist = dist[v]
        cloud[min_v] = min_dist
        for edge in G.incident_edges(min_v, outgoing=True):
            v = edge.opposite(min_v)
            if min_dist + edge.element() < dist[v]:
                dist[v] = min_dist + edge.element()
    return cloud

def construct_path(G, s, cloud):
    tree = {s : None}
    for u in cloud:
        for edge in G.incident_edges(u):
            v = edge.opposite(u)
            if cloud[u] + edge.element() == cloud[v]:
                tree[v] = edge
    return tree

if __name__ == "__main__":
    #construct graph
    G = Graph(is_directed=True)
    vertices = []
    for i in range(1, 9):
        vertices.append(G.insert_vertex(i))
    edges = [(1,2), (1,3), (1,4), (2,4), (2,5), (3,4), (3,7), (4,5), (6,7), (7,8)]
    for i1, i2 in edges:
        u, v = vertices[i1-1], vertices[i2-1]
        G.insert_edge(u, v, i2)

    source = vertices[0]
    cloud = dijkstra(G, source)
    for v in cloud:
        print(v.element(), cloud[v])

    #build the path from source to dest
    dest = vertices[-1]
    tree = construct_path(G, source, cloud)
    cur = dest
    path = []
    if cloud[dest] == INF:
        print("no path")
    else:
        while cur is not source:
            path.append(cur)
            edge = tree[cur]
            cur = edge.opposite(cur)
        path.append(source)
        print(" -> ".join([str(v.element()) for v in reversed(path)]))