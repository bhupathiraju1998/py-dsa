# we check if there exists a root-to-leaf path whose sum equals target

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to check path sum
def has_path_sum(root, targetSum):
    
    def dfs(node, current_sum):
        if not node:
            return False
        
        current_sum += node.val
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            return current_sum == targetSum
        
        # Recur for left and right subtree
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)
    
    return dfs(root, 0)


# ----------- Main Program -----------

# Build the tree manually
#         5
#       /   \
#      4     8
#     /     / \
#    11    13  4
#   /  \         \
#  7    2         1

root = TreeNode(5)
root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))

# Call function
target = 22
print("Path Sum exists:", has_path_sum(root, target))