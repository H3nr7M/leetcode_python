# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# https://leetcode.com/problems/word-search-ii/
# See WordSearch.py in python/backtracking
# The most efiicient solution is to use a Trie data structure to store the words and then search the board for the words.
class TrieNode:
    def __init__(self):
        self.children = {} # key: char, value: TrieNode
        self.isWord = False # True if this node is the end of a word
        self.refs = 0 # number of words that have this node as a prefix

    def addWord(self, word):
        cur = self
        cur.refs += 1 # increment the number of words that have this node as a prefix
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] # move down the trie
            cur.refs += 1 # increment the number of words that have this node as a prefix
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c] # move down the trie
                cur.refs -= 1


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words: # add all words to the trie
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set() # to store uniques

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS) 
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]] # move down the trie
            word += board[r][c] # build the word
            if node.isWord:
                # to not add the same word twice
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            # move troght the board
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution().findWords(board, words)) # ["eat","oath"]
