'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        # tiny pize of memory for not overlapping the matrix[0][0] element
        rowZero = False

        # determine which rows/cols need to be zero
        # Save the rows and cols that need to be zero in the first row and col
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Turn first element of row and col to 0
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True


        # avoid changing first row/col again
        # Turn the rows and cols to 0, except for the matrix[0][0] element
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # start with col and row
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Because the first col track the 1st col
        if matrix[0][0] == 0:
            for r in range(ROWS):
                # set first col to 0
                matrix[r][0] = 0

        # Because the rowZero is the tiny piece of memory for tracking the 1st row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Solution().setZeroes(matrix)
    for row in matrix:
        print(row)