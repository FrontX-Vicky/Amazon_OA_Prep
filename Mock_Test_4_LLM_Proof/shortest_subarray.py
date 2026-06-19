# Phase 1: Breaking the Templates (LLM-Proof Constraints)
# 
# Problem: Shortest Subarray with Sum at Least K
#
# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums 
# with a sum of at least k. If there is no such subarray, return -1.
#
# A subarray is a contiguous part of an array.
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5  <--- CAUTION: NEGATIVE NUMBERS ALLOWED
# 1 <= k <= 10^9
#
# Example 1:
# Input: nums = [1], k = 1
# Output: 1
#
# Example 2:
# Input: nums = [1,2], k = 4
# Output: -1
#
# Example 3:
# Input: nums = [2,-1,2], k = 3
# Output: 3

from collections import deque

def shortestSubarray(nums: list[int], k: int) -> int:
    n = len(nums)
    # 1. Prefix Sum Array
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # 2. Monotonic Deque
    # We will store INDICES of the prefix_sum array in this deque.
    # The values at these indices will be kept strictly increasing.
    q = deque()
    shortest = float('inf')

    for i in range(n + 1):
        # A) Check for valid subarray
        # If the difference between the current prefix sum and the prefix sum 
        # at the FRONT of the queue is >= k, we found a valid subarray!
        while q and prefix_sum[i] - prefix_sum[q[0]] >= k:
            shortest = min(shortest, i - q.popleft())
        
        # B) Maintain the Monotonic Property
        # If the current prefix sum is LESS than or equal to the prefix sum at the BACK
        # of the queue, the back element is useless. 
        while q and prefix_sum[i] <= prefix_sum[q[-1]]:
            q.pop()
            
        # C) Add current index to the queue
        q.append(i)

    return shortest if shortest != float('inf') else -1
