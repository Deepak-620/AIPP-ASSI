"""
Manual NumPy Style Calculator Module.

This module provides basic arithmetic operations for mathematical calculations.
It includes functions for addition, subtraction, multiplication, and division
with proper error handling and input validation.

Examples
--------
>>> from calculator import add, subtract, multiply, divide
>>> add(10, 5)
15
>>> divide(20, 4)
5.0
"""

from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.
    
    This function takes two numeric values and returns their sum.
    It supports both integers and floating-point numbers.
    
    Parameters
    ----------
    a : int or float
        The first number to add.
    b : int or float
        The second number to add.
    
    Returns
    -------
    int or float
        The sum of a and b.
    
    Examples
    --------
    >>> add(3, 4)
    7
    >>> add(3.5, 2.5)
    6.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract one number from another.
    
    This function takes two numeric values and returns the difference
    by subtracting the second value from the first value.
    
    Parameters
    ----------
    a : int or float
        The minuend (number to subtract from).
    b : int or float
        The subtrahend (number to subtract).
    
    Returns
    -------
    int or float
        The difference of a minus b.
    
    Examples
    --------
    >>> subtract(10, 3)
    7
    >>> subtract(5.5, 2.3)
    3.2
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers together.
    
    This function takes two numeric values and returns their product.
    Supports multiplication of integers and floating-point numbers.
    
    Parameters
    ----------
    a : int or float
        The first multiplicand.
    b : int or float
        The second multiplicand.
    
    Returns
    -------
    int or float
        The product of a and b.
    
    Examples
    --------
    >>> multiply(4, 5)
    20
    >>> multiply(2.5, 4)
    10.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide one number by another.
    
    This function takes two numeric values and returns the quotient
    by dividing the first number by the second. Raises an error if
    the divisor is zero to prevent undefined mathematical operations.
    
    Parameters
    ----------
    a : int or float
        The dividend (number to be divided).
    b : int or float
        The divisor (number to divide by).
    
    Returns
    -------
    float
        The quotient of a divided by b.
    
    Raises
    ------
    TypeError
        If either argument is not a numeric type.
    ZeroDivisionError
        If b is zero, as division by zero is undefined.
    
    Examples
    --------
    >>> divide(20, 4)
    5.0
    >>> divide(7, 2)
    3.5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


"""
AI-Generated NumPy Style Calculator Module (Comparison).

This module implements fundamental arithmetic operations with type safety.
Functions provide mathematical computations for integers and floats with
explicit error handling for invalid inputs and edge cases.

Examples
--------
>>> result = add_ai(15, 10)
>>> result
25
"""


def add_ai(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Computes and returns the arithmetic sum of two numeric operands.
    
    Accepts two numeric inputs (integer or floating-point) and computes
    their addition. Input type validation ensures both arguments are numeric
    before performing the operation to prevent type-related errors.
    
    Parameters
    ----------
    a : int or float
        First numeric operand for summation operation.
    b : int or float
        Second numeric operand for summation operation.
    
    Returns
    -------
    int or float
        Numeric result representing sum of both operands maintaining
        original numeric type when both inputs are integers.
    
    Raises
    ------
    TypeError
        If either parameter is not an int or float type.
    
    Examples
    --------
    >>> add_ai(12, 8)
    20
    >>> add_ai(3.14, 2.86)
    6.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def subtract_ai(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs subtraction operation returning difference of two numbers.
    
    Executes subtraction of second operand from first operand. Validates
    input types to ensure both parameters are numeric before computing
    the mathematical difference between the operands.
    
    Parameters
    ----------
    a : int or float
        The minuend numeric value (number being subtracted from).
    b : int or float
        The subtrahend numeric value (number being subtracted).
    
    Returns
    -------
    int or float
        Numeric difference result computed as (a - b) preserving numeric
        type consistency for integer operations.
    
    Raises
    ------
    TypeError
        When either argument fails numeric type validation check.
    
    Examples
    --------
    >>> subtract_ai(25, 10)
    15
    >>> subtract_ai(10.5, 3.2)
    7.3
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply_ai(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Computes the product by multiplying two numeric operands.
    
    Executes multiplication of two numeric values with comprehensive type
    checking. Validates that both inputs are numeric types before performing
    multiplication to ensure mathematical validity of the operation.
    
    Parameters
    ----------
    a : int or float
        First multiplicand numeric operand.
    b : int or float
        Second multiplicand numeric operand.
    
    Returns
    -------
    int or float
        Numeric product of multiplication operation, maintaining original
        numeric type when both operands are integers.
    
    Raises
    ------
    TypeError
        If either argument is not numeric (int or float).
    
    Examples
    --------
    >>> multiply_ai(6, 7)
    42
    >>> multiply_ai(2.5, 3.0)
    7.5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide_ai(a: Union[int, float], b: Union[int, float]) -> float:
    """Executes division operation returning quotient of dividend by divisor.
    
    Performs division of first operand by second operand with dual validation:
    type checking ensures numeric inputs and zero-check prevents undefined
    mathematical operation. Returns floating-point result for all divisions.
    
    Parameters
    ----------
    a : int or float
        The dividend operand (numerator to be divided).
    b : int or float
        The divisor operand (denominator dividing the dividend).
    
    Returns
    -------
    float
        Floating-point quotient result of division operation (a / b).
    
    Raises
    ------
    TypeError
        When either argument is not numeric type.
    ZeroDivisionError
        When divisor (b) equals zero, as division by zero is undefined
        in mathematics and computationally invalid.
    
    Examples
    --------
    >>> divide_ai(30, 6)
    5.0
    >>> divide_ai(9, 4)
    2.25
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def demonstrate_calculator():
    """Demonstrate the calculator functions with various test cases."""
    print("=" * 70)
    print("MANUAL NUMPY STYLE DOCSTRINGS - CALCULATOR DEMONSTRATION")
    print("=" * 70)
    
    test_cases = [
        ("Addition", add, 15, 10),
        ("Subtraction", subtract, 25, 7),
        ("Multiplication", multiply, 6, 8),
        ("Division", divide, 20, 4),
    ]
    
    for operation_name, func, a, b in test_cases:
        result = func(a, b)
        print(f"{operation_name}: {a} and {b} = {result}")
    
    print("\n" + "=" * 70)
    print("AI-GENERATED NUMPY STYLE DOCSTRINGS - CALCULATOR DEMONSTRATION")
    print("=" * 70)
    
    test_cases_ai = [
        ("Addition", add_ai, 20, 15),
        ("Subtraction", subtract_ai, 30, 12),
        ("Multiplication", multiply_ai, 7, 9),
        ("Division", divide_ai, 36, 6),
    ]
    
    for operation_name, func, a, b in test_cases_ai:
        result = func(a, b)
        print(f"{operation_name}: {a} and {b} = {result}")
    
    print("\n" + "=" * 70)
    print("ERROR HANDLING TEST CASES")
    print("=" * 70)
    
    error_tests = [
        ("Division by zero", divide, 10, 0),
        ("Invalid type in add", add, "10", 5),
        ("Invalid type in multiply", multiply, 10, "5"),
    ]
    
    for test_name, func, a, b in error_tests:
        try:
            result = func(a, b)
            print(f"{test_name}: {result}")
        except (TypeError, ZeroDivisionError) as e:
            print(f"{test_name}: Error - {type(e).__name__}: {e}")


if __name__ == "__main__":
    demonstrate_calculator()
