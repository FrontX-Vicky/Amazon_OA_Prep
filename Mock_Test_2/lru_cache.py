# Problem 2: LRU Cache
#
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# 
# Implement the LRUCache class:
# - LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
# - int get(int key): Return the value of the key if the key exists, otherwise return -1.
# - void put(int key, int value): Update the value of the key if the key exists. 
#   Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
#   evict the least recently used key.
#
# The functions get and put must each run in O(1) average time complexity.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key -> Node
        
        # Dummy nodes to make edge cases (empty list) easier
        # left = Least Recently Used (LRU)
        # right = Most Recently Used (MRU)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Helper 1: Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper 2: Insert node right before the right dummy (make it MRU)
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right
        
        prev_node.next = node
        next_node.prev = node
        
        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Find the node, snip it out of its current position, 
            # and append it to the MRU side (right side)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If it exists, remove the old node
            self.remove(self.cache[key])
            
        # Create a new node and make it MRU
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # Check capacity
        if len(self.cache) > self.capacity:
            # Evict the LRU (which is exactly next to the left dummy node)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] 