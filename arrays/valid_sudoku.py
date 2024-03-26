'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to 
be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

'''

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Conjuntos para rastrear números vistos en filas, columnas y cuadros
        rows = [set() for _ in range(9)]
        #[{0},{1},{2},{3},{4},{5},{6},{7},{8},]
        cols = [set() for _ in range(9)]
        #[{0},{1},{2},{3},{4},{5},{6},{7},{8},]
        boxes = [set() for _ in range(9)]
        #[{0},{1},{2},{3},{4},{5},{6},{7},{8},]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    
                    # Verifica si el número ya ha sido visto en la fila actual
                    if num in rows[i]:
                        return False
                    rows[i].add(num)
                    
                    # Verifica si el número ya ha sido visto en la columna actual
                    if num in cols[j]:
                        return False
                    cols[j].add(num)
                    
                    # Calcula el índice de la caja actual
                    #el *3 hace el salto de fila de cajas
                    box_index = (i // 3) * 3 + j // 3
                    
                    # Verifica si el número ya ha sido visto en la caja actual
                    if num in boxes[box_index]:
                        return False
                    boxes[box_index].add(num)
        
        return True
    
sol = Solution()
board =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board=board))
