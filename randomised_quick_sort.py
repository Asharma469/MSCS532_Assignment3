def QuickSort(arr):
    if len(arr) <= 1:
        print(f"Base case reached: {arr} -> no further partitioning needed.")
        return arr

    pivot = arr[len(arr) // 2]

    print(f"\nQuickSort step: current list = {arr}")
    print(f"Chosen pivot = {pivot}")

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"Partition result: left = {left}, middle = {middle}, right = {right}")

    sorted_left = QuickSort(left)
    sorted_right = QuickSort(right)
    result = sorted_left + middle + sorted_right

    return result