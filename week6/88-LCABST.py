# Lowest Common Ancestor (LCA) in a Binary Search Tree
# In BST: left < root < right
# We use this property to find LCA efficiently

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to find LCA in BST
def lowest_common_ancestor(root, p, q):
    
    current = root
    
    while current:
        # If both nodes are smaller → go left
        if p.val < current.val and q.val < current.val:
            current = current.left
        
        # If both nodes are greater → go right
        elif p.val > current.val and q.val > current.val:
            current = current.right
        
        # Otherwise, this is the split point → LCA
        else:
            return current


# ----------- Main Program -----------

# Build the BST manually
#         6
#       /   \
#      2     8
#     / \   / \
#    0   4 7   9
#       / \
#      3   5

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# Nodes for which we find LCA
p = root.left        # Node 2
q = root.left.right  # Node 4

# Call function
lca = lowest_common_ancestor(root, p, q)
print("Lowest Common Ancestor:", lca.val)