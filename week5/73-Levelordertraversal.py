# we solve this by having a queue first we atake a node  and we enter node value to queue and to that node if we have childern we will add those chidldren to the queue
from collections import deque

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function for level-order traversal
def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result #level order traversal
    #return result[::-1] #level order traversal bottom


# ----------- Example Usage -----------

# Build a sample tree:
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# Perform level order traversal
print(level_order(root))