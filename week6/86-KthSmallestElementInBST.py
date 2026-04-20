# we find the k-th smallest element in a BST
# using iterative inorder traversal (left → root → right)

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to find k-th smallest element
def kth_smallest(root, k):
    stack = []
    current = root
    
    while True:
        # Reach the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Node at top of stack
        current = stack.pop()
        k -= 1
        
        # If k becomes 0, we found our answer
        if k == 0:
            return current.val
        
        # Move to right subtree
        current = current.right


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

k = 3

# Call function
print(f"{k}-th smallest element is:", kth_smallest(root, k))