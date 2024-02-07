# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order. If there is no valid ordering, return an empty string. If there are multiple valid orderings, return any of them.
# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, it is guaranteed that no two words are the same.
# Example 1:
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:
# Input: words = ["z","x"]
# Output: "zx"
# Example 3:
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = {}
        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = set()

        # take 2 words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2)) # select the word with the min length
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # the prev word must be shorter than the next word and the first minLen chars must be the same
                return ""
            for j in range(minLen): # compare until shorter word finish
                if w1[j] != w2[j]: # looking for the first different char
                    adj[w1[j]].add(w2[j]) 
                    break

        visited = {} 
        res = []

        def dfs(char):
            if char in visited:
                return visited[char] # dfs return true

            visited[char] = True

            for neighChar in adj[char]: # the finish char dont enter in the for loop
                if dfs(neighChar):
                    return True #

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char): # if the dfs return true, there is a cycle
                return ""

        res.reverse() # post order dfs to avoid take the wrong order
        return "".join(res)
    

s = Solution()
words = ["wrt","wrf","er","ett","rftt"]
print(s.alienOrder(words))
