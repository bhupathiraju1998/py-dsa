# we get largest diameter using the deep left subtree and right subtree
# https://www.youtube.com/watch?v=Rezetez59Nk

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to find diameter
def diameter_of_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Update diameter
        diameter = max(diameter, left_height + right_height)
        
        return 1 + max(left_height, right_height)

    height(root)
    return diameter


# ----------- Main Program -----------

# Build the tree manually
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# Call function
print("Diameter of the tree:", diameter_of_tree(root))