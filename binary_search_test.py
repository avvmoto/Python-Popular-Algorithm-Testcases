import bisect
import binary_search  # The code to test
import unittest  # The test framework


class Test_TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        cases = [
            [],
            [1],
            [-1],
            [0],
            [1, 3],
            [0, 3],
            [1, 2, 3, 4, 5, 6],
            [1, 1, 2, 2, 2, 3, 3, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4],
            [-1, -1, 0, 1, 1],
            [2, 4, 6, 8, 9, 9, 9, 12],
        ]

        for c in cases:
            with self.subTest(msg=c):
                prev = 1 << 30
                for i in range(len(c)):
                    if prev == c[i]:
                        continue
                    prev = c[i]
                    expected = bisect.bisect_left(c, c[i])
                    got = binary_search.binary_search(c, c[i])
                    self.assertEqual(got, expected)


if __name__ == "__main__":
    unittest.main()
