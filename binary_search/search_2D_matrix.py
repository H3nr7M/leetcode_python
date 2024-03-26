'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''Verifica si hay matrix o la primera fila de la matriz está vacía'''
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        
        # Búsqueda binaria para encontrar la fila
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # Búsqueda binaria en la fila
                left, right = 0, cols - 1
                while left <= right:
                    mid_col = left + (right - left) // 2
                    if matrix[mid][mid_col] == target:
                        return True
                    elif matrix[mid][mid_col] < target:
                        left = mid_col + 1
                    else:
                        right = mid_col - 1
                return False #esta en el rango pero no en la fila
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        
        return False #no esta en el rango

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix=matrix, target=target))

