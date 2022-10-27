from typing import List


def merge_sort(a: List[int]):
    """merge_sort sorts int array `a` in-place.

    Args:
        a (List[int]): A int array to be sorted.
    """
    buf = [0] * len(a)

    def merge_sort_range(l, r):
        if r - l < 2:
            return

        m = l + (r - l) // 2

        merge_sort_range(l, m)
        merge_sort_range(m, r)

        for i in range(l, m):
            buf[i] = a[i]
        for i in range(m, r):
            buf[i] = a[r - 1 - i + m]

        for i in range(l, r):
            if buf[l] < buf[r - 1]:
                a[i] = buf[l]
                l += 1
            else:
                a[i] = buf[r - 1]
                r -= 1
        return

    merge_sort_range(0, len(a))
    return
