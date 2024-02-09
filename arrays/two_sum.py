'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        
        if len(nums) < 2:
            raise ValueError("La lista debe tener al menos dos elementos.")
        
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], idx]
            else:
                num_indices[num] = idx
        
        raise ValueError("No se encontraron dos números que sumen el objetivo.")


# Ejemplo de uso:
suma = Solution()
nums_example = [2, 7, 11, 15]
target_example = 9
result = suma.two_sum(nums_example, target_example)
print(result)  # Output: [0, 1] (ya que nums[0] + nums[1] = 2 + 7 = 9)
