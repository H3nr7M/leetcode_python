'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res, max_act = 0, 0
        for n in nums:
            if n - 1 in nums:
                continue
            while n in nums:
                max_act += 1
                n += 1
            res = max(res, max_act)
            max_act = 0
        return res

nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums)) #9
# final time complexity: O(n)

