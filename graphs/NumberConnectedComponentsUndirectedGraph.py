# The problem "Number of Connected Components In An Undirected Graph" asks us to find the number of connected components in an undirected graph. We are given an integer n which represents the number of nodes in the graph and a list of edges edges where each edge is represented by a pair of nodes. We need to return the number of connected components in the graph.
# Example 1:
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # DFS function to traverse the graph
        def dfs(node, visited):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        # Initialize counter and visited set
        count = 0
        visited = set()

        # Traverse the graph and count connected components
        for node in range(n):
            if node not in visited:
                dfs(node, visited)
                count += 1

        return count

s = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(s.countComponents(n, edges))
