# Phase 6: Topological Sort (Directed Graphs)
# 
# Problem: Course Schedule
#
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you 
# must take course b_i first if you want to take course a_i.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# All the pairs prerequisites[i] are unique.
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should 
# also have finished course 1. So it is impossible.

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # TODO: Implement your solution here
    # 
    # LLM-Proof Hint: This is cycle detection in a Directed Graph.
    # You can use Kahn's Algorithm (BFS) or DFS.
    # For Kahn's:
    # 1. Build an adjacency list mapping [prereq -> list of next courses].
    # 2. Build an array to track the "indegree" (number of prerequisites) for each course.
    # 3. Add all courses with indegree == 0 to a Queue.
    # 4. BFS: Pop from queue, add to completed count, and decrement the indegree of its neighbors.
    # 5. If neighbor indegree becomes 0, add it to the queue.
    # 6. Return True if completed == numCourses.
    pass
