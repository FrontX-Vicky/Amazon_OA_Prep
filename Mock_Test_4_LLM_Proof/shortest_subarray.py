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

def shortestSubarray(nums: list[int], k: int) -> int:
    # TODO: Implement your solution here
    # 
    # LLM-Proof Warning: A standard Two-Pointer / Sliding Window approach will FAIL here.
    # Why? Because standard Sliding Window relies on the sum *monotonically increasing* 
    # as you expand the right pointer, and *monotonically decreasing* as you shrink the left.
    # Because nums can contain negative numbers, expanding the right pointer might actually DECREASE the sum.
    # 
    # Hint: You need a Prefix Sum array. But to find the shortest distance efficiently, 
    # consider maintaining a Monotonic Deque of the prefix sum indices.
    
    n =len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

          