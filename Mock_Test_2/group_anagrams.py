# Problem 1: Group Anagrams
#
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
#
# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # TODO: Implement your solution here
    # Hint: A Hash Map (or collections.defaultdict) is your best friend here. 
    # What can you use as a consistent dictionary key for words that are anagrams?
    # Use defaultdict to avoid checking if a key exists before appending
    
    # STEP 1: Initialization
    # We use defaultdict(list). If we access a key that doesn't exist, 
    # it automatically creates an empty list for that key.
    anagram_map = defaultdict(list)
    
    # STEP 2: Iterate and Categorize
    for word in strs:
        # The Key: 
        # We sort the letters of the word. 
        # Anagrams will always result in the same sorted string.
        # Example: "eat" -> "aet", "tea" -> "aet"
        # Tuples are used because they are immutable and can be dictionary keys.
        sorted_key = tuple(sorted(word))
        
        # Append the original word to the list associated with its sorted key
        anagram_map[sorted_key].append(word)
        
    # STEP 3: Return the values
    # The values() of the dictionary are the lists of anagrams we just created.
    return list(anagram_map.values())
