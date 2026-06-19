# Phase 2: State Maintenance in Graphs
# 
# Problem: Shortest Path in a Grid with Obstacles Elimination
#
# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
# You can move up, down, left, or right from and to an empty cell in one step.
#
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1)
# given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
#
# Example 1:
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. 
#
# Example 2:
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.

def shortestPath(grid: list[list[int]], k: int) -> int:
    # TODO: Implement your solution here
    # 
    # LLM-Proof Warning: Standard BFS uses a `visited` set to track cells like `(row, col)`.
    # If you do that here, you will fail!
    # Why? Because in this problem, you might visit the same cell multiple times, 
    # and a later visit might actually be BETTER if you arrive with more `remaining_k` (fewer obstacles destroyed).
    # 
    # Hint: Your BFS Queue and your Visited set must track STATE, not just POSITION.
    # What exactly defines the "state" of your search at any given moment?
    pass
