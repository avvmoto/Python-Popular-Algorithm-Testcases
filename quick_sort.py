import random
from typing import List


def quick_sort(nums: List[int]):
    """quick_sort sorts nums in-place.

    Args:
        nums (List[int]): array to be sorted in-place.
    """

    # sort [l, r)
    def sort(nums, l, r):
        if r - l < 1:
            return

        m = l + (r - l) // 2
        i = l

        pivot = nums[m]
        nums[m], nums[r - 1] = nums[r - 1], nums[m]
        for j in range(l, r - 1):
            if nums[j] >= pivot:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        nums[i], nums[r - 1] = nums[r - 1], nums[i]

        sort(nums, l, i)
        sort(nums, i + 1, r)
        return

    sort(nums, 0, len(nums))
    return


def quick_select(nums: List[int], k: int) -> List[int]:
    """quick_select returns kth minimum numbers from nums.

    Args:
        nums (List[int]): target numbers.
        k (int): get kth minimum numbers.
    """

    # partition [l, r)
    def partition(nums, l, r, pivot_index):
        pivot = nums[pivot_index]
        nums[r - 1], nums[pivot_index] = nums[pivot_index], nums[r - 1]

        i = l
        for j in range(l, r - 1):
            if nums[j] >= pivot:
                continue
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
        nums[i], nums[r - 1] = nums[r - 1], nums[i]

        return i

    # select kth min from num[:] by choosing pivot from [l, r).
    def select(nums, l, r, k):
        if r - l < 1:
            return nums[:k]
        pivot_index = random.randint(l, r - 1)

        pivot_index = partition(nums, l, r, pivot_index)

        if pivot_index == k - 1:
            return nums[:k]
        elif pivot_index < k - 1:
            return select(nums, pivot_index + 1, r, k)
        else:
            return select(nums, l, pivot_index, k)

    return select(nums, 0, len(nums), k)
