def binary_search(lst, target):
    # Input validation
    if not isinstance(lst, list) or not all(isinstance(item, int) for item in lst):
        raise ValueError("Input list should contain integers only.")
        
    if not isinstance(target, int):
        raise ValueError("Target value should be an integer.")
    
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Test cases
if __name__ == "__main__":
    import math

    my_list = [1, 2, 3, 15, 17, 19, 39, 41]
    target_value = 3

    result = binary_search(my_list, target_value)
    if result is not None:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

    list_size = len(my_list)
    steps = math.log2(list_size)
    print(f"Log2 of list size ({list_size}) is: {steps:.2f}")
    
    # Test cases
    test_cases = [
        [my_list, 3],       # Element found
        [my_list, 10],      # Element not found
        [[], 5],            # Empty list
        [[1, 3, 5], 3],     # Element in a small list
        [[1, 3, 5], 4],     # Element not in a small list
        [[1], 1],           # Single element list
        [[1], 2],           # Element not in a single element list
        [[1, 2, 3, 4], 1],  # First element
        [[1, 2, 3, 4], 4],  # Last element
    ]
    
    for test in test_cases:
        test_list, test_target = test
        try:
            test_result = binary_search(test_list, test_target)
            if test_result is not None:
                print(f"Element {test_target} found at index {test_result}")
            else:
                print(f"Element {test_target} not found")
        except Exception as e:
            print(f"An error occurred: {e}")