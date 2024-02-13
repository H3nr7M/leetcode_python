# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {} # Dictionary for counting characters in s and t

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #add 1 to the count of the character if it exists, otherwise set it to 1
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT #return boolean

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t)) # Output: True

#Time complexity: O(n)
#Space complexity: O(n)
