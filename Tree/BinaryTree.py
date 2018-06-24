from Tree import *

class BinaryTree(Tree):
    def parent(self, p):
        raise ValueError("must be implemented by a subclass")

    def left(self, p):
        raise ValueError("must be implemented by a subclass")

    def right(self, p):
        raise ValueError("must be implemented by a subclass")

    def sibling(self, p):
        parent = self.parent(p)
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
    
    def children(self, p):
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)
    

