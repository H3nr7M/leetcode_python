# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])  # Sort intervals by their start values
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)  # No overlap, add the interval to the result
            else:
                res[-1][1] =  max(res[-1][1], interval[1]) # Merge overlapping intervals
        return res

f = Solution()
print(f.merge([[1,3],[2,6],[8,10],[15,18]]))
