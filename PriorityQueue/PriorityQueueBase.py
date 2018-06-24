class EmptyError(Exception):
    pass

class PriorityQueueBase:
    class _Item:
        __slots__ = "_key", "_value"
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def __le__(self, other):
            return self._key <= other._key

        def __str__(self):
            return "({0}, {1})".format(self._key, self._value)