'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
Input: m = 3, n = 7
Output: 28
Example 2:
Input: m = 3, n = 2
Output: 3
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # buttom row
        for i in range(m - 1): # rows less buttom row
            newRow = [1] * n
            for j in range(n - 2, -1, -1): # avoid the rightmost column, from right to left
                newRow[j] = newRow[j + 1] + row[j] # right + down
            row = newRow
        return row[0]

if __name__ == "__main__":
    m = 3
    n = 7
    print(Solution().uniquePaths(m, n)) # 28