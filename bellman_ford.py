import math
from typing import List, Tuple

def bellman_ford(g: List[List[List[int]]], s: int, t: int) -> Tuple[List[int], int, bool]:
    n = len(g)
    dist = [math.inf] * n
    prev = [-1] * n

    dist[s]=0
    negative_roop = False
    for i in range(n):
        updated = False
        for v in range(n):
            for u, weight in g[v]:
                new_weight = dist[v]+weight
                if dist[u]>new_weight:
                    dist[u]=new_weight
                    prev[u]=v
                    updated=True

        if i == n-1 and updated:
            negative_roop = True

    shortest = []
    if not negative_roop and not math.isinf(dist[t]):
        shortest = [t]
        while shortest[-1] != s:
            shortest.append(prev[shortest[-1]])
        shortest.reverse()

    return shortest, dist[t], negative_roop