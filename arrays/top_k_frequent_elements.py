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
        '''contar valor y frecuencia'''
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

        #lista de arreglos vacios + 1, para eliminar la frec 0
        bucket = [[] for _ in range(len(nums)+1)]

        for num, frec in dic.items():
            bucket[frec].append(num)

        res = []

        for i in range(len(bucket)-1, 0, -1): #a cero porque no lo vas a tomar
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k)) # Output: [1, 2]
