class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# "1(2(4)())(3()())"

root=TreeNode(1,None,TreeNode(2,TreeNode(3)))

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return root
        res=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        
        return res

f=Solution()
f.inorderTraversal(root)




