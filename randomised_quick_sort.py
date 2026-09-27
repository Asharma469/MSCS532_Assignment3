
# Simple QuickSort implementation with a middle pivot.
# Time complexity: Average case: O(n log n) and Worst case: O(n^2)
#   - Recurrence: T(n) = 2T(n/2) + O(n)
#   - In the worst case, recursion depth can reach O(n)

def QuickSort(arr):
    if len(arr) <= 1:
        print(f"Base case reached: {arr} -> no further partitioning needed.")
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"Partition result: left = {left}, middle = {middle}, right = {right}")

    # Each recursive call processes one partition.
    # The partition step itself takes O(n), so the total average time follows:
    # T(n) = T(left) + T(right) + O(n) = 2T(n/2) + O(n) -> O(n log n)
    sorted_left = QuickSort(left)
    sorted_right = QuickSort(right)
    result = sorted_left + middle + sorted_right

    return result


# QuickSort variant that chooses the first element as the pivot.
# Time complexity: Just like center pivot: Average case: O(n log n) and Worst case: O(n^2)
# Meanwhile Recurrence: T(n) = T(n-1) + O(n) in the worst case.
# Since the splits created by the first element as pivot can be highly unbalanced, 
# recursion depth can reach O(n) in the worst case.
# worse case can happen on center-pivot as well, but it's still not bad as the first element pivot.
def QuickSortFirstPivot(arr):
    if len(arr) <= 1:
        print(f"Base case reached: {arr} -> no further partitioning needed.")
        return arr

    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"Partition result: left = {left}, middle = {middle}, right = {right}")

    sorted_left = QuickSortFirstPivot(left)
    sorted_right = QuickSortFirstPivot(right)
    result = sorted_left + middle + sorted_right

    return result


# Randomized QuickSort
# Time complexity: Average case: O(n log n) and the worst case: O(n^2)
# The random pivot makes worst-case behavior unlikely, so average performance is much better in practice
#   - Recurrence (average case): T(n) = 2T(n/2) + O(n) -> O(n log n)
#   - Recurrence (worst case): T(n) = T(n-1) + O(n) -> O(n^2)
def RandomizedQuickSort(arr, low, high):
    if low < high:
        pi = RandomizedPartition(arr, low, high)

        # Two recursive calls on the left and right partitions.
        # The partitioning cost is O(high - low + 1), and the average total is O(n log n).
        RandomizedQuickSort(arr, low, pi - 1)
        RandomizedQuickSort(arr, pi + 1, high)

    return arr


# Partition helper for RandomizedQuickSort.
# Time complexity: O(n) for a given subarray because every element is examined once.
# Space complexity: O(1) extra space because the swap-based partition is done in place.
# This function is the main reason each recursion level costs linear time.

def RandomizedPartition(arr, low, high):
    import random

    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    print(f"Pivot placed at index {i + 1}; partitioned array = {arr[low:high + 1]}")

    return i + 1

