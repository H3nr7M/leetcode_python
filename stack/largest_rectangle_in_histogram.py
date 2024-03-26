'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
'''
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        
        heights.append(0)
        
        for i, h in enumerate(heights):
            #porque me interesa que la actual sea menor?
            while stack and h < heights[stack[-1]]:
                height_index = stack.pop()
                #porque me interesa que no haya nada en el stack?
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[height_index] * width)
            
            stack.append(i)
        
        return max_area
    
sol = Solution()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))