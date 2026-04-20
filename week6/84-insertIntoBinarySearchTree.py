# Binary Search Tree Insertion (Recursive and Iterative)

# Define the structure of a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------- Recursive Insertion --------
def insert_recursive(root, val):
    
    # If tree is empty, create new node
    if not root:
        return TreeNode(val)
    
    # Insert in left subtree
    if val < root.val:
        root.left = insert_recursive(root.left, val)
    
    # Insert in right subtree
    else:
        root.right = insert_recursive(root.right, val)
    
    return root


# -------- Iterative Insertion --------
def insert_iterative(root, val):
    
    new_node = TreeNode(val)
    
    # If tree is empty
    if not root:
        return new_node
    
    current = root
    
    while True:
        
        # Go left
        if val < current.val:
            if not current.left:
                current.left = new_node
                break
            current = current.left
        
        # Go right
        else:
            if not current.right:
                current.right = new_node
                break
            current = current.right
    
    return root


# ----------- Main Program -----------

# Build BST using recursive insert
root = None
values = [5, 3, 7, 2, 4, 6, 8]

for v in values:
    root = insert_recursive(root, v)

print("BST built using recursive insertion.")


# Insert using iterative method
root = insert_iterative(root, 1)
root = insert_iterative(root, 9)

print("Inserted additional nodes using iterative method.")


# Simple inorder traversal to verify BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


print("Inorder Traversal of BST:")
inorder(root)