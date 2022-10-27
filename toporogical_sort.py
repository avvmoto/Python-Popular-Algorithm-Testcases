from typing import List


def toporogical_sort(edges: List[List[int]]) -> List[int]:
    """ Topological sort

    Args:
        edges (List[List[int]]): An integer array represents valid order where edges[i] = [a_i, b_i, ...] indicates that you must place i first in the result sorted list before you place a_i, b_i, ... .

    Returns:
        List[int]: A sorted integers in given order.
    """

    node_num = len(edges)
    output = []
    seen = [False] * node_num

    def dfs(v):
        if seen[v]:
            return
        seen[v] = True

        for u in edges[v]:
            dfs(u)

        output.append(v)
        return

    for v in range(node_num):
        dfs(v)

    output.reverse()
    return output
