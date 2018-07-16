class Graph:
    '''Graph represented in adjacency map'''
    class Edge:
        def __init__(self, origin, destination, weight):
            self._origin = origin
            self._destination = destination
            self._weight = weight

        def element(self):
            return self._element

        def opposite(self, u):
            return self._destination if u is self._origin else self._origin

        def endpoints(self):
            return self._origin, self._destination

        def __hash__(self):
            return hash(id(self))

    class Vertex:
        def __init__(self, element):
            self._element = element

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

    # ----------------------Graph update methods-----------------
    def insert_edge(self, u, v, weight=1):
        edge = self.Edge(u, v, weight)
        self._outgoing[u][v] = self._ingoing[v][u] = edge

    def insert_vertex(self, element):
        vertex = self.Vertex(element)
        self._outgoing[vertex] = {}
        self._ingoing[vertex] = {}
        return vertex

    #-----------------------Graph access methods-----------------
    def __init__(self, is_directed=False):
        self._outgoing = {}
        self._ingoing = {} if is_directed else self._outgoing   #if the graph is directed, _ingoing need to be a new map

    def is_directed(self):
        return self._outgoing is not self._ingoing

    def get_edge(self, u, v):
        # return self._outgoing[u][v] if v in self._outgoing[u] else None   #the get() method of dict can do the same thing, see the following line
        return self._outgoing[u].get(v)

    def edge_count(self):   #Attention! In an undirected graph, the number of all edges in self._outgoing doubles the actural number.
        cnt = 0
        for vertex in self._outgoing:
            cnt += len(self._outgoing[vertex])
        return cnt if self.is_directed() else cnt // 2

    def edges(self):    #Attention!
        edge_set = set()
        for secondary_map in self._outgoing.values():
            for edge in secondary_map.values():
                if edge not in edge_set:
                    edge_set.add(edge)
                    yield edge

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        for vertex in self._outgoing:
            yield vertex

    def degree(self, v, outgoing=True):
        return len(self._outgoing[v]) if outgoing else len(self._ingoing[v])

    def incident_edges(self, v, outgoing=True):
        secondary_map = self._outgoing[v] if outgoing else self._ingoing[v]
        for edge in secondary_map.values():
            yield edge

if __name__ == "__main__":
    a = Graph()
    v1 = a.insert_vertex(1)
    v2 = a.insert_vertex(2)
    v3 = a.insert_vertex(3)
    v4 = a.insert_vertex(4)
    a.insert_edge(v1, v2)
    a.insert_edge(v1, v3)
    a.insert_edge(v1, v4)
    a.insert_edge(v2, v4)
    a.insert_edge(v3, v2)
    a.insert_edge(v3, v4)
    for each in a.vertices():
        print(each)
    print("-----------------")
    for each in a.edges():
        print(each)