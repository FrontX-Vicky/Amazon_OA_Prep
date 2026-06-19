import pytest
from minimum_window import minWindow

class TestMock6:

    def test_min_window_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        assert minWindow(s, t) == "BANC"

    def test_min_window_2(self):
        s = "a"
        t = "a"
        assert minWindow(s, t) == "a"

    def test_min_window_3(self):
        s = "a"
        t = "aa"
        assert minWindow(s, t) == ""
        
    def test_min_window_4(self):
        # LLM-proof check: Overlapping requirement
        s = "aaflslflsldkalskaaa"
        t = "aaa"
        assert minWindow(s, t) == "aaa"

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_6.py"])
