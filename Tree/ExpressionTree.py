from LinkedBinaryTree import LinkedBinaryTree
import sys
sys.path.append(r"..\\")
from LinkedStack import LinkedStack

class ExpressionTree(LinkedBinaryTree):
    '''given an expression, build a binary tree'''
    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise ValueError("parameter must be a string")
        self._add_root(token)
        if left is not None:
            self._attach(self.root(), left, right)

    def inorder(self):
        def inorder_recur(p, results=[]):
            left = self.left(p)
            right = self.right(p)
            if left is not None:
                results.append('(')
                inorder_recur(left, results)
            results.append(p.element())
            if right is not None:
                inorder_recur(right, results)
                results.append(')')
        results = []
        inorder_recur(self.root(), results)
        return "".join(results)

    def __str__(self):
        return self.inorder()

    def evaluate(self):
        def eval_recur(p):
            char = p.element()
            left = self.left(p)
            right = self.right(p)
            if char not in "+-*/":
                return int(p.element())
            elif char == '+':
                return eval_recur(left) + eval_recur(right)
            elif char == '-':
                return eval_recur(left) - eval_recur(right)
            elif char == '*':
                return eval_recur(left) * eval_recur(right)
            elif char == '/':
                return eval_recur(left) / eval_recur(right)
        return eval_recur(self.root())

def make_tree(s):
    stack = LinkedStack()
    for char in s:
        if char in '+-*/':
            stack.push(char)
        elif char == '(':
            continue
        elif char == ')':
            right = stack.pop()
            oper = stack.pop()
            left = stack.pop()
            stack.push(ExpressionTree(oper, left, right))
        else:
            stack.push(ExpressionTree(char))
    while len(stack) != 1:
        right = stack.pop()
        oper = stack.pop()
        left = stack.pop()
        stack.push(ExpressionTree(oper, left, right))
    return stack.pop()

a = make_tree("(((1+2)*3)+4+(1*2))")
print(a)
print(a.evaluate())
