import unittest
from evolving_prefix import countBalancedSubarrays

class TestEvolvingPrefix(unittest.TestCase):
    def test_basic(self):
        # "AABA", K = 1.
        # "A", "A" (from index 1), "AAB", "ABA"
        self.assertEqual(countBalancedSubarrays("AABA", 1), 4)

    def test_zero_k(self):
        # K=0 means exactly equal number of A and B
        # "AB", "BA", "AB" (from index 2), "ABAB"
        self.assertEqual(countBalancedSubarrays("ABAB", 0), 4)

    def test_all_same(self):
        # Subarrays of length 2 have exactly 2 A's.
        # "AA" (idx 0-1), "AA" (idx 1-2), "AA" (idx 2-3)
        self.assertEqual(countBalancedSubarrays("AAAA", 2), 3)

    def test_large_k(self):
        # K is larger than the string length
        self.assertEqual(countBalancedSubarrays("AB", 5), 0)

if __name__ == '__main__':
    unittest.main()
