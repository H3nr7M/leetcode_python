'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
https://leetcode.com/problems/word-search/
'''
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visit = set()

        def back(visit, r, c, word):
            if len(word) == 0:
                return True
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r, c) in visit or board[r][c] != word[0]:
                return False
            
            visit.add((r, c))
            res = back(visit, r + 1, c, word[1:]) or back(visit, r - 1, c, word[1:]) or back(visit, r, c + 1, word[1:]) or back(visit, r, c - 1, word[1:])

            visit.remove((r, c))
            return res

        for r in range(ROW):
            for c in range(COL):
                if back(visit, r, c, word):
                    return True
                
        return False   


    
if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCCED"
    print(Solution().exist(board, word))
