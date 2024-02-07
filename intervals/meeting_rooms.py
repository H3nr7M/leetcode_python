# Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], determine if a person could attend all meetings.
# In other words, you are given a list of time intervals where each interval represents a meeting with a start time and an end time. Your task is to determine whether a person could attend all of the meetings without overlapping. If it is possible for a person to attend all the meetings without overlap, the function should return true, otherwise, it should return false.
# Example: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example: intervals = [[7,10],[2,4]]
# Output: true

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort()
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                return False
            else:
                end = intervals[i][1]
        return True

# Time complexity: O(nlogn) because of the sorting
# Space complexity: O(1) because we are not using any extra space

interval = [[0,30],[5,10],[15,20]]
print(Solution().canAttendMeetings(interval)) # False