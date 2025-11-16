from typing import List, Tuple

def sum_even_odd_manual(numbers: List[int]) -> Tuple[int, int]:
    """Calculate the sum of even and odd numbers in the given list.
    
    This function takes a list of integers and returns a tuple containing
    the sum of even numbers and the sum of odd numbers respectively.
    
    Args:
        numbers: A list of integers to process.
        
    Returns:
        tuple: A tuple of two integers where:
            - First element is the sum of even numbers
            - Second element is the sum of odd numbers
            
    Examples:
        >>> sum_even_odd_manual([1, 2, 3, 4, 5])
        (6, 9)
        >>> sum_even_odd_manual([2, 4, 6])
        (12, 0)
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

def sum_even_odd_ai(numbers: List[int]) -> Tuple[int, int]:
    """Computes the separate sums of even and odd numbers from a list.

    Takes a list of integers as input and processes it to calculate two sums:
    one for all even numbers and another for all odd numbers. Uses modulo
    operator to determine even/odd status of each number.

    Args:
        numbers (List[int]): The input list of integers to process.

    Returns:
        Tuple[int, int]: A tuple where:
            - index 0 contains the sum of all even numbers
            - index 1 contains the sum of all odd numbers

    Examples:
        >>> sum_even_odd_ai([1, 2, 3, 4])
        (6, 4)
        >>> sum_even_odd_ai([])
        (0, 0)
        >>> sum_even_odd_ai([1, 3, 5])
        (0, 9)
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

def main():
    test_lists = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8],
        [1, 3, 5, 7],
        [],
        [-1, -2, 3, 4]
    ]
    
    print("Testing both implementations:")
    print("-" * 50)
    
    for test_list in test_lists:
        manual_result = sum_even_odd_manual(test_list)
        ai_result = sum_even_odd_ai(test_list)
        
        print(f"Input list: {test_list}")
        print(f"Manual function result: {manual_result}")
        print(f"AI function result: {ai_result}")
        print("-" * 50)

if __name__ == "__main__":
    main()
