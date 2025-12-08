"""Convert conditional statements from Java to Python."""

def check_number(num):
    """
    Check if a number is positive, negative, or zero.
    
    Args:
        num: An integer to check
        
    Returns:
        A string describing the number's sign
    """
    if num > 0:
        return "The number is positive"
    elif num < 0:
        return "The number is negative"
    else:
        return "The number is zero"


if __name__ == "__main__":
    # Test cases
    test_cases = [-5, 0, 7]
    
    for num in test_cases:
        result = check_number(num)
        print(f"Input: {num} → Output: {result}")