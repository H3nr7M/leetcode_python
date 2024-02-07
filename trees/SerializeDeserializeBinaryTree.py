# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = []
        queue = [self]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        return " ".join(result)

class Codec:
    def serialize(self, root):
        stack = []

        def bfs(node):
            if not node:
                stack.append('null')
                return
                
            stack.append(str(node.val))
            bfs(node.left)
            bfs(node.right)
            

        bfs(root)
        return ','.join(stack)


    def deserialize(self, data):
        if not data:
            return None

        que = deque(data.split(','))
        def bfs():
            if que:
                val = que.popleft()
                if val == 'null':
                    return None
                node = TreeNode(int(val))
                node.left = bfs()
                node.right = bfs()
                return node

        return bfs()

    
if __name__ == "__main__":
    from collections import deque
    root = TreeNode(1, TreeNode(2, TreeNode(6), TreeNode(7)), TreeNode(3, TreeNode(4), TreeNode(5)))
    f = Codec()
    print(f.serialize(root))
    print(f.deserialize(f.serialize(root)))
