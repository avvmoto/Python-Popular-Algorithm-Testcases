import heapq
import math
from typing import List, Tuple


def dijkstra_array(
    graph: List[List[List[int]]], src: int, tgt: int
) -> Tuple[List[int], int]:
    """Dijkstra algorythm using array.

    Args:
        graph (List[List[List[int]]]): Adjacency list of a directed weighted graph. graph[v] = [u_i, weight_i] means there is v->u_i edge with cost weight_i.
        src (int): Source node
        dst (int): Destination node

    Returns:
        Tuple[List[int], int]: Shortest path from src to dst, and weight of the shortest path. Returns ([], math.inf) if theres no rote.
    """
    n = len(graph)
    dist = [math.inf] * n
    prev = [-1] * n
    seen = [False] * n

    dist[src] = 0

    for _ in range(n - 1):
        min_v = 0
        min_dist = math.inf

        for v in range(n):
            if dist[v] < min_dist and not seen[v]:
                min_dist = dist[v]
                min_v = v

        seen[min_v] = True

        for u, weight in graph[min_v]:
            new_dist = min_dist + weight
            if new_dist < dist[u]:
                dist[u] = new_dist
                prev[u] = min_v

    shortest_path = []
    if not math.isinf(dist[tgt]):
        shortest_path.append(tgt)
        while shortest_path[-1] != src:
            shortest_path.append(prev[shortest_path[-1]])
        shortest_path.reverse()

    return shortest_path, dist[tgt]


def dijkstra_pq(
    graph: List[List[List[int]]], src: int, tgt: int
) -> Tuple[List[int], int]:
    """Dijkstra algorythm using priority queue.

    Args:
        graph (List[List[List[int]]]): Adjacency list of a directed weighted graph. graph[v] = [u_i, weight_i] means there is v->u_i edge with cost weight_i.
        src (int): Source node
        dst (int): Destination node

    Returns:
        Tuple[List[int], int]: Shortest path from src to dst, and weight of the shortest path. Returns ([], math.inf) if theres no rote.
    """

    n = len(graph)
    dist = [math.inf] * n
    prev = [-1] * n

    pq = [(src, 0)]
    dist[src] = 0

    while pq:
        v, d = heapq.heappop(pq)

        if v == tgt:
            break

        for u, weight in graph[v]:
            new_dist = d + weight
            if new_dist < dist[u]:
                prev[u] = v
                dist[u] = new_dist

                heapq.heappush(pq, (u, new_dist))

    shortest_path = []
    if not math.isinf(dist[tgt]):
        shortest_path.append(tgt)
        while shortest_path[-1] != src:
            shortest_path.append(prev[shortest_path[-1]])
        shortest_path.reverse()

    return shortest_path, dist[tgt]
