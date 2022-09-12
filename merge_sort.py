def merge_sort(a):

    buf = [0] * len(a)

    def sort_range(a, l, r):
        if r - l <= 1:
            return

        m = l + (r - l) // 2

        sort_range(a, l, m)
        sort_range(a, m, r)

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

    sort_range(a, 0, len(a))
    return
