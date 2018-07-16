from AdjMapGraph import *

def DFS(G, s, discovered):
    '''given an initial empty dict "discovered", map each vertex with the edge that discovered the vertex'''
    for edge in G.incident_edges(s, outgoing=True):
        v = edge.opposite(s)
        if v not in discovered:
            print("visit:", s.element(), v.element())
            discovered[v] = edge
            DFS(G, v, discovered)

def construct_path(u, v, discovered):
    '''based on discovered, construct a path from u to v'''
    path = []
    cur = v
    while cur is not u and discovered.get(cur) is not None:
        if cur in discovered:
            path.append(cur)
            e = discovered[cur]
            if e is not None:
                cur = e.opposite(cur)
    if cur is u:
        path.append(u)
        return reversed(path)
    else:
        return None

def DFS_comlete(G):
    forest = {}
    for v in G.vertices():
        if v not in forest:
            forest[v] = None
            DFS(G, v, forest)
    return forest

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

    #DFS
    result = {vertices[0] : None}
    DFS(G, vertices[0], result)
    print("DFS visits {0} vertices.".format(len(result)))
    #print path
    orig, dest =  vertices[0], vertices[4]
    path = construct_path(orig, dest, result)
    if path is not None:
        print("path:", " -> ".join([str(x.element()) for x in path]))
    else:
        print("no path from {0} to {1}".format(str(orig.element()), str(dest.element())))

    #DFS_complete
    print("-------------DFS_complete-----------")
    complete_result = DFS_comlete(G)
    print("DFS_complete visits {0} vertices.".format(len(complete_result)))