"""Odd and Even Sum Calculator

This program calculates the sum of odd and even numbers in a list.
Users can input numbers manually or use example lists.
"""

from typing import List, Tuple


def calculate_odd_even_sums(numbers: List[int]) -> Tuple[int, int]:
    """Calculate the sum of odd and even numbers in a list.
    
    Args:
        numbers: List of integers to process
        
    Returns:
        Tuple of (sum of odd numbers, sum of even numbers)
        
    Example:
        >>> calculate_odd_even_sums([1, 2, 3, 4, 5])
        (9, 6)  # Odd sum: 1+3+5=9, Even sum: 2+4=6
    """
    odd_sum = sum(num for num in numbers if num % 2 != 0)2
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return odd_sum, even_sum


def get_number_list() -> List[int]:
    """Get a list of numbers from user input.
    
    Returns:
        List of integers entered by the user
    """
    numbers = []
    print("\nEnter numbers one per line (press Enter with no input to finish):")
    
    while True:
        try:
            line = input("Number (or Enter to finish): ").strip()
            if not line:
                break
            numbers.append(int(line))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    return numbers


def main():
    """Main program loop."""
    print("Odd and Even Sum Calculator")
    print("-" * 25)
    
    while True:
        # Let user choose input method
        print("\nChoose input method:")
        print("1. Enter numbers manually")
        print("2. Use example list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
        print("3. Quit")
        
        choice = input("\nYour choice (1-3): ")
        
        if choice == '3':
            break
        elif choice == '2':
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        elif choice == '1':
            numbers = get_number_list()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue
            
        if not numbers:
            print("No numbers to process!")
            continue
            
        # Calculate and display results
        odd_sum, even_sum = calculate_odd_even_sums(numbers)
        
        print("\nResults for numbers:", numbers)
        print(f"Odd numbers sum: {odd_sum}")
        print(f"Even numbers sum: {even_sum}")
        
        # Show the odd and even numbers separately
        odd_nums = [n for n in numbers if n % 2 != 0]
        even_nums = [n for n in numbers if n % 2 == 0]
        
        print(f"\nOdd numbers: {odd_nums}")
        print(f"Even numbers: {even_nums}")
        
        print("\nWould you like to try another list?")
        if input("Press 'y' to continue, any other key to quit: ").lower() != 'y':
            break
    
    print("\nThank you for using the Odd and Even Sum Calculator!")


if __name__ == "__main__":
    main()
