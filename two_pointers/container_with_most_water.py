# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

class Solution:
    def max_area(self, height: list[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            base = right - left
            if height[left] < height[right]:
                result = max(result, height[left]*base)
                left += 1
            else:
                result = max(result, height[right]*base)
                right -= 1

        return result

height = [1,8,6,2,5,4,8,3,7]
print(Solution().max_area(height)) # Output: 49