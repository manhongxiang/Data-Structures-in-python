from LinkedTree import *

class EulerTour:
    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        def recur(p, depth=0, path=[]):
            self._previsit(p, depth, path)
            count = 0
            for each in self._tree.children(p):
                path.append(count)
                count += 1
                recur(each, depth + 1, path)
                path.pop()
            self._postvisit(p, depth, path)
        recur(self._tree.root(), 0, [])

    def _previsit(self, p, depth, path):
        # print(p.element())
        pass

    def _postvisit(self, p, depth, path):
        # print(p.element())
        pass

if __name__ == "__main__":
    T = LinkedTree()
    p = T._add_root(1)
    p1 = T._add_child(p, 2)
    T._add_child(p, 3)
    T._add_child(p1, 4)
    T._add_child(p1, 5)
    e = EulerTour(T)
    e.execute()
