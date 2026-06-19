import pytest
from house_robber import rob

class TestMock5P2:

    def test_rob_1(self):
        nums = [1, 2, 3, 1]
        assert rob(nums) == 4

    def test_rob_2(self):
        nums = [2, 7, 9, 3, 1]
        assert rob(nums) == 12

    def test_rob_3(self):
        # Edge case: Only 1 house
        nums = [5]
        assert rob(nums) == 5
        
    def test_rob_4(self):
        # Edge case: 2 houses
        nums = [5, 10]
        assert rob(nums) == 10
        
    def test_rob_5(self):
        # LLM-proof check: Greedy (picking evens vs odds) FAILS here!
        # Evens: 2 + 3 = 5
        # Odds: 1 + 9 + 1 = 11
        # Optimal: 2 + 9 + 1 = 12 (Rob indices 0, 2, 4)
        nums = [2, 1, 9, 3, 1]
        assert rob(nums) == 12
        
    def test_rob_6(self):
        # Another test where you skip TWO houses to get a better payout
        nums = [2, 1, 1, 2]
        # Optimal is index 0 and index 3 = 2 + 2 = 4
        assert rob(nums) == 4

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_5_p2.py"])
