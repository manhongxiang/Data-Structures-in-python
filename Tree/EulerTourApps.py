from LinkedTree import *
from EulerTour import *

class PreIndent(EulerTour):
    def _previsit(self, p, depth, path):
        print(' ' * 2 * depth + p.element())

class PreLabel(EulerTour):
    def _previsit(self, p, depth, path):
        print(' ' * 2 * depth + ".".join([str(x + 1) for x in path]), p.element())

class Parenthesize(EulerTour):
    def _previsit(self, p, depth, path):
        if path:
            mark = '(' if path[-1] == 0 else ', '
            print(mark, end='')
        print(p.element(), end='')

    def _postvisit(self, p, depth, path):
        parent = self._tree.parent(p)
        if path and path[-1] == self._tree.num_children(parent) - 1:
            print(')', end='')

if __name__ == "__main__":
    T = LinkedTree()
    root = T._add_root("Electronics R'Us")
    T._add_child(root, "R&D")
    p = T._add_child(root, "Sales")
    T._add_child(p, "Domestic")
    p = T._add_child(p, "International")
    T._add_child(p, "Canada")
    T._add_child(p, "S.America")
    p = T._add_child(p, "Overseas")
    T._add_child(p, "Africa")
    T._add_child(p, "Europe")
    T._add_child(p, "Asia")
    T._add_child(p, "Australia")
    T._add_child(root, "Purchasing")
    p = T._add_child(root, "Manufacturing")
    T._add_child(p, "TV")
    T._add_child(p, "CD")
    T._add_child(p, "Tuner")
    print(len(T))
    a1 = PreIndent(T)
    # a1.execute()
    a2 = PreLabel(T)
    # a2.execute()
    a3 = Parenthesize(T)
    a3.execute()