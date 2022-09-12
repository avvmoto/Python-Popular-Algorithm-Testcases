import random


def quick_sort(a):
    def helper(a, l, r): # sort [l,r)
        if r-l<=1:
            return
        
        p = l + (r-l)//2
        pivot = a[p]
        a[r-1], a[p] = a[p], a[r-1]

        i = l
        for j in range(l, r-1):
            if a[j] >= pivot:
                continue
            a[i], a[j]= a[j], a[i]
            i+=1
        a[i], a[r-1] = a[r-1], a[i]

        helper(a, l, i)

        helper(a, i+1, r)
        return

    helper(a, 0, len(a))
    return




def partition(a, l, r, pivot_index):
    pivot_value = a[pivot_index]
    a[r-1], a[pivot_index] = a[pivot_index], a[r-1]

    i = l
    for j in range(l, r-1):
        if a[j]>=pivot_value:
            continue
        a[i], a[j] = a[j], a[i]
        i+=1

    a[i], a[r-1] = a[r-1], a[i]
    return i


def select(a, l, r, k):
    if r-l<=1:
        return a[:k]

    pivot_index = random.randint(l, r-2)
    pivot_index = partition(a, l, r,  pivot_index)

    if pivot_index+1 == k:
        return a[:k]
    elif pivot_index+1 <k:
        return select(a,pivot_index+1,r, k)
    else:
        return select(a,l, pivot_index+1,k )


def quick_select(a, k):
    return select(a, 0, len(a), k)