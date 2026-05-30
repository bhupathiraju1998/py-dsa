# All Nodes Distance K from Target
from collections import deque
# Define tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------- Main Program -----------


def nodes_at_distance_k(root, target, k):
    parent = {}
    def build_parent(node,par):
        if not node:
            return 
        parent[node] = par
        build_parent(node.left,node)
        build_parent(node.right,node)


    build_parent(root,None)

    deq = deque([(target,0)])
    visited  = set([target])
    result = []

    while deq:
        current_node, current_distance = deq.popleft()

        if current_distance == k:
            result.append(current_node.val)
            continue

        for neighbour in [
            current_node.left,
            current_node.right,
            parent.get(current_node)
        ]:
            if neighbour and neighbour not in visited:
                visited.add(neighbour)
                deq.append((neighbour, current_distance + 1))
    return result

# Build the tree manually
#         3
#       /   \
#      5     1
#     / \   / \
#    6   2 0   8
#       / \
#      7   4

root = TreeNode(3)
root.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
root.right = TreeNode(1, TreeNode(0), TreeNode(8))

target = root.left   # node with value 5
k = 2


# Call your function
print(nodes_at_distance_k(root, target, k))