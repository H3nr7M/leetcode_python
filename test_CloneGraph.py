class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

# create the original graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# clone the graph
cloned = Solution().cloneGraph(node1)

# check if cloned node has the same val and neighbors as the original node
assert cloned.val == node1.val
assert len(cloned.neighbors) == len(node1.neighbors)

for cloned_nei, orig_nei in zip(cloned.neighbors, node1.neighbors):
    assert cloned_nei.val == orig_nei.val
    assert len(cloned_nei.neighbors) == len(orig_nei.neighbors)

    for cloned_nei_nei, orig_nei_nei in zip(cloned_nei.neighbors, orig_nei.neighbors):
        assert cloned_nei_nei.val == orig_nei_nei.val
