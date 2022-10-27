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
    pass
