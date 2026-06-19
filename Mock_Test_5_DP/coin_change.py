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
    # 1. Initialize the DP array
    # We use float('inf') as a placeholder for "impossible"
    # The size is amount + 1 because we need an index for every amount from 0 up to 'amount'
    dp = [float('inf')] * (amount + 1)
    
    # 2. Base Case
    # It takes exactly 0 coins to make an amount of 0.
    dp[0] = 0
    
    # 3. Bottom-Up DP (The Transition)
    # We will try to find the optimal answer for amount 1, then amount 2, etc.
    for i in range(1, amount + 1):
        for coin in coins:
            # If the current coin is small enough to fit inside amount 'i'
            if i - coin >= 0:
                # The minimum coins to make amount 'i' is either:
                # Option A: What we already have (dp[i])
                # Option B: 1 (the coin we just used) + the minimum coins needed to make the remaining amount (dp[i - coin])
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    # 4. Final Answer
    # If the last element is still infinity, it means it's impossible to make that amount.
    return dp[amount] if dp[amount] != float('inf') else -1
