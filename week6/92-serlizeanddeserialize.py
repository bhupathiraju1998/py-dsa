from collections import deque

# Define tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------- Serialize -----------

def serialize(root):
    def dfs(node):
        if not node:
            return "null,"
        return str(node.val) + "," + dfs(node.left) + dfs(node.right)
    
    return dfs(root)


# ----------- Deserialize -----------

def deserialize(data):
    values = data.split(",")
    i = 0

    def dfs():
        nonlocal i   # ✅ FIX
        
        if values[i] == "null":
            i += 1
            return None
        
        node = TreeNode(int(values[i]))
        i += 1
        node.left = dfs()
        node.right = dfs()
        return node
    
    return dfs()


# ----------- Build Tree -----------

#         3
#       /   \
#      5     1
#     / \   / \
#    6   2 0   8
#       / \
#      7   4

root = TreeNode(3)
root.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
root.right = TreeNode(1, TreeNode(0), TreeNode(8))

target = root.left   # node with value 5
k = 2


# ----------- Test -----------

serialized = serialize(root)
print("Serialized:", serialized)

deserialized_root = deserialize(serialized)

# To verify, serialize again
print("After Deserialize -> Serialize:", serialize(deserialized_root))