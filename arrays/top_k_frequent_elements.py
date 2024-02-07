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
#         dic = collections.Counter(nums)
#         res = []
#         for i in range(k):
#             res.append(dic.most_common()[i][0]) # dic is sort by the most common to the least common
#         return res
        dic = {}
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)

        bucket = [[] for _ in range(len(nums)+1)]
        for ke, v in dic.items():
            bucket[v].append(ke)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
# import collections

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k)) # Output: [1, 2]
