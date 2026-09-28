from randomised_quick_sort import QuickSort, QuickSortFirstPivot, RandomizedQuickSort
from chained_hashing import LinkedList

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

print("\n\nLinkedList trace:\n")
ll = LinkedList()
ll.insert(1, "one")
ll.insert(2, "two")
ll.insert(3, "three")

print("Search 2:", ll.search(2))
print("Delete 2:", ll.delete(2))
print("Search 2 after delete:", ll.search(2))
for key, value in ll:
    print(f"{key}: {value}")