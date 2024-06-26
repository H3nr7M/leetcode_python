# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        # set rows/cols to zero
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0: # if the first row or col is zero
                    matrix[r][c] = 0

        if matrix[0][0] == 0: # if the first element is zero (first row set to zero)
            for r in range(1, ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(1, COLS): # if rowZero is True, then the first col needs to be zero
                matrix[0][c] = 0

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix) # [[1,0,1],[0,0,0],[1,0,1]]
    print(matrix)