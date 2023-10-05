def divide_and_conquer_max(arr):
    # Error checking
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    if len(arr) == 0:
        raise ValueError("Input list is empty")

    # Base case: If the array has only one element, return it.
    if len(arr) == 1:
        return arr[0]

    # Split the array into two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively find the maximum in each half.
    max_left = divide_and_conquer_max(left_half)
    max_right = divide_and_conquer_max(right_half)

    # Return the maximum of the two maximums.
    return max(max_left, max_right)

if __name__ == "__main__":
    # Test cases
    arr1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    arr2 = [10, 20, 30, 40, 50]
    arr3 = [5]
    arr4 = []

    print(divide_and_conquer_max(arr1))  # Expected output: 9
    print(divide_and_conquer_max(arr2))  # Expected output: 50
    print(divide_and_conquer_max(arr3))  # Expected output: 5
    # Uncomment the line below to test with an empty list (should raise a ValueError)
    print(divide_and_conquer_max(arr4))
