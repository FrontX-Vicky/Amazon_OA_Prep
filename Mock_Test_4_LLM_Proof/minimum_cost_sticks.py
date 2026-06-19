# Phase 3: Priority Queues & Invariants
# 
# Problem: Minimum Cost to Connect Sticks
#
# You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, 
# where sticks[i] is the length of the ith stick.
#
# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. 
# You must connect all the sticks until there is only one stick remaining.
#
# Return the minimum cost of connecting all the given sticks into one stick in this way.
#
# Constraints:
# 1 <= sticks.length <= 10^4
# 1 <= sticks[i] <= 10^4
#
# Example 1:
# Input: sticks = [2,4,3]
# Output: 14
# Explanation: You start with sticks = [2,4,3].
# 1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
# 2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
# There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
#
# Example 2:
# Input: sticks = [1,8,3,5]
# Output: 30
#
# Example 3:
# Input: sticks = [5]
# Output: 0

import heapq

def connectSticks(sticks: list[int]) -> int:
    # TODO: Implement your solution here
    # 
    # LLM-Proof Warning: A naive approach might just sort the array once and then add the numbers up.
    # Why does that fail? Because when you combine two small sticks, the NEW combined stick 
    # might actually be LARGER than other existing sticks in the array!
    # 
    # Hint: You need a data structure that allows you to constantly remove the two smallest elements,
    # and insert a new element, while maintaining sorted order perfectly in O(log N) time.
    pass
