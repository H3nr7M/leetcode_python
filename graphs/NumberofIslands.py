'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''

class Solution:
    def numIslands(self, grid: list[list[int]]):
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        row, col = len(grid), len(grid[0])
        visit = set()

        def checkDir(r: int, c: int):
            if (r not in range(row) 
                or c not in range(col) 
                or (r,c) in visit 
                or grid[r][c] == '0'):
                return 
            
            visit.add((r, c))
            direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in direction:
                checkDir(r + dr, c + dc)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visit:
                    islands += 1
                    checkDir(r,c)

        return islands

        

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(Solution().numIslands(grid))