# Binary Search Algorithm

This repository contains a Python script that implements the binary search algorithm. Binary search is an efficient search algorithm for finding a target value in a sorted list. This README provides an overview of the code and how to use it.

## Code Explanation

The Python script, `binary_search.py`, consists of two main parts: the `binary_search` function and the main code block.

### `binary_search` Function

The `binary_search` function is defined to perform binary search on a sorted list. It takes two parameters:
- `lst` (list): The sorted list to search in.
- `target` (int): The target value to find.

The function follows these steps:
1. Initialize `low` and `high` as the starting and ending indices of the search range.
2. Enter a `while` loop that continues until `low` is less than or equal to `high`, ensuring the search range is valid.
3. Calculate the `mid` index using integer division of `(low + high) // 2`.
4. Obtain the value at the `mid` index in the list (`guess`).
5. If `guess` is equal to the `target`, the function returns the `mid` index, indicating the target value was found.
6. If `guess` is greater than the `target`, the search range is narrowed to the lower half by updating `high` to `mid - 1`.
7. If `guess` is less than the `target`, the search range is narrowed to the upper half by updating `low` to `mid + 1`.
8. If the `target` is not found in the list, the function returns `None`.

### Main Code Block

The script's main code block uses the `binary_search` function to search for a specific target value (`target_value`) in a predefined sorted list (`my_list`). It follows these steps:
1. Check if the script is being run as the main program using `if __name__ == "__main__":`.
2. Define the sorted list `my_list` and the target value `target_value`.
3. Call the `binary_search` function with `my_list` and `target_value`, storing the result in the `result` variable.
4. Check if the `result` is not `None`, indicating that the target value was found. If so, print the index where the element was found. Otherwise, print "Element not found."

### Maximum Number of Steps in Binary Search

In binary search, the maximum number of steps required to find an item in a sorted list of size `n` can be calculated using the formula `log2(n)`. This is because binary search divides the search range in half with each comparison. The logarithm base 2 provides the number of times you can divide `n` by 2 until you reach 1.

## Usage

To use the binary search script:
1. Make sure you have Python installed on your system.
2. Clone or download this repository.
3. Open a terminal and navigate to the repository directory.
4. Run the script using the command: `python binary_search.py`.



## Contributing

Contributions to improve this code are welcome! If you find any issues or have suggestions, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).