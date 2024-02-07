class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = set()
        for n in nums:
            if n in dic:
                return True
            dic.add(n)
        return False

nums = [1,2,3,1]
print(Solution().containsDuplicate(nums)) 

#Time complexity: O(n)
#Space complexity: O(n)
