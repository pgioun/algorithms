# Factorial Calculation Algorithm

This is a simple Python program that calculates the factorial of a non-negative integer using recursion. The program checks for errors in the input and includes test cases to demonstrate its functionality.

## Algorithm Description

The `factorial` function in `factorial.py` calculates the factorial of a non-negative integer `n` using recursion. Here's how it works:

1. **Input Validation**: The program checks if the input `n` is a non-negative integer. If `n` is negative, it raises a `ValueError` with an error message indicating that negative integers are not allowed.

2. **Base Case**: If `n` is 0, the function returns 1. This is because the factorial of 0 is defined as 1.

3. **Recursive Case**: For values of `n` greater than 0, the function calculates the factorial by calling itself recursively with `n-1` and multiplying the result by `n`. This process continues until `n` becomes 0, at which point the recursion stops.

## Usage

To use the `factorial` function, simply call it with a non-negative integer as an argument. For example:

```python
result = factorial(5)
print("Factorial of 5:", result)  # Expected output: 120

## License

This project is licensed under the [Apache License License]( http://www.apache.org/licenses/).


