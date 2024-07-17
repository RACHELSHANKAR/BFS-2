from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    print(queue)
    
    while queue:
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            
            # Capture the last node of each level
            if i == level_length - 1:           #for left side view i == 0 and rest of the code remains same
                result.append(node.val)
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Example usage
# Constructing a binary tree:
#     1
#   /   \
#  2     3
#  \    / \
#   5  4   6
#
# Expected right side view: [1, 3, 6]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)

print(right_side_view(root))  # Output: [1, 3, 6]

#time = O(N), N is the number of nodes in the tree
#space = O(N)