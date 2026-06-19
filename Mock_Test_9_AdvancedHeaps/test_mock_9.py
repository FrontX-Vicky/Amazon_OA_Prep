import pytest
from find_median import MedianFinder

class TestMock9:

    def test_median_finder_1(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5
        mf.addNum(3)
        assert mf.findMedian() == 2.0

    def test_median_finder_2(self):
        mf = MedianFinder()
        mf.addNum(5)
        assert mf.findMedian() == 5.0
        mf.addNum(1)
        assert mf.findMedian() == 3.0
        mf.addNum(3)
        assert mf.findMedian() == 3.0
        
    def test_median_finder_3(self):
        mf = MedianFinder()
        # Adding negative numbers
        mf.addNum(-1)
        assert mf.findMedian() == -1.0
        mf.addNum(-2)
        assert mf.findMedian() == -1.5
        mf.addNum(-3)
        assert mf.findMedian() == -2.0

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_9.py"])
