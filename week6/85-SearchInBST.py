# we search for a value in a Binary Search Tree
# if value is smaller → go left, if larger → go right

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to search in BST
def search_bst(root, target):
    
    def dfs(node):
        # If node is null → value not found
        if not node:
            return False
        
        # If value matches → found
        if node.val == target:
            return True
        
        # Go left or right based on BST property
        if target < node.val:
            return dfs(node.left)
        else:
            return dfs(node.right)
    
    return dfs(root)


# ----------- Main Program -----------

# Build the BST manually
#         5
#       /   \
#      3     7
#     / \   / \
#    2   4 6   8

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# Value to search
target = 6

# Call function
print("Is value found in BST?", search_bst(root, target))