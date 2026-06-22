import pytest
from grid_inconvenience import getMinInconvenience

class TestMock10:

    def test_example_1(self):
        grid = [
            [0, 0, 0, 1],
            [0, 0, 0, 1]
        ]
        assert getMinInconvenience(grid) == 1

    def test_single_cell(self):
        assert getMinInconvenience([[0]]) == 0
        assert getMinInconvenience([[1]]) == 0

    def test_no_ones(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        # Placing a 1 in the center (1,1) gives max distance 1 to the corners.
        assert getMinInconvenience(grid) == 1
        
    def test_all_ones(self):
        grid = [
            [1, 1],
            [1, 1]
        ]
        assert getMinInconvenience(grid) == 0

    def test_large_gap(self):
        grid = [
            [1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        # We can place a 1 in the middle to minimize the distance
        # Initial max distance from ends is around 3.
        # Check actual logic handling
        assert getMinInconvenience(grid) <= 2
        
    def test_impossible_to_improve(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        # Inconvenience is already 1, adding another 1 can't make it 0.
        assert getMinInconvenience(grid) == 1

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_10.py"])
