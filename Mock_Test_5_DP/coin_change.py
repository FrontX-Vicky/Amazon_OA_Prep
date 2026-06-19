# Phase 4: Dynamic Programming (The Final Boss)
# 
# Problem: Coin Change
#
# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
#
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

def coinChange(coins: list[int], amount: int) -> int:
    # TODO: Implement your solution here
    # 
    # LLM-Proof Warning: A naive Greedy approach (always taking the largest coin first) FAILS.
    # For example, if coins = [1, 3, 4] and amount = 6. 
    # Greedy takes 4, leaving 2. Then takes 1, 1. Total = 3 coins.
    # But optimal is 3 + 3. Total = 2 coins!
    #
    # Hint: You need a 1D DP array of size (amount + 1). 
    # dp[i] will store the MINIMUM number of coins needed to make amount 'i'.
    # Bottom-up approach: solve for amount=1, then amount=2, all the way up to target.
        

