from typing import List


def toporogical_sort(edges: List[List[int]]) -> List[int]:
    output = []
    n = len(edges)
    seen = [False] * n

    def dfs(v):
        if seen[v]:
            return
        seen[v] = True
        for u in edges[v]:
            dfs(u)
        output.append(v)
        return

    for v in range(n):
        dfs(v)

    output.reverse()
    return output
