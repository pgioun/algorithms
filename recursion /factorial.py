def factorial(n):
    # Check for invalid input (negative numbers are not allowed)
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: factorial(n) = n * factorial(n-1)
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Test cases
    try:
        # Test with valid input
        result = factorial(5)
        print("Factorial of 5:", result)  # Expected output: 120

        # Test with 0
        result = factorial(0)
        print("Factorial of 0:", result)  # Expected output: 1

        # Test with negative input (should raise an error)
        result = factorial(-3)
        print("Factorial of -3:", result)  # This line won't be reached
        
    except ValueError as e:
        print("Error:", e)  # Expected error message: "Input must be a non-negative integer"
