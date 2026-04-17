# we collect all root-to-leaf paths whose sum equals target
# similar to path sum 1, but we store the path instead of just checking

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to find all paths
def path_sum_2(root, targetSum):
    result = []

    def dfs(node, current_sum, path):
        if not node:
            return
        
        current_sum += node.val
        path.append(node.val)
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            if current_sum == targetSum:
                result.append(list(path))  # store a copy
        
        # Recur for left and right subtree
        dfs(node.left, current_sum, path)
        dfs(node.right, current_sum, path)
        
        # Backtrack
        path.pop()

    dfs(root, 0, [])
    return result


# ----------- Main Program -----------

# Build the tree manually
#         5
#       /   \
#      4     8
#     /     / \
#    11    13  4
#   /  \       / \
#  7    2     5   1

root = TreeNode(5)
root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root.right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))

# Call function
target = 22
print("All paths with given sum:", path_sum_2(root, target))