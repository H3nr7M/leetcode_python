# Description Given a string s, find the length of the longest 
# substring
#  without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, right = 0, 0
        max_length = 0
        
        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                window.remove(s[left])
                left += 1
        
        return max_length

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb")) # 3