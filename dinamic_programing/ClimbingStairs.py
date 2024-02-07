'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]* (n + 1)
        for i in range(n -2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        return dp[0]

        # version optimizada
        # if n <= 3:
        #   return n
        # n1, n2 = 2, 3

        # for i in range(4, n + 1):
        #     temp = n1 + n2
        #     n1 = n2
        #     n2 = temp
        # return n2
f=Solution()
n = 4
print(f.climbStairs(n))

