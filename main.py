from randomised_quick_sort import QuickSort, QuickSortFirstPivot, RandomizedQuickSort

def CreateRandomArray(size):
    import random
    return [random.randint(0, 100) for _ in range(size)]

arr = CreateRandomArray(10)

print("QuickSort trace:\n")
quick_sorted = QuickSort(arr.copy())
print("\nFinal sorted array using QuickSort:", quick_sorted)
first_pivot_sorted = QuickSortFirstPivot(arr.copy())
print("\nFinal sorted array using QuickSort with first pivot:", first_pivot_sorted)

print("\n\nRandomizedQuickSort trace:\n")
randomized_arr = arr.copy()
random_sorted = RandomizedQuickSort(randomized_arr, 0, len(randomized_arr) - 1)
print("\nFinal sorted array using RandomizedQuickSort:", random_sorted)