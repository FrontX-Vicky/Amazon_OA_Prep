import pytest
from shortest_subarray import shortestSubarray

class TestMock4:

    def test_shortest_subarray_1(self):
        nums = [1]
        k = 1
        assert shortestSubarray(nums, k) == 1

    def test_shortest_subarray_2(self):
        nums = [1,2]
        k = 4
        assert shortestSubarray(nums, k) == -1

    def test_shortest_subarray_3(self):
        # A standard sliding window will fail on this test case!
        nums = [2,-1,2]
        k = 3
        assert shortestSubarray(nums, k) == 3

    def test_shortest_subarray_4(self):
        # Extreme test case with multiple negatives
        nums = [84,-37,32,40,95]
        k = 167
        assert shortestSubarray(nums, k) == 3

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_4.py"])
