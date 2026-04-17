# we check whether one tree is a subtree of another
# subtree means there exists a node in main tree such that
# the subtree starting from that node is identical to given subRoot

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to check if two trees are identical
def is_same_tree(p, q):
    
    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False
    
    return (is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


# Function to check if subRoot is a subtree of root
def is_subtree(root, subRoot):
    
    if not root:
        return False
    
    # If trees match at this node
    if is_same_tree(root, subRoot):
        return True
    
    # Otherwise check left and right subtree
    left_check = is_subtree(root.left, subRoot)
    right_check = is_subtree(root.right, subRoot)
    
    return left_check or right_check


# ----------- Main Program -----------

# Build main tree
#         3
#       /   \
#      4     5
#     / \
#    1   2

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

# Build subtree
#       4
#      / \
#     1   2

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# Call function
print("Is subRoot a subtree of root?", is_subtree(root, subRoot))