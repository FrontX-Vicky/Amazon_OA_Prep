import pytest
from course_schedule import canFinish

class TestMock7:

    def test_can_finish_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        assert canFinish(numCourses, prerequisites) == True

    def test_can_finish_2(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        assert canFinish(numCourses, prerequisites) == False

    def test_can_finish_3(self):
        # A valid linear chain: 0 -> 1 -> 2 -> 3
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2]]
        assert canFinish(numCourses, prerequisites) == True
        
    def test_can_finish_4(self):
        # Disconnected components (valid)
        numCourses = 5
        prerequisites = [[1, 0], [3, 2]]
        assert canFinish(numCourses, prerequisites) == True
        
    def test_can_finish_5(self):
        # Complex graph with a cycle deep inside: 0->1->2, 2->3, 3->1
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2], [1, 3]]
        assert canFinish(numCourses, prerequisites) == False

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_7.py"])
