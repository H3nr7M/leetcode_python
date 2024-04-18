# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([char for char in s if char.isalnum()])

        return s == s[::-1]        

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))  # Output: True
