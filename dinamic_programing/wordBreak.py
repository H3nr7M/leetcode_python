'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # empty string is always in the dictionary
        
        for i in range(1, n+1): # i is the length of the substring
            for j in range(i): 
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[n]

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    print(Solution().wordBreak(s, wordDict))