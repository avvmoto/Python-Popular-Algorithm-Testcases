from typing import List

def binary_search(a: List[int], v: int) -> int:
    if not a or a[0]>=v:
        return 0

    l = 0
    r = len(a)-1

    while r-l>1:
        m = l + (r-l)//2

        if a[m]>=v:
            r = m
        else:
            l = m

    return r