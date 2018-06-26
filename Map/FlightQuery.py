from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expeted period'''
    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"
        def __init__(self, origine, dest, date="", time=""):
            self._origin = origine
            self._dest = dest
            self._date = date
            self._time = time
        
        def __lt__(self, other):
            return self._date < other._date if self._date != other._date else self._time < other._time

        def __eq__(self, other):
            return self._date == other._date and self._time == other._time

        def __str__(self):
            return "{0} {1} {2} {3}".format(self._origin, self._dest, str(self._date), str(self._time))

    def query(self, k1, k2):
        k1, k2 = self.Key(*k1), self.Key(*k2)
        index1 = self._find_index(k1)
        index2 = self._find_index(k2)
        print(index1, index2)
        if index2 < len(self):
            index2 += 1
        for i in range(index1, index2):
            print(self._table[i]._key, ':', self._table[i]._value)


a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3")]
for each in s:
    key = a.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    a[key] = value
print(len(a))

k1 = ("A", "B", 622, 1200)
k2 = ("A", "B", 622, 1300)
a.query(k1, k2)