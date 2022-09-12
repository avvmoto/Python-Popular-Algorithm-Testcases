import unittest  # The test framework
import union_find  # The code to test


class Test_TestUnionFind(unittest.TestCase):
    def test_union_find(self):
        n = 10
        uf = union_find.UnionFind(n)

        # initial state
        for a in range(1, n):
            self.assertEqual(False, uf.isSame(0, a))

        # unite(0,1)
        uf.unite(0, 1)
        self.assertEqual(True, uf.isSame(0, 1))
        for a in range(2, n):
            self.assertEqual(False, uf.isSame(0, a))

        # group (0, 1, 2), (3,4)
        uf.unite(2, 1)
        uf.unite(3, 4)
        self.assertEqual(True, uf.isSame(0, 1))
        self.assertEqual(True, uf.isSame(0, 2))
        self.assertEqual(True, uf.isSame(3, 4))
        self.assertEqual(False, uf.isSame(0, 5))


if __name__ == "__main__":
    unittest.main()
