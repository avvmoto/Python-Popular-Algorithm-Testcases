import unittest  # The test framework
import union_find  # The code to test


class Test_TestUnionFind(unittest.TestCase):
    def test_union_find(self):
        n = 10
        uf = union_find.UnionFind(n)

        # initial state
        for a in range(1, n):
            self.assertFalse(uf.isSame(0, a))

        # unite(0,1)
        uf.unite(0, 1)
        self.assertTrue(uf.isSame(0, 1))
        for a in range(2, n):
            self.assertFalse(uf.isSame(0, a))

        # group (0, 1, 2), (3,4)
        uf.unite(2, 1)
        uf.unite(3, 4)
        self.assertTrue(uf.isSame(0, 1))
        self.assertTrue(uf.isSame(0, 2))
        self.assertTrue(uf.isSame(3, 4))
        self.assertFalse(uf.isSame(0, 5))

        # swap internaly
        uf.unite(3, 0)
        self.assertTrue(uf.isSame(1, 4))

        # unite within same group
        uf.unite(0, 1)
        self.assertTrue(uf.isSame(1, 4))
        self.assertFalse(uf.isSame(0, 5))
