# Phase 4: Dynamic Programming (The Final Boss)
# 
# Problem: House Robber
#
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you 
# from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.
#
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

def rob(nums: list[int]) -> int:
    # TODO: Implement your solution here
    # 
    # LLM-Proof Hint: This is the ultimate test of understanding DP State Transitions!
    # Let dp[i] be the MAXIMUM money you can steal if you consider houses from index 0 up to index i.
    # 
    # For any house 'i', you only have TWO choices:
    # 1. You ROB house 'i'. This means you CANNOT rob house 'i-1'. 
    #    So your total money is: (Money at house i) + (Max money you could steal up to house i-2).
    # 
    # 2. You SKIP house 'i'. This means your total money is exactly the same as 
    #    the max money you could steal up to house 'i-1'.
    #
    # Your Transition Formula: dp[i] = max(Option 1, Option 2)
    pass
