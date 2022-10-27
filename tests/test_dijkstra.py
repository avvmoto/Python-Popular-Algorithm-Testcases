import math
import unittest  # The test framework
import dijkstra  # The code to test

cases = [
    {
        "g": [[[1, 1]], [[2, 3]], []],
        "s": 0,
        "t": 2,
        "dist": 4,
        "shortest": [0, 1, 2],
        "msg": "simple",
    },
    {
        "g": [
            [[1, 3], [2, 5]],
            [[2, 4], [3, 12]],
            [[3, 9], [4, 4]],
            [[5, 2]],
            [[3, 7], [5, 8]],
            [],
        ],
        "s": 0,
        "t": 5,
        "dist": 16,
        "shortest": [0, 2, 3, 5],
        "msg": "big graph",
    },
    {
        "g": [
            [[1, 3], [2, 5]],
            [[2, 4], [3, 12]],
            [[3, 9], [4, 4]],
            [[5, 2]],
            [[3, 7], [5, 8]],
            [],
        ],
        "s": 0,
        "t": 4,
        "dist": 9,
        "shortest": [0, 2, 4],
        "msg": "big graph midddle path",
    },
    {
        "g": [[[1, 1]], []],
        "s": 0,
        "t": 1,
        "dist": 1,
        "shortest": [0, 1],
        "msg": "smallest graph",
    },
    {
        "g": [[[1, 1]], [], []],
        "s": 0,
        "t": 2,
        "dist": math.inf,
        "shortest": [],
        "msg": "no route",
    },
    {
        "g": [[[1, 3], [2, 1]], [[3, 1]], [[1, 1]], []],
        "s": 0,
        "t": 3,
        "dist": 3,
        "shortest": [0, 2, 1, 3],
        "msg": "cause old queue",
    },
    {
        "g": [[], [], []],
        "s": 0,
        "t": 2,
        "dist": math.inf,
        "shortest": [],
        "msg": "empty edge",
    },
    {
        "g": [[], [], [], [[2, 1]]],
        "s": 0,
        "t": 2,
        "dist": math.inf,
        "shortest": [],
        "msg": "min_v == -1 killer",
    },
    {
        "g": [[[1, 1], [2, 1]], [[3, 1]], [[3, 1]], []],
        "s": 0,
        "t": 3,
        "dist": 2,
        "shortest": [0, 1, 3],
        "msg": "exists same cost",
    },
]


class Test_TestDijkstra(unittest.TestCase):
    def test_dijkstra_array(self):
        for i, c in enumerate(cases):
            msg = c.get("msg", i)
            with self.subTest(msg=msg):
                shortest, dist = dijkstra.dijkstra_array(c["g"], c["s"], c["t"])

                if math.isinf(c["dist"]):
                    self.assertEqual(math.isinf(dist), True)
                    continue

                self.assertEqual(dist, c["dist"])
                self.assertEqual(shortest, c["shortest"])

    def test_dijkstra_pq(self):
        for i, c in enumerate(cases):
            msg = c.get("msg", i)
            with self.subTest(msg=msg):
                shortest, dist = dijkstra.dijkstra_pq(c["g"], c["s"], c["t"])

                if math.isinf(c["dist"]):
                    self.assertEqual(math.isinf(dist), True)
                    continue

                self.assertEqual(dist, c["dist"])
                self.assertEqual(shortest, c["shortest"])
