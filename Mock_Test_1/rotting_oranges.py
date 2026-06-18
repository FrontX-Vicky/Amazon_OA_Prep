# Problem 2: Rotting Oranges
#
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
# If this is impossible, return -1.

from collections import deque
def orangesRotting(grid: list[list[int]]) -> int:
    # TODO: Implement your solution here
    # Hint: This is a classic multi-source BFS problem. 
    # Use a collections.deque to keep track of rotten oranges and minutes elapsed.
    # Get grid dimensions to make boundary checks easier
    rows, cols = len(grid), len(grid[0])
    
    # We use a deque (double-ended queue) for O(1) pops from the left side.
    # This queue will hold the coordinates of all CURRENTLY rotting oranges.
    q = deque()
    
    # Track how many fresh oranges exist. If this never reaches 0, we return -1.
    fresh_count = 0

    # STEP 1: Initialize the queue and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Found a fresh orange
                fresh_count += 1
            elif grid[r][c] == 2:
                # Found a rotten orange. Add it to our "Level 0" starting queue.
                # Because we can have multiple rotten oranges at the start, 
                # this is a "Multi-Source" BFS.
                q.append((r, c))
    
    minutes = 0

    # STEP 2: Breadth-First Search (BFS)
    # We only continue if there are items in the queue AND there are still fresh oranges left.
    # (If fresh_count is 0, we don't need to process the last minute).
    while q and fresh_count > 0:
        # Take a snapshot of the queue size. This represents all the oranges
        # that are rotting during THIS specific minute.
        size = len(q)
        
        # Process ONLY the oranges for the current minute
        for _ in range(size):
            r, c = q.popleft() # O(1) removal from front of queue
            
            # Check all 4 adjacent directions (Right, Left, Down, Up)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # If the adjacent cell is within grid bounds AND contains a fresh orange (1)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2       # 1. Rot the fresh orange
                    fresh_count -= 1       # 2. Decrease fresh count
                    q.append((nr, nc))     # 3. Add to queue so it can rot its neighbors next minute
        
        # After processing all oranges for this level/minute, increment the timer
        minutes += 1
    
    # STEP 3: Final Check
    # If all fresh oranges were successfully rotted, return the total time
    if fresh_count == 0:
        return minutes
    else:
        # Some fresh oranges were unreachable (blocked by empty cells)
        return -1
    