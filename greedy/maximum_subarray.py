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
        result = float('-inf')
        actual = 0

        for n in nums:
            actual += n
            result = max(result, actual)
            if actual <= 0:
                actual = 0          

        return result

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))