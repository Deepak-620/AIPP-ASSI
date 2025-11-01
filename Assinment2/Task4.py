"""Sum of Squares Calculator

This program calculates the sum of squares from 1 to n,
where n is provided by the user.

Example:
    For n = 3, calculates 1² + 2² + 3² = 1 + 4 + 9 = 14
"""


def calculate_sum_of_squares(n: int) -> int:
    """Calculate the sum of squares from 1 to n.
    
    Args:
        n: A positive integer
        
    Returns:
        The sum of squares from 1 to n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Number must be non-negative")
    
    # Using sum with generator expression
    return sum(i * i for i in range(1, n + 1))


def get_valid_input() -> int:
    """Get a valid positive integer from the user.
    
    Returns:
        A positive integer entered by the user
    """
    while True:
        try:
            num = input("Enter a positive number: ")
            n = int(num)
            if n < 0:
                print("Please enter a non-negative number.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """Main program loop."""
    print("Sum of Squares Calculator")
    print("-" * 25)
    print("This program will calculate the sum of squares from 1 to n")
    
    while True:
        n = get_valid_input()
        result = calculate_sum_of_squares(n)
        
        # Show the calculation for small numbers
        if n <= 10:
            squares = [f"{i}² = {i*i}" for i in range(1, n + 1)]
            print(f"\nCalculation: {' + '.join(squares)}")
        
        print(f"\nThe sum of squares from 1 to {n} is: {result}")
        
        # Ask if user wants to continue
        again = input("\nCalculate another sum? (y/n): ").lower()
        if again != 'y':
            break
    
    print("\nThank you for using the Sum of Squares Calculator!")


if __name__ == "__main__":
    main()
