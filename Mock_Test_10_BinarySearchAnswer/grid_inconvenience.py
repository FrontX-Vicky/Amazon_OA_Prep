from collections import deque

def getMinInconvenience_Simple(grid: list[list[int]]) -> int:
    """
    O(N * M * log D) Solution
    Iterates over the entire grid for each binary search guess to find bounding box.
    Extremely elegant, fast to write, easily passes constraints.
    """
    n = len(grid)
    if n == 0: return 0
    m = len(grid[0])
    if m == 0: return 0

    dist = [[-1] * m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))

    # Edge case: No 1s in the entire grid
    if not q:
        return max((n - 1) // 2, (m - 1) // 2, n // 2, m // 2)

    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    maxDist = max(max(row) for row in dist)

    def can(mid):
        r1, r2 = 0, n - 1
        c1, c2 = 0, m - 1
        for i in range(n):
            for j in range(m):
                if dist[i][j] > mid:
                    r1 = max(r1, i - mid)
                    r2 = min(r2, i + mid)
                    c1 = max(c1, j - mid)
                    c2 = min(c2, j + mid)
        return r1 <= r2 and c1 <= c2

    left, right = 0, maxDist
    while left < right:
        mid = (left + right) // 2
        if can(mid):
            right = mid
        else:
            left = mid + 1
            
    return left

def getMinInconvenience_Optimal(grid: list[list[int]]) -> int:
    """
    O(N * M) Solution
    Precomputes suffix arrays to bound the rectangles in strictly O(1) time.
    """
    n = len(grid)
    if n == 0: return 0
    m = len(grid[0])
    if m == 0: return 0
    
    dist = [[float('inf')] * m for _ in range(n)]
    q = deque()
    
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                dist[r][c] = 0
                q.append((r, c))
                
    if not q:
        return max((n - 1) // 2, (m - 1) // 2, n // 2, m // 2)
        
    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    max_d = 0
    
    while q:
        r, c = q.popleft()
        d = dist[r][c]
        if d > max_d: max_d = d
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == float('inf'):
                dist[nr][nc] = d + 1
                q.append((nr, nc))
                
    if max_d == 0:
        return 0
        
    max_r = [-float('inf')] * (max_d + 1)
    min_r = [float('inf')] * (max_d + 1)
    max_c = [-float('inf')] * (max_d + 1)
    min_c = [float('inf')] * (max_d + 1)
    
    for r in range(n):
        for c in range(m):
            d = dist[r][c]
            if d != float('inf'):
                if r > max_r[d]: max_r[d] = r
                if r < min_r[d]: min_r[d] = r
                if c > max_c[d]: max_c[d] = c
                if c < min_c[d]: min_c[d] = c
                
    s_max_r = [-float('inf')] * (max_d + 2)
    s_min_r = [float('inf')] * (max_d + 2)
    s_max_c = [-float('inf')] * (max_d + 2)
    s_min_c = [float('inf')] * (max_d + 2)
    
    for d in range(max_d, -1, -1):
        s_max_r[d] = max(max_r[d], s_max_r[d+1])
        s_min_r[d] = min(min_r[d], s_min_r[d+1])
        s_max_c[d] = max(max_c[d], s_max_c[d+1])
        s_min_c[d] = min(min_c[d], s_min_c[d+1])
        
    def check(K):
        if K >= max_d:
            return True
            
        R_min = s_max_r[K+1] - K
        R_max = s_min_r[K+1] + K
        C_min = s_max_c[K+1] - K
        C_max = s_min_c[K+1] + K
        
        if R_min > R_max or C_min > C_max:
            return False
            
        R_min = max(R_min, 0)
        R_max = min(R_max, n - 1)
        C_min = max(C_min, 0)
        C_max = min(C_max, m - 1)
        
        return R_min <= R_max and C_min <= C_max

    left = 0
    right = max_d
    ans = right
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ans

def getMinInconvenience(grid: list[list[int]]) -> int:
    return getMinInconvenience_Simple(grid)
