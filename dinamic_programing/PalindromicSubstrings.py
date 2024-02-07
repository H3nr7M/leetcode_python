
'''
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
# dp solution, O(n^2) time, O(n^2) space
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n):
            dp[i][i] = True
            res += 1
        for window in range(2, n + 1):
            for i in range(n - window + 1):
                j = i + window - 1
                if s[i] == s[j] and (window == 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res

# two pointers solution, O(n^2) time, O(1) space
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         res = 0

#         for i in range(len(s)):
#             res += self.countPali(s, i, i)
#             res += self.countPali(s, i, i + 1)
#         return res

#     def countPali(self, s, l, r):
#         ans = 0
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             ans += 1
#             # the window is opening
#             l -= 1
#             r += 1
#         return ans

if __name__ == "__main__":
    s = "aaa"
    print(Solution().countSubstrings(s))