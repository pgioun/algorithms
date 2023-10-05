def quick_sort(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Test cases for input validation
    # try:
    #     quick_sort("invalid_input")
    # except ValueError as e:
    #     print(f"Error: {e}")
    
    try:
        quick_sort([])
    except ValueError as e:
        print(f"Error: {e}")

    # Test cases for the Quick Sort algorithm
    arr1 = [3, 6, 8, 10, 1, 2, 1]
    arr2 = [9, 7, 5, 3, 1]
    arr3 = [1, 2, 3, 4, 5]

    print(quick_sort(arr1))  # Should print [1, 1, 2, 3, 6, 8, 10]
    print(quick_sort(arr2))  # Should print [1, 3, 5, 7, 9]
    print(quick_sort(arr3))  # Should print [1, 2, 3, 4, 5]
