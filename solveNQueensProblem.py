def solveNQueens(n):
    def can_place(row, col):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row = 0, count = 0):
        if row == n:
            count += 1
        else:
            for col in range(n):
                if can_place(row, col):
                    board[row] = col
                    count = backtrack(row + 1, count)
        return count

    board = [-1 for i in range(n)]
    return backtrack()

# Call the solveNQueens function
result = solveNQueens(4)

# Print the result
print("The number of possible arrangements of the 4x4 board is: ", result)
