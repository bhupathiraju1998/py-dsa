# Enter values: 4 2 6 1 3 5 7
# Max Depth (Recursive): 3
# Max Depth (Level Order): 3
# Max Depth (Iterative DFS): 3

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
def max_depth_recursive(root):
    if root is None:
        return 0
    return 1 + max(max_depth_recursive(root.left),
                   max_depth_recursive(root.right))


# -------------------------------
# 2. Level Order (BFS)
def max_depth_level_order(root):
    if root is None:
        return 0
    
    queue = deque([root])
    depth = 0
        
    while queue:
        size = len(queue)
        
        for _ in range(size):
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        depth += 1
    
    return depth


# -------------------------------
# 3. Iterative (DFS using stack)
def max_depth_iterative(root):
    if root is None:
        return 0
    
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        
        if node:
            max_depth = max(max_depth, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    
    return max_depth


# -------------------------------
# MAIN PROGRAM

# Build BST
values = list(map(int, input("Enter values: ").split()))
root = None

for v in values:
    root = insert(root, v)

# Results
print("Max Depth (Recursive):", max_depth_recursive(root))
print("Max Depth (Level Order):", max_depth_level_order(root))
print("Max Depth (Iterative DFS):", max_depth_iterative(root))