'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 #obtener el valor
            res = res | (bit << (31 - i)) #escribir valor
        return res
        

if __name__ == '__main__':
    x = 0b00000010100101000001111010011100
    print(Solution().reverseBits(x))

