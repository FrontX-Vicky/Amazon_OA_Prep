import pytest
from coin_change import coinChange

class TestMock5DP:

    def test_coin_change_1(self):
        coins = [1, 2, 5]
        amount = 11
        assert coinChange(coins, amount) == 3

    def test_coin_change_2(self):
        coins = [2]
        amount = 3
        assert coinChange(coins, amount) == -1

    def test_coin_change_3(self):
        coins = [1]
        amount = 0
        assert coinChange(coins, amount) == 0
        
    def test_coin_change_4(self):
        # LLM-proof check: Greedy approach fails here!
        # Greedy takes 4 -> 2 -> 1,1 (3 coins)
        # Optimal is 3 -> 3 (2 coins)
        coins = [1, 3, 4]
        amount = 6
        assert coinChange(coins, amount) == 2
        
    def test_coin_change_5(self):
        # Edge case: amount is exactly equal to one of the coins
        coins = [1, 2, 5]
        amount = 5
        assert coinChange(coins, amount) == 1

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_5_dp.py"])
