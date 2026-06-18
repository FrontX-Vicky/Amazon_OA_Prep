import pytest
from group_anagrams import groupAnagrams
from lru_cache import LRUCache

class TestMock2:

    def test_group_anagrams_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        res = groupAnagrams(strs)
        # Sort each inner list and the outer list to safely compare unordered sets
        res_sorted = sorted([sorted(group) for group in res])
        expected = sorted([sorted(["bat"]), sorted(["nat","tan"]), sorted(["ate","eat","tea"])])
        assert res_sorted == expected

    def test_group_anagrams_2(self):
        strs = [""]
        res = groupAnagrams(strs)
        assert res == [[""]]

    def test_group_anagrams_3(self):
        strs = ["a"]
        res = groupAnagrams(strs)
        assert res == [["a"]]

    def test_lru_cache_1(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1) # cache is {1=1}
        lRUCache.put(2, 2) # cache is {1=1, 2=2}
        assert lRUCache.get(1) == 1    # return 1
        lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        assert lRUCache.get(2) == -1   # returns -1 (not found)
        lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        assert lRUCache.get(1) == -1   # return -1 (not found)
        assert lRUCache.get(3) == 3    # return 3
        assert lRUCache.get(4) == 4    # return 4

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_2.py"])
