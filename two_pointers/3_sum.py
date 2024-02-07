# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2): # n=6 range 0 to 4
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: # skip duplicates
                continue
            l, r = i+1, len(nums)-1 # two pointers
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    l += 1
                    r -= 1
        return res


    

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums)) # Output: [[-1,-1,2],[-1,0,1]]
