'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom: # because we are not using indices
            # get every i in the top row
            for i in range(left, right): # because we are using indices
                res.append(matrix[top][i])
            top += 1 # move top down
            # get every i in the right col
            for i in range(top, bottom): # because we are using indices
                res.append(matrix[i][right - 1])
            right -= 1 # move right left
            if not (left < right and top < bottom): # if we have reached the center element
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1): # because we are using indices
                res.append(matrix[bottom - 1][i])
            bottom -= 1 # move bottom up
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1): # because we are using indices
                res.append(matrix[i][left])
            left += 1 # move left right

        return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix)) # [1,2,3,6,9,8,7,4,5]