# Enter values: 4 2 6 1 3 5 7

from collections import deque

# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insert into BST
def insert(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root


# -------------------------------
# 1. Recursive (DFS)
def balanced_recursive(root):
    if root is None:
        return [True,0]
    
    left,right = balanced_recursive(root.left),balanced_recursive(root.right)
    balanced = (left[0] and  right[0] and abs(left[1] -right[1] ) <= 1)
    return [balanced , 1+ max(left[1],right[1])]
    
# -------------------------------
# -------------------------------
# MAIN PROGRAM

# Build BST
values = [4 ,2, 6, 1, 3, 5, 7]
root = None

for v in values:
    root = insert(root, v)

# Results
print("Balanced(Recursive):", balanced_recursive(root))