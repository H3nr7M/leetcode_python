'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # add a 0 col and row for outbound values
        dp = []
        for i in range(len(text1) + 1):
            dp.append([0] * (len(text2) + 1))

        for i in range(len(text1) - 1, -1, -1): # using index buttom up
            for j in range(len(text2) - 1, -1, -1): # using index right to left
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j]) # max of left or down

        return dp[0][0]

text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))