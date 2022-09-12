import math
import unittest   # The test framework
import bellman_ford    # The code to test

class Test_TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        cases = [
            {
                "g": [[[1, 1]],[[2, 3]], []],
                "s": 0,
                "t": 2,
                "dist":4,
                "shortest":[0,1,2],
                "has_negative_circle": False,
            },
            {
                "g": [[[1, -1]],[[2, -3]], []],
                "s": 0,
                "t": 2,
                "dist":-4,
                "shortest":[0,1,2],
                "has_negative_circle": False,
                "msg": "simple negative path"
            },
            {
                "g": [[[1, -1]],[[0, 1]]],
                "s": 0,
                "t": 1,
                "dist":-1,
                "shortest":[0,1],
                "has_negative_circle": False,
                "msg": "two nodes"
            },
            {
                "g": [[[1, 3],[3,100]],[[3,57], [4,-4], [2,50]], [[3,-10], [4,-5], [5,100]],[[1,-5]],[[2,57],[3,25],[5,8]],[]],
                "s": 0,
                "t": 5,
                "dist":7,
                "shortest":[0,1,4,5],
                "has_negative_circle": False,
                "msg": "big graph"
            },
            {
                "g": [[[1, 100], [3, 0]], [[2, 0]], [], [[0, -100]]],
                "s": 0,
                "t": 1,
                "has_negative_circle": True,
                "msg": "reachable negative circle"
            },
            {
                "g": [[[1, 1]],[[2, 3]], [], [[4, -100]], [[3, -100]]],
                "s": 0,
                "t": 2,
                "dist":4,
                "shortest":[0,1,2],
                "has_negative_circle": False,
                "msg": "unreachable negative circle"
            },
            {
                "g": [[], []],
                "s": 0,
                "t": 1,
                "dist":math.inf,
                "has_negative_circle":False,
                "msg": "unreachable target"
            }                                                         
        ]

        for i, c in enumerate(cases):
            msg = c.get("msg", i)
            with self.subTest(msg=msg):
                n = len(c["g"])

                shortest, dist, has_negative_circle = bellman_ford.bellman_ford(c["g"], c["s"], c["t"])
                print(shortest, dist, has_negative_circle)
                self.assertEqual(has_negative_circle, c["has_negative_circle"])



                if not c["has_negative_circle"]:
                    if math.isinf(c["dist"]):
                        self.assertEqual(math.isinf(dist), True)
                        continue                    
                    self.assertEqual(dist, c["dist"])
                    self.assertEqual(shortest, c["shortest"])


if __name__ == '__main__':
    unittest.main()
