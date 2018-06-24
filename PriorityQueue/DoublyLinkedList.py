class EmptyError(Exception):
    pass

class DLList:
    class _Node:
        __slots__ = "_element", "_prev", "_next"
        def __init__(self, element, left, right):
            self._element = element
            self._prev = left
            self._next = right

    def __init__(self):
        self._size = 0
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, preNode, nextNode):
        node = self._Node(element, preNode, nextNode)
        preNode._next = node
        nextNode._prev = node
        self._size += 1
        return node

    def _delete_node(self, node):
        if self.is_empty():
            raise EmptyError("try to delete from an empty list")
        pre, next = node._prev, node._next
        pre._next = next
        next._prev = pre
        node._prev = node._next = None
        self._size -= 1
        return node._element

if __name__ == "__main__":
    a = DLList()
    a._insert_between(1, a._header, a._trailer)
    a._insert_between(2, a._header, a._trailer)
    print(len(a))
