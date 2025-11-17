def divide_numbers(a, b):
    """
    Safely divides two numbers.

    This function handles division errors using try-except.
    If 'b' is zero, it returns a message instead of raising an exception.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Testing the function
print(divide_numbers(10, 0))
print(divide_numbers(20, 5))
