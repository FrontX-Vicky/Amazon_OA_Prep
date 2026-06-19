# Problem 1: Number of Islands
#
# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
#
# Example:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

def numIslands(grid: list[list[str]]) -> int:
    # TODO: Implement your solution here
    # Hint: You can use either DFS or BFS. When you find a '1', increment your island count, 
    # and then run a DFS/BFS to mark all connected '1's as visited (or change them to '0').
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islandCount = 0


    def dfs(grid, r, c):
        if  0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
            grid[r][c] = "0"
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(grid, r, c)
                islandCount += 1
    
    return islandCount

