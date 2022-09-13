from typing import List, Tuple


def dijkstra_array(graph: List[List[List[int]]], src: int, tgt: int) -> Tuple[List[int], int]:
    """Dijkstra algorythm using array, not priority queue.

    Args:
        graph (List[List[List[int]]]): Adjacency list of a directed weighted graph. w = graph[v][u] means there is v->u edge with cost w.
        src (int): Source node
        dst (int): Destination node

    Returns:
        Tuple[List[int], int]: Shortest path from src to dst, and weight of the shortest path.
    """


def dijkstra_pq(graph: List[List[List[int]]], src: int, tgt: int) -> Tuple[List[int], int]:
    """Dijkstra algorythm using priority queue.

    Args:
        graph (List[List[List[int]]]): Adjacency list of a directed weighted graph. w = graph[v][u] means there is v->u edge with cost w.
        src (int): Source node
        dst (int): Destination node

    Returns:
        Tuple[List[int], int]: Shortest path from src to dst, and weight of the shortest path.
    """
    pass
