# Phase 8: Advanced Heaps (Data Streams)
# 
# Problem: Find Median from Data Stream
#
# The median is the middle value in an ordered integer list. If the size of the list is even, 
# there is no middle value, and the median is the mean of the two middle values.
#
# Implement the MedianFinder class:
# - MedianFinder() initializes the MedianFinder object.
# - void addNum(int num) adds the integer num from the data stream to the data structure.
# - double findMedian() returns the median of all elements so far.
#
# Constraints:
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
#
# Example 1:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

import heapq

class MedianFinder:

    def __init__(self):
        # TODO: Implement your initialization here
        # LLM-Proof Hint: Sorting on every findMedian() call is O(N log N) which gives TLE.
        # You need TWO HEAPS to achieve O(log N) insertions and O(1) median lookups:
        # 1. A Max-Heap to store the smaller half of the numbers.
        # 2. A Min-Heap to store the larger half of the numbers.
        #
        # Python's heapq is a Min-Heap by default. To make a Max-Heap, insert negative values.
        pass

    def addNum(self, num: int) -> None:
        # TODO: Implement your solution here
        pass

    def findMedian(self) -> float:
        # TODO: Implement your solution here
        pass
