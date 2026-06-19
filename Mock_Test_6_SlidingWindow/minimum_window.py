# Phase 5: Hard Sliding Window
# 
# Problem: Minimum Window Substring
#
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"

def minWindow(s: str, t: str) -> str:
    # TODO: Implement your solution here
    # 
    # LLM-Proof Hint: This requires TWO dynamically updating hashmaps (or arrays), 
    # and a variable tracking "have" vs "need" to keep it O(N).
    # Expand your right pointer until you have all the required characters.
    # Then, shrink your left pointer as much as possible while still having all required characters.
    pass
