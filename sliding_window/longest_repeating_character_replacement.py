# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        res = 0

        l = 0
        maxK = 0
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            #get the last added value vs the maxK value
            maxK = max(maxK, dic[s[r]])

            # add 1 because we are using r and l in the same position include 1 character
            window= r - l + 1
            if window - maxK > k:
                # move the left pointer
                dic[s[l]] -= 1
                l += 1
                window -= 1
            # save the max value of the window that satisfies the condition 
            res = max(res, window)
        return res

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k)) 
