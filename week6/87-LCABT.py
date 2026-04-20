# Lowest Common Ancestor (LCA) in a Binary Tree
# The LCA of two nodes p and q is the lowest node that has both p and q as descendants

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to find LCA
def lowest_common_ancestor(root, p, q):
    
    def dfs(node):
        # Base case: if node is null or matches p or q
        if not node or node == p or node == q:
            return node
        
        # Search in left and right subtree
        left = dfs(node.left)
        right = dfs(node.right)
        
        # If both sides return non-null → this is LCA
        if left and right:
            return node
        
        # Otherwise return the non-null child
        return left if left else right

    return dfs(root)


# ----------- Main Program -----------

# Build the tree manually
#         3
#       /   \
#      5     1
#     / \   / \
#    6   2 0   8
#       / \
#      7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Nodes for which we find LCA
p = root.left          # Node 5
q = root.left.right.right  # Node 4

# Call function
lca = lowest_common_ancestor(root, p, q)
print("Lowest Common Ancestor:", lca.val)