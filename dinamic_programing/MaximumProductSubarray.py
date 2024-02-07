'''
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # n = len(nums)
        # max_dp = [0] * n  # maximum product subarray ending at index i
        # min_dp = [0] * n  # minimum product subarray ending at index i
        # max_dp[0] = min_dp[0] = res = nums[0]

        # for i in range(1, n):
        #     if nums[i] < 0:
        #         max_dp[i], min_dp[i] = min_dp[i-1]*nums[i], max_dp[i-1]*nums[i] 
        #     else:
        #         max_dp[i], min_dp[i] = max_dp[i-1]*nums[i], min_dp[i-1]*nums[i]

        #     max_dp[i] = max(max_dp[i], nums[i])
        #     min_dp[i] = min(min_dp[i], nums[i])
        #     res = max(res, max_dp[i])

        # return res
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax * n
            tmp2 = curMin * n
            curMax = max(tmp, tmp2, n)
            curMin = min(tmp, tmp2, n)
            res = max(res, curMax)
        return res

if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(Solution().maxProduct(nums))