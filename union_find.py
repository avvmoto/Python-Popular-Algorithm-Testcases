class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [-1] * n
        self.size = [1] * n

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)

        if self.size[b] > self.size[a]:
            a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]

    def isSame(self, a, b):
        return self.root(a) == self.root(b)

    def root(self, a):
        v = a
        while self.parent[v] != -1:
            v = self.parent[v]

        if self.parent[a] != -1:
            self.parent[a] = v
        return v
