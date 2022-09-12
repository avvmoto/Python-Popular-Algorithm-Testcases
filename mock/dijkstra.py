from collections import deque
import heapq
import math
from typing import List, Tuple

def dijkstra_array(g: List[List[List[int]]], s: int, t:int) -> Tuple[List[int], int]:
    n = len(g)
    dist = [math.inf] * n
    prev = [-1] * n
    done = [False] * n

    dist[s]=0

    for _ in range(n-1):
        min_dist = math.inf
        v = -1
        for u in range(n):
            if not done[u] and dist[u] < min_dist:
                v = u
                min_dist = dist[u]
        
        if v == t or v == -1:
            break

        for u, weight in g[v]:
            new_dist = min_dist + weight
            if new_dist < dist[u]:
                dist[u] = new_dist
                prev[u] = v

        done[v] = True

    if math.isinf(dist[t]):
        return [], math.inf

    shortest = [t]
    while shortest[-1]!=s:
        shortest.append(prev[shortest[-1]])
    shortest.reverse()
    return shortest, dist[t]


def dijkstra_pq(g: List[List[List[int]]], s: int, t:int) -> Tuple[List[int], int]:
    n = len(g)
    dist = [math.inf] * n
    prev = [-1] * n
    dist[s] = 0
    q = [(0, s)]

    while q:
        d, v = heapq.heappop(q)

        if v == t:
            break

        if d > dist[v]:
            continue

        for u, weight in g[v]:
            new_dist = dist[v] + weight
            if new_dist < dist[u]:
                dist[u] = new_dist
                prev[u] = v
                heapq.heappush(q, (new_dist, u))

    if math.isinf(dist[t]):
        return [], math.inf

    shortest = [t]
    while shortest[-1] != s:
        shortest.append(prev[shortest[-1]])
    shortest.reverse()    

    return shortest, dist[t]