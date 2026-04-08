# we solve this by having a queue first we atake a node  and we enter node value to queue and to that node if we have childern we will add those chidldren to the queue
from collections import deque

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function for level-order traversal
def avg_level_order(root):
    if not root:
        return []
    q = deque([root])
    res=[]
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(sum(level)/len(level))
    return res


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
print(avg_level_order(root))