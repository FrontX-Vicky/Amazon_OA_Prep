# Phase 7: Advanced Backtracking
# 
# Problem: Word Search
#
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
# are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

def exist(board: list[list[str]], word: str) -> bool:
    # TODO: Implement your solution here
    # 
    # LLM-Proof Hint: This requires DFS with State Reversion (Backtracking).
    # When you visit a cell, you must mark it as visited (e.g., change it to '#') 
    # so you don't use it twice in the SAME path.
    # CRITICAL: If the path fails, you MUST change it back to its original character
    # before returning, so other paths can use it!
    pass
