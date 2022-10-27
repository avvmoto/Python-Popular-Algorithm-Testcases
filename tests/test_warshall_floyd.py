import math
import unittest  # The test framework
import warshall_floyd  # The code to test
import dijkstra


class Test_TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        cases = [
            {
                "g": [[[1, 1]], [[2, 3]], []],
                "has_negative_cycle": False,
            },
            {
                "g": [[[1, -1]], [[2, -3]], []],
                "has_negative_cycle": False,
                "msg": "simple negative path",
            },
            {
                "g": [[[1, -1]], [[0, 1]]],
                "has_negative_cycle": False,
                "msg": "two nodes",
            },
            {
                "g": [
                    [[1, 3], [3, 100]],
                    [[3, 57], [4, -4], [2, 50]],
                    [[3, -10], [4, -5], [5, 100]],
                    [[1, -5]],
                    [[2, 57], [3, 25], [5, 8]],
                    [],
                ],
                "has_negative_cycle": False,
                "msg": "big graph",
            },
            {
                "g": [[[1, 100], [3, 0]], [[2, 0]], [], [[0, -100]]],
                "has_negative_cycle": True,
                "msg": "negative cycle",
            },
            {
                "g": [[[1, 1]], [[2, 3]], [], [[4, -100]], [[3, -100]]],
                "has_negative_cycle": True,
                "msg": "negative cycle2",
            },
            {
                "g": [[], []],
                "has_negative_cycle": False,
                "msg": "empty edge",
            },
        ]

        for i, c in enumerate(cases):
            msg = c.get("msg", i)
            with self.subTest(msg=msg):
                n = len(c["g"])

                shortest, has_negative_cycle = warshall_floyd.washall_floyd(c["g"])
                self.assertEqual(has_negative_cycle, c["has_negative_cycle"])
                if c["has_negative_cycle"]:
                    continue

                self.assertEqual(n, len(shortest))
                self.assertEqual(n, len(shortest[0]))

                for src in range(n):
                    for dst in range(n):
                        _, expected_dist = dijkstra.dijkstra_pq(c["g"], src, dst)
                        self.assertEqual(expected_dist, shortest[src][dst], msg="dist")
