# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # to limit the result to 32 bits
        # F = 1111, 8 * 4 = 32 bits
        while b & mask != 0: # while b is not 0
            carry = (a & b) << 1 
            a = a ^ b # sum without carry
            b = carry

        return a & mask if b > mask else a # truncate the result to 32 bits

# Time Complexity: O(1)
# Space Complexity: O(1)
f = Solution()
print(f.getSum(-1, 1))
