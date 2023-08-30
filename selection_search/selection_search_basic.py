def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.

    :param arr: List[int], the input array to be sorted
    :return: List[int], the sorted array
    """

    # Check for inappropriate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Test cases
if __name__ == "__main__":
    # Test case 1: Positive integers
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr1 = selection_sort(arr1.copy())
    print("Original array:", arr1)
    print("Sorted array:", sorted_arr1)
    
    # Test case 2: Negative integers
    arr2 = [-12, -45, -23, -6, -89, -34]
    sorted_arr2 = selection_sort(arr2.copy())
    print("Original array:", arr2)
    print("Sorted array:", sorted_arr2)
    
    # Test case 3: Mixed positive and negative integers
    arr3 = [-5, 10, -3, 8, -1, 0, -7]
    sorted_arr3 = selection_sort(arr3.copy())
    print("Original array:", arr3)
    print("Sorted array:", sorted_arr3)
    
    # Test case 4: Floats
    arr4 = [3.14, 1.618, 2.718, 0.577, 1.414]
    sorted_arr4 = selection_sort(arr4.copy())
    print("Original array:", arr4)
    print("Sorted array:", sorted_arr4)
    
    # Test case 5: Empty array
    arr5 = []
    sorted_arr5 = selection_sort(arr5.copy())
    print("Original array:", arr5)
    print("Sorted array:", sorted_arr5)