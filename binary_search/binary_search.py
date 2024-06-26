'''
Given an array of integers nums which is sorted in ascending 
order, and an integer target, write a function to search target 
in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int: #[-1,0,3,5,9,12]

        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(sol.search(nums, target))