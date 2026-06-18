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

class LRUCache:

    def __init__(self, capacity: int):
        # TODO: Initialize your data structures here
        self.cache = {}
        self.capacity = capacity
        self.order = []

    def get(self, key: int) -> int:
        # TODO: Implement get logic
        if key not in self.cache:
            return -1
        
        # Move the key to the end of the order list
        self.order.remove(key)
        self.order.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # TODO: Implement put logic
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) == self.capacity:
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
            self.cache[key] = value
            self.order.append(key)

    