import merge_sort  # The code to test
import unittest  # The test framework


class Test_TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        cases = [
            [5, 4, 3, 2, 1],
            [],
            [9],
            [1, 2, 3, 4, 5, 6],
            [1, 3],
            [2, 1],
            [3, 2, 4, 5, 1, 9],
            [3, 2, 4, 5, 1, 9, 0],
            [1, 1, 2, 2, 2, 3, 3, 3, 4],
            [0, 0, 0, 0, 0],
        ]

        for c in cases:
            with self.subTest(msg=c):
                expected = sorted(c)
                merge_sort.merge_sort(c)
                self.assertEqual(c, expected)


if __name__ == "__main__":
    unittest.main()
