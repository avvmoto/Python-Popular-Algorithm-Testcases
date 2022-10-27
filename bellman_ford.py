import math
from typing import List, Tuple


def bellman_ford(graph: List[List[List[int]]], src: int, dst: int) -> Tuple[List[int], int, bool]:
    """Bellman-Ford algorythm.

    Args:
        graph (List[List[List[int]]]): Adjacency list of a directed weighted graph. graph[v] = [u_i, weight_i] means there is v->u_i edge with cost weight_i.
        src (int): Source node
        dst (int): Destination node

    Returns:
        List[int]: Shortest path from src to dst. If not exist, returns [].
        int: The cost of the shortest path. If not exist, returns math.inf.
        bool: Return True if and only if there is a reachable negative cycle from src.
    """

    nodes_num = len(graph)
    dist = [math.inf] * nodes_num
    prev = [-1] * nodes_num

    dist[src] = 0
    has_negative_cycle = False

    for i in range(nodes_num):
        updated = False

        for v in range(nodes_num):
            for u, weight in graph[v]:
                new_dist = dist[v] + weight

                if new_dist < dist[u]:
                    updated = True
                    dist[u] = new_dist
                    prev[u] = v

        if not updated:
            break

        if i == nodes_num - 1 and updated:
            has_negative_cycle = True

    if has_negative_cycle or math.isinf(dist[dst]):
        return [], math.inf, has_negative_cycle

    shortest = [dst]
    while shortest[-1] != src:
        shortest.append(prev[shortest[-1]])
    shortest.reverse()

    return shortest, dist[dst], False
