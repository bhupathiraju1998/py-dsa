# we check whether a binary tree is symmetric (mirror of itself)
# left subtree should be a mirror of right subtree

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to check if tree is symmetric
def is_symmetric(root):
    
    def dfs(left, right):
        # If both nodes are null → symmetric
        if not left and not right:
            return True
        
        # If one is null or values differ → not symmetric
        if not left or not right or left.val != right.val:
            return False
        
        # Check mirror condition
        outer = dfs(left.left, right.right)
        inner = dfs(left.right, right.left)
        
        return outer and inner

    return dfs(root.left, root.right)


# ----------- Main Program -----------

# Build the tree manually
#         1
#       /   \
#      2     2
#     / \   / \
#    3   4 4   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

# Call function
print("Is the tree symmetric?", is_symmetric(root))