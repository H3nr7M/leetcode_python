'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
'''
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Inicializar límites de búsqueda
        left, right = 1, max(piles)
        result = right

        while left <= right:
            eating_time = (left + right) // 2 #mid

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / eating_time)

            if totalTime <= h: #tiempo valido
                result = eating_time
                right = eating_time - 1 #checar si puede haber otro min
            else:
                left = eating_time + 1 

        return result

sol = Solution()
piles = [3,6,7,11]
h = 8
print(sol.minEatingSpeed(piles, h))