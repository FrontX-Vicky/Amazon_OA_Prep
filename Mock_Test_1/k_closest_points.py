# Problem 1: K Closest Points to Origin
#
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
# return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., sqrt(x^2 + y^2)).
# You may return the answer in any order.
import heapq

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    # TODO: Implement your solution here
    # Hint: Think about using a Priority Queue (Heap) or Sorting. 
    # Python's heapq module will be very useful.
    heap = []
    res = []

    for x,y in points:
        d = (x*x + y*y)
        heapq.heappush(heap, (d, x ,y))

    for _ in range(k):
        _, x, y = heapq.heappop(heap)
        res.append([x, y])
    
    return res





