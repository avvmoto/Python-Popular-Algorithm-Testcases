from typing import List, Tuple


def washall_floyd(graph: List[List[List[int]]]) -> Tuple[List[List[int]], bool]:
    """Warshall-Floyd algorythm.

    Args:
        graph (List[List[List[int]]]): Adjacency list of a directed weighted graph. graph[v] = [u_i, weight_i] means there is v->u_i edge with cost weight_i.

    Returns:
        List(List[int]): Shortest path from src to dst. dp[i][j] is cost of the shortest path from i to j.
        bool: Return True if and only if there is a negative cycle.
    """
    n = len(graph)
    dp = [[float("inf")] * n for _ in range(n)]

    for v in range(n):
        for u, w in graph[v]:
            dp[v][u] = w

        dp[v][v] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    for v in range(n):
        if dp[v][v] < 0:
            return dp, True

    return dp, False
