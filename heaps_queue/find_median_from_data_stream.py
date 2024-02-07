# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
#                          output [2, 1.5, 2, 3.5, 2, 2, 2]
# the list must be sorted always, and know if the list is even or odd if even then take the average of the two middle numbers and if odd then take the middle number
#which data structure is always sorted and can be used to find the middle number in a list
# getMin(): It returns the root element of Min Heap. The Time Complexity of this operation is O(1).
# extractMin(): Removes the minimum element from MinHeap. The Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing the root.
# insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If a new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.

import heapq

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], []  # left and right half of the list

    def addNum(self, num: int) -> None:
        # in relation to the number, it accommodates it on the left or right side
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else: # everything new is added to the left side
            heapq.heappush(self.small, -1 * num)

        # balance the two sides
        if len(self.small) > len(self.large) + 1: # difference between the two sides is 2 or greater
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1: # difference between the two sides is 2 or greater
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2



medianFinder = MedianFinder()
medianFinder.addNum(1)   
medianFinder.addNum(2)  
medianFinder.addNum(6)
medianFinder.addNum(10)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)  
print(medianFinder.findMedian())
