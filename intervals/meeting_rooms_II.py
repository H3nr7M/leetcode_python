# The input to the problem is a list of intervals, where each interval represents a meeting that needs to be scheduled. The intervals are given as pairs of start and end times, where the start time is inclusive and the end time is exclusive. For example, an interval (1, 3) means that a meeting starts at time 1 and ends at time 3.
# The goal of the problem is to find the minimum number of meeting rooms required to schedule all the given meetings. A meeting room can only be used for one meeting at a time, and a new meeting cannot start until the previous meeting in that room has ended.
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Explanation: We need two meeting rooms
import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # create a array of start times and end times
        time = []
        for start, end in intervals:
            time.append((start, 1)) # 1 means start a meeting
            time.append((end, -1)) # -1 means end a meeting
        
        time.sort(key=lambda x: (x[0], x[1])) # Sort the time list by the start time and then by the end time
        
        count = 0
        max_count = 0 # store the max number opend meeting rooms
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count


# Time complexity: O(nlogn) because of the sorting
# Space complexity: O(n) because we are using a list to store the start and end times of all the meetings

interval = [[0,5],[5,10],[10,20]]
print(Solution().minMeetingRooms(interval))