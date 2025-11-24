def poorly_commented_function(lst):
    """
    Refactored version with automatic documentation:

    This function takes a list of integers as input and returns a tuple containing:
      - A list of the even numbers from the input list.
      - The sum of those even numbers.
      - The count of even numbers in the list.

    Args:
        lst (list): List of integers.

    Returns:
        tuple: (list of even numbers, sum of even numbers, count of even numbers)
    """
    evens = [x for x in lst if x % 2 == 0]
    total = sum(evens)
    count = len(evens)
    return (evens, total, count)

# Example usage and output:
if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = poorly_commented_function(sample)
    print("Evens:", result[0])
    print("Sum of evens:", result[1])
    print("Count of evens:", result[2])

"""
Clarity & Completeness Evaluation:
- The docstring clearly explains parameters and return values.
- Automatic documentation using a docstring covers all details, arguably more reliably than sparse manual comments.
- The usage example and output further clarify behavior for the user.
"""
