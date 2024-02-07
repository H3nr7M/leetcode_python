# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        #save the minimum number of coins to reach the amount
        dp = [amount + 1] * (amount + 1)
        #dp= [12] [12] [12] [12] [12] [12] [12] [12] [12] [12] [12] [12]
        #gonna calculate the minimum number of coins to reach the amount in ascending order
        dp[0] = 0

        for actualCoin in range(1, amount + 1): #moneda que quiero alcanzar
            #for each coin in the list of coins
            for c in coins:
                #calculate the minimum number of coins to reach the actualCoin from 1 to amount
                if actualCoin - c >= 0:
                    dp[actualCoin] = min(dp[actualCoin], 1 + dp[actualCoin - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

coins = [1,3,5]
amount = 11

f=Solution()
print(f.coinChange(coins, amount))
