# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
# Note:
# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

class Solution:
    def hamming_weight(self, n: int) -> int:
        count = 0
        while n: # the whole value of n
            count += n & 1 # performs a bitwise AND operation, this operation extracts the least significant bit of n.
            n = n >> 1 # shifts n one bit to the right, removing the least significant bit.
        return count

    
if __name__ == '__main__':
    n = 0o0010001001011
    print(Solution().hamming_weight(n)) #5
