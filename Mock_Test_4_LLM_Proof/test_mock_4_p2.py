import pytest
from shortest_path_obstacles import shortestPath

class TestMock4P2:

    def test_shortest_path_1(self):
        grid = [
            [0,0,0],
            [1,1,0],
            [0,0,0],
            [0,1,1],
            [0,0,0]
        ]
        k = 1
        assert shortestPath(grid, k) == 6

    def test_shortest_path_2(self):
        grid = [
            [0,1,1],
            [1,1,1],
            [1,0,0]
        ]
        k = 1
        assert shortestPath(grid, k) == -1
        
    def test_shortest_path_3(self):
        # Edge case: No obstacles needed
        grid = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        k = 0
        assert shortestPath(grid, k) == 4
        
    def test_shortest_path_4(self):
        # A test case where visiting the same node again is REQUIRED to find the optimal path
        # if the first visit destroyed too many walls.
        grid = [
            [0,1,0,0,0],
            [0,1,0,1,0],
            [0,0,0,1,0]
        ]
        k = 1
        assert shortestPath(grid, k) == 6

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_4_p2.py"])
