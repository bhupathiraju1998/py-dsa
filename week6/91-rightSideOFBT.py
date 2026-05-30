# All Nodes Distance K from Target
from collections import deque
# Define tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------- Main Program -----------


def rightside_view(root):
    
    res = []
    deq = deque([root])

    while deq:
        level_size = len(deq)
        for i in range(level_size):
            curr_node = deq.popleft()

            if i == level_size -1:
                res.append(curr_node.val)
            if curr_node.left:
                deq.append(curr_node.left)
            if curr_node.right:
                deq.append(curr_node.right)
    return res

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
print(rightside_view(root))