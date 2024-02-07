# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # the idea is count need against have characters
        count = len(t) # number of characters needed to form t
        if not count <= len(s):
            return ""

        target = {} #map of characters in t
        for c in t:
            if c not in target:
                target[c] = 1
            else:
                target[c] += 1

        # initialize pointers and counters
        left = 0
        right = 0
        ans = ""
        min_len = float("inf")

        # iterate through the string s
        while right < len(s):
            # if the character at right pointer is in target, decrement count
            if s[right] in target:
                if target[s[right]] > 0:
                    count -= 1
                target[s[right]] -= 1
            
            # move right pointer
            right += 1
            
            # if count is 0, update ans and move left pointer
            while count == 0:
                # update ans if new window is smaller than previous
                if right - left < min_len:
                    min_len = right - left
                    ans = s[left:right]
                
                # if the character at left pointer is in target, increment count
                if s[left] in target:
                    target[s[left]] += 1 # I'm subtracting a nedded character so I need to add it back
                    if target[s[left]] > 0: # if target[s[left]] is negative or 0 means I have more than needed 
                        count += 1
                
                # move left pointer
                left += 1
        
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC")) # BANC