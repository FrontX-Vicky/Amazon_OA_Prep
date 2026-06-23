"""
AMAZON OA: Delivery Center Routing (Modified Graph BFS)

You are navigating a city grid of size N x M to deliver a package.
- '0' represents a valid road.
- '1' represents an obstacle (building).
- 'S' is your starting position.
- 'D' is the destination.
- 'C' is a charging station.

You are driving an electric van. It takes 1 minute to move to any adjacent 
cell (up, down, left, right). Every time you move, your battery drops by 1.
You start with a full battery of capacity `B`.
If your battery reaches 0, you can no longer move.

When you land on a charging station 'C', your battery instantly recharges 
to its maximum capacity `B`. (The move to the station still takes 1 minute).

Find the minimum time (in minutes) to reach the destination 'D'.
If it is impossible to reach 'D', return -1.

THE TWIST (Why standard BFS fails):
Standard BFS marks a cell as `visited` so you never revisit it. 
However, in this problem, you might need to walk over the SAME cell twice 
(e.g., crossing your own path after charging your battery) to reach the destination!
If you use a standard `visited = set()`, your code will fail.
"""
from collections import deque

def minDeliveryTime(grid: list[list[str]], B: int) -> int:
    # TODO: Implement your state-space BFS here!
    rows, cols = len(grid), len(grid[0])
    charging_stations = []
    start = None
    steps = 0
    q = deque()
    destination = None
    visited = {}



    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'C':
                charging_stations.append((i,j))
            if grid[i][j] == 'D': 
                destination = (i, j)
            if grid[i][j] == 'S':
                start = (i,j,B, steps)
                visited[(i,j)] = B
                q.append(start)
            


    directions = [(0,1),(0,-1),(-1,0),(1,0)]

    while q:
        x, y, b, s = q.popleft()
      
      
        if grid[x][y] == 'D':
            return s 
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            next_b = b - 1
            next_s = s + 1

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '1' and grid[nx][ny] != 'S':
                if next_b < 0: continue
                if grid[nx][ny] == 'C': next_b = B
                
                # Only explore this cell if we arrive with MORE battery than before
                if next_b > visited.get((nx, ny), -1):
                    visited[(nx, ny)] = next_b
                    q.append((nx, ny, next_b, next_s))

    return -1
                



        







    

    
    