# we check whether two binary trees are identical
# trees are same if structure and node values match

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to check if two trees are the same
def is_same_tree(p, q):
    
    def dfs(node1, node2):
        # If both nodes are null, trees match here
        if not node1 and not node2:
            return True
        
        # If one is null or values differ → not same
        if not node1 or not node2 or node1.val != node2.val:
            return False
        
        # Recur for left and right subtree
        left_same = dfs(node1.left, node2.left)
        right_same = dfs(node1.right, node2.right)
        
        return left_same and right_same

    return dfs(p, q)


# ----------- Main Program -----------

# Build first tree
#         1
#       /   \
#      2     3

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Build second tree
#         1
#       /   \
#      2     3

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# Call function
print("Are the two trees the same?", is_same_tree(p, q))