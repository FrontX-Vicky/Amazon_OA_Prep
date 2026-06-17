# Amazon SDE II - DSA Patterns Cheatsheet (Python)

Since you want to maximize pattern recognition without wasting time typing out boilerplate, here are the highest-yield patterns for Amazon OAs with the optimal Python code and explanation. 

Amazon heavily tests: **Arrays/Strings, Hash Maps, Sliding Window, Trees/Graphs (BFS/DFS), and Priority Queues (Heaps).**

---

## 1. Sliding Window (Longest / Substrings)
**When to use:** Problems asking for "longest/shortest substring, subarray, or max sum of contiguous elements".
**Pattern Idea:** Use two pointers (`left` and `right`) to represent a window. Expand `right` until a condition is violated, then shrink `left` until it's valid again.

**Example: Longest Substring Without Repeating Characters**
```python
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # If character is in set, we shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the new character to the window
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        
    return max_len
```
**Explanation:** `right` pointer iterates through the string. If `s[right]` is already in `char_set`, we remove elements from the `left` until the duplicate is gone. We update the `max_len` at each valid step.

---

## 2. Two Pointers (Sorted Arrays / Palindromes)
**When to use:** Searching pairs in a sorted array, palindrome checks, or merging intervals.

**Example: 3Sum (Find all unique triplets that sum to 0)**
```python
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort() # Sorting is crucial for Two Pointer approach
    
    for i, a in enumerate(nums):
        # Skip positive integers (can't sum to 0) and duplicates for `a`
        if a > 0: break
        if i > 0 and a == nums[i - 1]: continue
            
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = a + nums[left] + nums[right]
            
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for `left` pointer
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                    
    return res
```
**Explanation:** Sort the array first. Iterate with index `i`. Treat `nums[i]` as the target for a Two Sum problem on the remaining array (`left` to `right`). Crucial detail: aggressively skip duplicates to ensure unique triplets.

---

## 3. Top K Elements (Heaps / Priority Queue)
**When to use:** "Find the Kth largest/smallest/most frequent element". Python's `heapq` module provides a Min-Heap by default.

**Example: Top K Frequent Elements**
```python
import heapq
from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Count frequencies: {element: count}
    count = Counter(nums)
    
    # Use a heap to keep track of the top k elements.
    # We store tuples of (frequency, element)
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        # If heap size exceeds k, pop the smallest frequency element
        if len(heap) > k:
            heapq.heappop(heap)
            
    # The heap now contains the top k elements
    return [item[1] for item in heap]
```
**Explanation:** Count frequencies first. Push `(freq, num)` to a min-heap. If the heap grows larger than `K`, pop the smallest. This keeps the time complexity at `O(N log K)`.

---

## 4. Breadth-First Search (BFS) on Graphs/Grids
**When to use:** Shortest path in an unweighted graph, finding the minimum steps to reach a target, level-order traversal.

**Example: Number of Islands (Grid problem)**
```python
from collections import deque

def numIslands(grid: list[list[str]]) -> int:
    if not grid: return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    visited = set() # Or mutate grid to '0' to save space
    
    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))
        
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == "1" and (nr, nc) not in visited):
                    q.append((nr, nc))
                    visited.add((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1
                
    return islands
```
**Explanation:** Iterate through every cell. When you find a `"1"` (land) that hasn't been visited, you've found a new island. Trigger a BFS to mark all connected `"1"`s as visited.

---

## 5. Depth-First Search (DFS) / Backtracking
**When to use:** Generating all permutations/combinations, searching through a tree/graph to the leaf nodes.

**Example: Word Search (Find if a word exists in a grid)**
```python
def exist(board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    path = set()
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or 
            r >= ROWS or c >= COLS or 
            word[i] != board[r][c] or 
            (r, c) in path):
            return False
            
        path.add((r, c))
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))
        path.remove((r, c)) # Backtrack!
        return res
        
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True
            
    return False
```
**Explanation:** At each cell, try to match `word[i]`. If it matches, mark it as visited (`path.add`) and recursively explore 4 directions. **Crucial step**: `path.remove((r, c))` after the recursive calls so the cell can be used in different paths.
