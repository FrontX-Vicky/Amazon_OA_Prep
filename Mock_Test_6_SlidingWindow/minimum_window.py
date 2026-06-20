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
    if t == "": return ""
    
    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
        
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("inf")
    l = 0
    
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        
        if c in countT and window[c] == countT[c]:
            have += 1
            
        while have == need:
            # Update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
                
            # Pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
            
    l, r = res
    return s[l:r+1] if resLen != float("inf") else ""
