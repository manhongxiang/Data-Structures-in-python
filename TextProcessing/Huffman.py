import sys
sys.path.append("../Tree")
sys.path.append("../PriorityQueue")
from LinkedBinaryTree import *
from HeapPriorityQueue import *

class EditableBinaryTree(LinkedBinaryTree):
    def add_root(self, e):
        return self._add_root(e)

    def attach(self, p, t1, t2):
        return self._attach(p, t1, t2)

    def show_code(self):
        '''after the construction of the binary tree, show the code of each character using DFS'''
        def dfs_recur(p, path):
            if self.is_leaf(p):
                print(p.element(), "".join([str(x) for x in path]))
            else:
                if self.left(p) is not None:
                    path.append(0)
                    dfs_recur(self.left(p), path)
                    path.pop()
                if self.right(p) is not None:
                    path.append(1)
                    dfs_recur(self.right(p), path)
                    path.pop()
        if not self.is_empty():
            dfs_recur(self.root(), [])

def huffman(X):
    '''given a string X, create the huffman node of all characters on the basis of their frequency'''
    cnt = {}
    for each in X:  #calculate frequency of each character
        cnt[each] = cnt[each] + 1 if each in cnt else 1
    Q = HeapPriorityQueue()
    for each in cnt:
        t = EditableBinaryTree()
        t.add_root(each)
        Q.add(cnt[each], t)
    while len(Q) > 1:
        k1, t1 = Q.remove_min()
        k2, t2 = Q.remove_min()
        t = EditableBinaryTree()
        root = t.add_root(k1 + k2)
        t.attach(root, t1, t2)
        Q.add(k1 + k2, t)

    k, t = Q.remove_min()
    return t


if __name__ == "__main__":
    s = "abbcccddddeeeeeffffff"
    T = huffman(s)
    T.show_code()