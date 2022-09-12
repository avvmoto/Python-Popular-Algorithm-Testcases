import sort  # The code to test
import unittest  # The test framework


class Test_TestQuickSelect(unittest.TestCase):
    def test_quick_select(self):
        cases = [
            [5, 4, 3, 2, 1],
            [],
            [9],
            [1, 2, 3, 4, 5, 6],
            [1, 3],
            [2, 1],
            [3, 2, 4, 5, 1, 9],
            [1, 1, 2, 2, 2, 3, 3, 3, 4],
            [0, 0, 0, 0, 0],
        ]

        for c in cases:
            with self.subTest(msg=c):
                for _ in range(100):
                    for k in range(len(c)):
                        expected = sorted(c)[:k]
                        got = sort.quick_select(c, k)
                        self.assertEqual(sorted(got), expected)


class Test_TestQuickSort(unittest.TestCase):
    def test_sort(self):
        cases = [
            [5, 4, 3, 2, 1],
            [],
            [9],
            [1, 2, 3, 4, 5, 6],
            [1, 3],
            [2, 1],
            [3, 2, 4, 5, 1, 9],
            [1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
        ]

        for c in cases:
            with self.subTest(msg=c):
                expected = sorted(c)
                sort.quick_sort(c)
                self.assertEqual(c, expected)


if __name__ == "__main__":
    unittest.main()
