'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
'''
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = collections.Counter(nums)
        res = []
        for i in range(k):
            #(n, k)
            res.append(dic.most_common()[i][0]) # dic is sort by the most common to the least common
        return res
        
        
import collections

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k)) # Output: [1, 2]
