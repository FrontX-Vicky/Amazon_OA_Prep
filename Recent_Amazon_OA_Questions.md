# Top Amazon OA & Interview Questions (Last 6 Months - 2026)

Based on recent reports from LeetCode Discuss and Blind for Amazon SDE Online Assessments in 2026, here are the highest-frequency questions you need to grind. 

Amazon is currently heavily indexing on **Arrays/Strings (Prefix Sums, Two Pointers)**, **Graphs (BFS/DFS)**, and **Priority Queues (Heaps)**. They are also introducing more "LLM-proof" problems that require state maintenance or logic rather than just memorizing a template.

---

## 1. Arrays, Strings, & Two Pointers
These are the most common "Question 1" problems in the OA. They test your ability to optimize `O(N^2)` brute-force solutions down to `O(N)` or `O(N log N)`.

*   **Two Sum** (Classic, but expect variations like Two Sum Less Than K)
*   **Three Sum** (3Sum) - *You practiced this in the Visualizer!*
*   **Container With Most Water** - *You nailed this in Mock Test 3!*
*   **Trapping Rain Water** (Hard - Very high frequency for SDE 2)
*   **Longest Substring Without Repeating Characters** (Sliding Window)
*   **Minimum Window Substring** (Hard Sliding Window)
*   **Group Anagrams** - *You nailed this in Mock Test 2!*
*   **Reorder Data in Log Files** (Amazon specific classic string parsing)
*   **String to Integer (atoi)**

## 2. Graphs & Matrices (BFS / DFS)
Amazon loves 2D grids. Expect at least one grid traversal problem.

*   **Number of Islands** - *You nailed this in Mock Test 3!*
*   **Rotting Oranges** (Multi-source BFS) - *You nailed this in Mock Test 1!*
*   **Word Search** (DFS with Backtracking)
*   **Snakes and Ladders** (BFS for shortest path)
*   **Course Schedule** (Topological Sort / Cycle Detection in Directed Graph)
*   **Pacific Atlantic Water Flow** (DFS from edges)

## 3. Priority Queues (Min/Max Heaps)
Whenever a question asks for the "Top K", "Kth largest", or "Minimum cost to connect...", immediately think of Heaps.

*   **K Closest Points to Origin** - *You nailed this in Mock Test 1!*
*   **Top K Frequent Elements / Words**
*   **Merge K Sorted Lists** (Hard)
*   **Find Median from Data Stream** (Hard - Two Heaps pattern)
*   **Minimum Cost to Connect Sticks** (Greedy + Heap)

## 4. Linked Lists & Object-Oriented Design
These are heavily tested to see if you understand pointers and state management.

*   **LRU Cache** (HashMap + Doubly Linked List) - *You nailed this in Mock Test 2!*
*   **Merge Two Sorted Lists**
*   **Copy List with Random Pointer** (Requires a Deep Copy HashMap)
*   **Reverse Nodes in k-Group** (Hard)
*   **Design Tic-Tac-Toe**

## 5. Dynamic Programming & Trees
Usually the harder "Question 2" in the OA.

*   **Best Time to Buy and Sell Stock** (And variations like Stock with Cooldown)
*   **Climbing Stairs** / **Coin Change**
*   **Word Break**
*   **Binary Tree Maximum Path Sum** (Hard)
*   **Lowest Common Ancestor of a Binary Tree**
*   **Diameter of Binary Tree**

---

### 🔥 2026 "LLM-Proof" Trends to Watch Out For:
Recently, Amazon has been twisting classic problems to break AI tools. 
1.  **Dynamic Constraints:** Instead of just finding the shortest path, you might have to find the shortest path where the "cost" of a step changes dynamically based on how many steps you've taken.
2.  **State Maintenance:** Problems where you have to simulate a process (like a conveyor belt of packages) and track multiple overlapping states over time.
3.  **Mathematical Invariants:** Problems that look like DP but can actually be solved in `O(N)` if you recognize a specific math trick or prefix-sum property.

**Strategy:** Focus heavily on the **Graphs** and **Heaps** lists above, as these are where you can pick up the most points in the 70-minute window.
