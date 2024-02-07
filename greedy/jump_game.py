'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0  # maximum index that can be reached
        
        for i in range(len(nums)):
            if i > max_reach:  # if the current index is unreachable
                return False
            max_reach = max(max_reach, i + nums[i])  # update the maximum reach
            
            if max_reach >= len(nums) - 1:  # if the maximum reach exceeds or reaches the last index
                return True

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums)) # True