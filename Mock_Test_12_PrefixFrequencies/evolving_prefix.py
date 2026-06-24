"""
AMAZON OA: Evolving Prefix Frequencies (Prefix Sum & Math)

You are analyzing a stream of packages arriving at a sorting facility. 
The packages are of two types: 'A' and 'B'.
Given a string `s` representing the packages, and an integer `K`, find the 
total number of contiguous subarrays where the absolute difference between the 
count of 'A' and the count of 'B' is EXACTLY `K`.

Example 1:
s = "AABA", K = 1
Output: 4
Explanation:
Subarrays with absolute difference 1: "A", "A", "AAB", "ABA"

THE TWIST (Why Sliding Window Fails):
If the problem asked for "difference <= K", you could easily use a Sliding Window.
However, because it asks for EXACTLY K, the difference `abs(count(A) - count(B))` 
goes up and down (it is NOT monotonically increasing). Therefore, the left pointer 
in a sliding window wouldn't know whether to shrink or stay still.

You MUST use a Prefix Sum approach combined with a HashMap to track mathematical invariants!
"""

def countBalancedSubarrays(s: str, k: int) -> int:
    # TODO: Implement your Prefix Hashmap solution here!
    pass
