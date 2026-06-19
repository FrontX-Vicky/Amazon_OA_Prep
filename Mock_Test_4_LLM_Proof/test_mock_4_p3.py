import pytest
from minimum_cost_sticks import connectSticks

class TestMock4P3:

    def test_connect_sticks_1(self):
        sticks = [2, 4, 3]
        assert connectSticks(sticks) == 14

    def test_connect_sticks_2(self):
        sticks = [1, 8, 3, 5]
        assert connectSticks(sticks) == 30

    def test_connect_sticks_3(self):
        # Edge case: Only 1 stick costs 0 to connect
        sticks = [5]
        assert connectSticks(sticks) == 0
        
    def test_connect_sticks_4(self):
        # Edge case: All same lengths
        sticks = [2, 2, 2, 2]
        # 2+2=4 -> [2, 2, 4] -> cost 4
        # 2+2=4 -> [4, 4] -> cost 4
        # 4+4=8 -> [8] -> cost 8
        # total = 4 + 4 + 8 = 16
        assert connectSticks(sticks) == 16
        
    def test_connect_sticks_5(self):
        # LLM-proof check: Naive sorting fails here if they don't re-sort the combined stick!
        sticks = [3354, 4316, 3259, 4904, 4598, 474, 3166, 6322, 8080, 9009]
        assert connectSticks(sticks) == 151646

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_4_p3.py"])
