# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])  # Sort intervals by their end values
        end = intervals[0][1]
        count = 1
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]
        
        return len(intervals) - count

f = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(f.eraseOverlapIntervals(intervals)) # 1