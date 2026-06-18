import pytest
from k_closest_points import kClosest
from rotting_oranges import orangesRotting

class TestMock1:

    def test_k_closest_1(self):
        # The distance between (1, 3) and the origin is sqrt(10).
        # The distance between (-2, 2) and the origin is sqrt(8).
        # Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        points = [[1, 3], [-2, 2]]
        k = 1
        res = kClosest(points, k)
        assert len(res) == 1
        assert res[0] == [-2, 2]

    def test_k_closest_2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        res = kClosest(points, k)
        assert len(res) == 2
        # Order doesn't matter, so we sort before asserting
        assert sorted(res) == [[-2, 4], [3, 3]]


    def test_rotting_oranges_1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        assert orangesRotting(grid) == 4

    def test_rotting_oranges_2(self):
        # The orange in the bottom left corner (row 2, column 0) is never rotten
        # because rotting only happens 4-directionally.
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        assert orangesRotting(grid) == -1

    def test_rotting_oranges_3(self):
        # Since there are already no fresh oranges at minute 0, the answer is just 0.
        grid = [[0,2]]
        assert orangesRotting(grid) == 0

if __name__ == "__main__":
    pytest.main(["-v", "test_mock.py"])
