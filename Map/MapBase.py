class MapBase:
    class _Item:
        __slots__ = "_key", "_value"
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return str(self._key) < str(self._value)

        def __str__(self):
            return "{0} : {1}".format(self._key, self._value)