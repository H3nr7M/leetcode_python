# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

class Solution:
    def countBits(self, n: int) -> list[int]:
        bits = [0] * (n + 1)  # Create a list to store the bit counts
        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)
            # bits[i >> 1] takes the bit representation of i and shifts it one bit to the right
            # (i & 1) takes the bit representation of i and get the least significant bit
        
        return bits
    
if __name__ == '__main__':
    n = 8
    print(Solution().countBits(n))
