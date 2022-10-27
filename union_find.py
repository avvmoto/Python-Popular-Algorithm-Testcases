class UnionFind:
    """UnionFind provides Union Find algotytm for node 0..n-1 ."""

    def __init__(self, n: int) -> None:
        self.size = [1] * n
        self.parent = [-1] * n

    def unite(self, a: int, b: int) -> None:
        """unite unites node a and node b as a same group.

        Args:
            a (int): A node. Must within [0, n-1].
            b (int): A node. Must within [0, n-1].
        """

        a = self.root(a)
        b = self.root(b)

        if a == b:
            return

        if self.size[a] < self.size[b]:
            a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]

    def isSame(self, a: int, b: int) -> bool:
        """isSame returns True if and only if node a and node b are same group.

        Args:
            a (int): A node. Must within [0, n-1] .
            b (int): A node. Must within [0, n-1] .

        Returns:
            bool: True if node a and node b are same group.
        """
        return self.root(a) == self.root(b)

    def root(self, a):
        v = a
        while self.parent[v] != -1:
            v = self.parent[v]

        if v != a:
            self.parent[a] = v
        return v
