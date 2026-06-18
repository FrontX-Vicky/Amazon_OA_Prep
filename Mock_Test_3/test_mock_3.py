import pytest
from number_of_islands import numIslands
from container_with_most_water import maxArea

class TestMock3:

    def test_number_of_islands_1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        assert numIslands(grid) == 1

    def test_number_of_islands_2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        assert numIslands(grid) == 3

    def test_max_area_1(self):
        height = [1,8,6,2,5,4,8,3,7]
        assert maxArea(height) == 49

    def test_max_area_2(self):
        height = [1,1]
        assert maxArea(height) == 1

    def test_max_area_3(self):
        height = [4,3,2,1,4]
        assert maxArea(height) == 16

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_3.py"])
