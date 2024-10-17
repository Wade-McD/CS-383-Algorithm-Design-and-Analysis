from collections import deque

class Node:


    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.left}, {self.key}, {self.right}]'

    def __repr__(self):
        return str(self)



samp_tree = Node('C', Node('F', Node('D')), Node('B', Node('A', Node('G'), Node('E'))))

# Level order, Top down (left to right)
def level_order(t):
    result = []
    if t:
        d = deque()
        d.append(t)
        while len(d):
            n = d.popleft()
            result.append(n.key)
            if n.left:
                d.append(n.left)
            if n.right:
                d.append(n.right)
    return result

# Preorder, Start at root then go through left tree and then right tree
def preorder(t):
    result = []
    def f(n):
        if n:
            result.append(n.key)
            f(n.left)
            f(n.right)
    f(t)
    return result

# Inorder, Read bottom left to right with the root in the middle
def inorder(t):
    result = []
    def f(n):
        if n:
            f(n.left)
            result.append(n.key)
            f(n.right)
    f(t)
    return result

# Postorder, Go through left tree and then the right tree and end at the root
def postorder(t):
    result = []
    def f(n):
        if n:
            f(n.left)
            f(n.right)
            result.append(n.key)
    f(t)
    return result