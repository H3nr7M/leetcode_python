# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break

            left, right = i+1, len(nums) - 1
        
            while left < right:
                suma = nums[i] + nums[left] + nums[right]
                if suma == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif suma < 0:
                    left += 1
                else:
                    right -= 1

        return result


    

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums)) # Output: [[-1,-1,2],[-1,0,1]]
