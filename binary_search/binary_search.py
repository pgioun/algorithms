def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2  # Use integer division to get a valid index
        guess = lst[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    result = binary_search(my_list, 3)
    if result is not None:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

