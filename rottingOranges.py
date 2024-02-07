'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
'''
import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        #we going to use BFS
        q = collections.deque() #for track of rotten oranges
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1 #track the number of fresh oranges
                if grid[r][c] == 2:
                    q.append((r, c)) #track the location of rotten oranges

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] #this is a list of directions
        while fresh > 0 and q:
            length = len(q)
            for i in range(length): #for each starting rotten orange
                r, c = q.popleft()

                for dr, dc in directions: #this going to run 4 times
                    row, col = r + dr, c + dc #get the next cell and each direction
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2 #make fresh orange rotten
                        q.append((row, col))
                        fresh -= 1
            time += 1 #increment time
        return time if fresh == 0 else -1

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))
