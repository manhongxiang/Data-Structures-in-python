from EulerTour import EulerTour

class BinaryEulerTour(EulerTour):
    def execute(self):
        def recur(p, depth=0, path=[]):
            self._previsit(p)
            if p.left():
                path.append(0)
                recur(p.left(), depth + 1, path)
                path.pop()
            self._inorder_visit(p, depth, path)
            if p.right():
                path.append(1)
                recur(p.right(), depth + 1, path)
                path.pop()
            self._postvisit(p, depth + 1, path)
        recur(self._tree.root())

    def _inorder_visit(self, p, depth, path):
        pass