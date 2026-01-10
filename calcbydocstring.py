"""
Simple Calculator Program

This program demonstrates the use of docstrings in Python.
It provides basic arithmetic operations such as addition,
subtraction, multiplication, and division.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Result of division

    Raises:
    ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))
