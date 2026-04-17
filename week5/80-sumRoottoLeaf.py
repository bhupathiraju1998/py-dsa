# we form numbers from root to leaf paths and sum them
# each path acts like a number (e.g., 1->2->3 = 123)

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to find total sum of all root-to-leaf numbers
def sum_root_to_leaf(root):
    
    def dfs(node, current_number):
        if not node:
            return 0
        
        # Form the number
        current_number = current_number * 10 + node.val
        
        # If it's a leaf node, return the number
        if not node.left and not node.right:
            return current_number
        
        # Recur for left and right subtree
        left_sum = dfs(node.left, current_number)
        right_sum = dfs(node.right, current_number)
        
        return left_sum + right_sum

    return dfs(root, 0)


# ----------- Main Program -----------

# Build the tree manually
#         1
#       /   \
#      2     3
# Paths: 12, 13 → Sum = 25

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Call function
print("Sum of root-to-leaf numbers:", sum_root_to_leaf(root))