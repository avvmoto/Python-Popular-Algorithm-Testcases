from typing import List


def binary_search(a: List[int], x: int) -> int:
    """binary_search returns minumum index of the sorted array `a` which satisfy a[i]>=x.
    Just same as bisect.bisect_left.

    Args:
        a (List[int]): A sorted array.
        x (int): A target value.

    Returns:
        int: the smallest index which satisfy a[i]>=x.
    """
    if not a or a[0] >= x:
        return 0

    if a[-1] < x:
        return len(a)

    l = 0
    r = len(a) - 1

    while r - l > 1:
        m = l + (r - l) // 2

        if a[m] >= x:
            r = m
        else:
            l = m

    return r
