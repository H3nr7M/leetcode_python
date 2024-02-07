'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        count = 0
        res = nums[0]
        for v in nums:
            count += v
            res = max(res, count)
            if count < 1:
                count = 0
            

        return res

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))