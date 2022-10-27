import unittest  # The test framework
import toporogical_sort  # The code to test


class Test_TestToporogicalSort(unittest.TestCase):
    def test_toporogical_sort(self):
        cases = [
            {"edges": [[]], "msg": "one node"},
            {"edges": [[5], [3, 6], [5, 7], [0, 7], [1, 6], [], [7], []], "msg": "big graph",},
            {"edges": [[], [], [], []], "msg": "empty edge"},
            {"edges": [[1], [], [], []], "msg": "almost empty edge"},
        ]

        for i, c in enumerate(cases):
            msg = c.get("msg", i)
            with self.subTest(msg=msg):
                n = len(c["edges"])

                got = toporogical_sort.toporogical_sort(c["edges"])
                self.assertEqual(len(got), n)

                index = {}
                for j, v in enumerate(got):
                    index[v] = j

                for v in range(n):
                    self.assertTrue(v in index)

                for v, edge in enumerate(c["edges"]):
                    for u in edge:
                        self.assertGreater(index[u], index[v])
