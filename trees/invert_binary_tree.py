# Given the root of a binary tree, invert the tree, and return its root.
# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def invert(node):
            if not node:
                return
            
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)
            
        
        invert(root)
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

s = Solution()
s.invertTree(root)
