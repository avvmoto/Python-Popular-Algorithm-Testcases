import heapq
from typing import List, Tuple
import math


def dijkstra_array(graph: List[List[List[int]]], src: int, tgt: int) -> Tuple[List[int], int]:
    """Dijkstra algorythm using array, not priority queue.

    Args:
        graph (List[List[List[int]]]): Adjacency list of a directed weighted graph. graph[v] = [u_i, weight_i] means there is v->u_i edge with cost weight_i.
        src (int): Source node.
        dst (int): Destination node.

    Returns:
        Tuple[List[int], int]: Shortest path from src to dst, and weight of the shortest path. Returns ([], math.inf) if theres no rote.
    """
    n = len(graph)
    dist = [math.inf] * n
    prev = [-1] * n
    seen = [False] * n

    dist[src] = 0

    for _ in range(n - 1):
        min_dist = math.inf
        min_v = -1

        for v in range(n):
            if dist[v] < min_dist and not seen[v]:
                min_dist = dist[v]
                min_v = v

        seen[min_v] = True
        if min_v == tgt:
            break

        if min_v == -1:
            break

        for u, weight in graph[min_v]:
            if dist[min_v] + weight < dist[u]:
                dist[u] = dist[min_v] + weight
                prev[u] = min_v

    if math.isinf(dist[tgt]):
        return [], dist[tgt]

    shortest = [tgt]
    while shortest[-1] != src:
        shortest.append(prev[shortest[-1]])
    shortest.reverse()

    return shortest, dist[tgt]


def dijkstra_pq(graph: List[List[List[int]]], src: int, tgt: int) -> Tuple[List[int], int]:
    """Dijkstra algorythm using priority queue.

    Args:
        graph (List[List[List[int]]]): Adjacency list of a directed weighted graph. graph[v] = [u_i, weight_i] means there is v->u_i edge with cost weight_i.
        src (int): Source node.
        dst (int): Destination node.

    Returns:
        Tuple[List[int], int]: Shortest path from src to dst, and weight of the shortest path. Returns ([], math.inf) if theres no rote.
    """
    n = len(graph)
    dist = [math.inf] * n
    prev = [-1] * n

    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, v = heapq.heappop(pq)

        if v == tgt:
            break

        if dist[v] < d:
            continue

        for u, weight in graph[v]:
            new_dist = d + weight

            if new_dist < dist[u]:
                dist[u] = new_dist
                prev[u] = v

                heapq.heappush(pq, (new_dist, u))

    if math.isinf(dist[tgt]):
        return [], math.inf

    shortest_path = [tgt]
    while shortest_path[-1] != src:
        shortest_path.append(prev[shortest_path[-1]])
    shortest_path.reverse()

    return shortest_path, dist[tgt]
