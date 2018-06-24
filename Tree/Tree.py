class Tree:
    '''abstract base class for general trees'''
    class Position:
        __slots__ = "_container", "_node"
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            raise ValueError("must be implemented by a subclass")
        
        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node
        
        def __ne__(self, other):
            return self != other
    
    def is_empty(self):
        raise ValueError("must be implemented by a subclass")
    
    def root(self):
        raise ValueError("must be implemented by a subclass")
    
    def is_root(self, p):
        raise ValueError("must be implemented by a subclass")
    
    def is_leaf(self, p):
        raise ValueError("must be implemented by a subclass")
    
    def parent(self, p):
        raise ValueError("must be implemented by a subclass")
    
    def children(self, p):
        raise ValueError("must be implemented by a subclass")
    
    def positions(self):
        raise ValueError("must be implemented by a subclass")
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    
    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max([self.depth(x) for x in self.children(p)])
