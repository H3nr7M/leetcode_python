# Given the root to a binary search tree, find the second largest node in the tree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findSecondLargest(root):
    current = root
    while current:
        if not current.right and current.left:
            return maxValue(current.left)
        if current.right and not current.right.left and not current.right.right:
            return current.val
        current = current.right

def maxValue(node):
    while node.right:
        node = node.right
    return node.val

# Create the binary search tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(13)
root.right.right = Node(20)

# Call the findSecondLargest function
result = findSecondLargest(root)

# Print the result
print("The second largest node in the binary search tree is: ", result)
