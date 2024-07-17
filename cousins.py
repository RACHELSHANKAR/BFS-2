class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_cousins(root, x, y):
    def dfs(node, parent, depth):
        if not node:
            return
        
        if node.val == x:
            nonlocal x_parent, x_depth
            x_parent, x_depth = parent, depth
        elif node.val == y:
            nonlocal y_parent, y_depth
            y_parent, y_depth = parent, depth
        
        dfs(node.left, node, depth + 1)
        dfs(node.right, node, depth + 1)
    
    x_parent = y_parent = None
    x_depth = y_depth = -1
    
    dfs(root, None, 0)
    
    return x_depth == y_depth and x_parent != y_parent

# Example usage
# Constructing a binary tree:
#     1
#   /   \
#  2     3
# / \   /
#4   5 6
#
# Check if 5 and 6 are cousins (they are not)
# Check if 4 and 6 are cousins (they are)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(are_cousins(root, 5, 6))  # Output: False
print(are_cousins(root, 4, 6))  # Output: True

#time = O(N) N is the number of nodes in the tree.
#space = O(H) H is the height of the tree.