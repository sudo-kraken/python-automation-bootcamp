# functions_example.py
# Demonstrates how to define and use functions in Python.

def greet(name):
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.
    Returns None for negative inputs.
    """
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    # Example usage of the functions
    name = "Joe"
    print(greet(name))
    
    number = 5
    print(f"Factorial of {number} is {factorial(number)}")

if __name__ == "__main__":
    main()
