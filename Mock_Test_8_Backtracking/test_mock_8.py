import pytest
from word_search import exist

class TestMock8:

    def test_exist_1(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        assert exist(board, word) == True

    def test_exist_2(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        assert exist(board, word) == True

    def test_exist_3(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        assert exist(board, word) == False
        
    def test_exist_4(self):
        # LLM-proof check: State reversion test. 
        # If they don't revert state, they will fail to find 'A' again if an earlier path marked it.
        board = [["A", "A", "A", "A"], ["A", "A", "A", "A"], ["A", "A", "A", "B"]]
        word = "AAAAAAAAAAAB"
        assert exist(board, word) == True

if __name__ == "__main__":
    pytest.main(["-v", "test_mock_8.py"])
