import sys
sys.path.append("../LinkedBased")
from LinkedQueue import *
from AdjMapGraph import *

def BFS(G, s, discovered):
    Q = LinkedQueue()
    Q.enqueue(s)
    while not Q.is_empty():
        u = Q.dequeue()
        for edge in G.incident_edges(u):
            v = edge.opposite(u)
            if v not in discovered:
                print("visit:", u.element(), v.element())
                discovered[v] = edge
                Q.enqueue(v)

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

    #BFS
    result = {vertices[0] : None}
    BFS(G, vertices[0], result)
    print("DFS visits {0} vertices.".format(len(result)))
