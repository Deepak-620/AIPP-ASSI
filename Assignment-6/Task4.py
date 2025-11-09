"""
AI PROMPT:
----------
Generate a Python function sum_to_n() that calculates the sum of first n natural numbers.
The function should accept n as user input and use different looping approaches (for loop, 
while loop, recursion). Include code analysis and explanations for each approach.
"""


def sum_to_n_for_loop(n):
    """
    Calculate sum of first n natural numbers using for loop.
    
    Approach: Iterate from 1 to n and accumulate the sum.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


def sum_to_n_while_loop(n):
    """
    Calculate sum of first n natural numbers using while loop.
    
    Approach: Use a counter that increments until it reaches n.
    Time Complexity: O(n)
    Space Complexity: O(1)R
    """
    total = 0
    i = 1
    while i <= n:
        total = total + i
        i = i + 1
    return total


def sum_to_n_recursion(n):
    """
    Calculate sum of first n natural numbers using recursion.
    
    Approach: Base case is n=0 or n=1, recursive case adds n to sum of (n-1).
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_to_n_recursion(n - 1)


def sum_to_n_formula(n):
    """
    Calculate sum of first n natural numbers using mathematical formula.
    
    Formula: sum = n * (n + 1) / 2
    This is the most efficient approach - no loop needed!
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return n * (n + 1) // 2


def sum_to_n_list_comprehension(n):
    """
    Calculate sum using list comprehension and built-in sum() function.
    
    Approach: Generate list of numbers [1, 2, ..., n] and sum them.
    Time Complexity: O(n)
    Space Complexity: O(n) for the list
    """
    return sum([i for i in range(1, n + 1)])


def sum_to_n_reduce(n):
    """
    Calculate sum using functools.reduce with lambda function.
    
    Approach: Reduce operation accumulates values using addition.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    from functools import reduce
    return reduce(lambda x, y: x + y, range(1, n + 1))


def sum_to_n_generator(n):
    """
    Calculate sum using generator expression (memory efficient).
    
    Approach: Generator creates numbers on-the-fly without storing in memory.
    Time Complexity: O(n)
    Space Complexity: O(1) - more memory efficient than list comprehension
    """
    return sum(i for i in range(1, n + 1))


def sum_to_n_accumulate(n):
    """
    Calculate sum using itertools.accumulate.
    
    Approach: Creates cumulative sums and returns the last value.
    Time Complexity: O(n)
    Space Complexity: O(n) for intermediate results
    """
    from itertools import accumulate
    return list(accumulate(range(1, n + 1)))[-1]


if __name__ == "__main__":
    print("=" * 70)
    print("SUM OF FIRST N NATURAL NUMBERS - MULTIPLE IMPLEMENTATIONS")
    print("=" * 70)
    
    try:
        n = int(input("\nEnter a positive integer n: "))
        
        if n < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            print(f"\nCalculating sum of first {n} natural numbers...")
            print("-" * 70)
            
            print(f"\n1. FOR LOOP:")
            result1 = sum_to_n_for_loop(n)
            print(f"   Result: {result1}")
            print(f"   Explanation: Iterates from 1 to n, adding each number to total.")
            
            print(f"\n2. WHILE LOOP:")
            result2 = sum_to_n_while_loop(n)
            print(f"   Result: {result2}")
            print(f"   Explanation: Uses counter variable, increments until reaching n.")
            
            print(f"\n3. RECURSION:")
            result3 = sum_to_n_recursion(n)
            print(f"   Result: {result3}")
            print(f"   Explanation: Recursively adds n to sum of (n-1), base case at n=0 or n=1.")
            
            print(f"\n4. MATHEMATICAL FORMULA (Most Efficient):")
            result4 = sum_to_n_formula(n)
            print(f"   Result: {result4}")
            print(f"   Explanation: Uses formula n*(n+1)/2 - no loop needed, O(1) complexity.")
            
            print(f"\n5. LIST COMPREHENSION:")
            result5 = sum_to_n_list_comprehension(n)
            print(f"   Result: {result5}")
            print(f"   Explanation: Creates list [1,2,...,n] and uses built-in sum() function.")
            
            print(f"\n6. REDUCE FUNCTION:")
            result6 = sum_to_n_reduce(n)
            print(f"   Result: {result6}")
            print(f"   Explanation: Uses functools.reduce to accumulate values with addition.")
            
            print(f"\n7. GENERATOR EXPRESSION:")
            result7 = sum_to_n_generator(n)
            print(f"   Result: {result7}")
            print(f"   Explanation: Memory-efficient generator creates numbers on-the-fly.")
            
            print(f"\n8. ITERTOOLS.ACCUMULATE:")
            result8 = sum_to_n_accumulate(n)
            print(f"   Result: {result8}")
            print(f"   Explanation: Creates cumulative sums and returns the last value.")
            
            print("\n" + "=" * 70)
            print("VERIFICATION:")
            print("=" * 70)
            print(f"All methods should return the same result: {result1}")
            print(f"Results match: {all([result1 == r for r in [result2, result3, result4, result5, result6, result7, result8]])}")
            
            if n <= 10:
                numbers = [str(i) for i in range(1, n + 1)]
                print(f"\nVisual representation: {' + '.join(numbers)} = {result1}")
            
    except ValueError:
        print("Error: Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except RecursionError:
        print("Error: Recursion depth exceeded. Please use a smaller value or use iterative methods.")
    
    print("\n" + "=" * 70)
    print("CODE ANALYSIS:")
    print("=" * 70)
    print("""
PERFORMANCE COMPARISON:
-----------------------
1. FOR LOOP:
   - Time: O(n), Space: O(1)
   - Most readable and intuitive
   - Best for beginners
   - Recommended for general use

2. WHILE LOOP:
   - Time: O(n), Space: O(1)
   - Explicit control over iteration
   - Useful when termination condition is complex
   - Requires careful counter management

3. RECURSION:
   - Time: O(n), Space: O(n) - recursion stack
   - Elegant mathematical approach
   - Risk of stack overflow for large n
   - Good for learning recursive thinking

4. MATHEMATICAL FORMULA:
   - Time: O(1), Space: O(1)
   - Most efficient - constant time!
   - No loop needed
   - Best for production code

5. LIST COMPREHENSION:
   - Time: O(n), Space: O(n)
   - Pythonic and concise
   - Creates intermediate list (memory overhead)
   - Good for small to medium n

6. REDUCE FUNCTION:
   - Time: O(n), Space: O(1)
   - Functional programming style
   - Requires importing functools
   - Less readable for beginners

7. GENERATOR EXPRESSION:
   - Time: O(n), Space: O(1)
   - Memory efficient (no list creation)
   - More efficient than list comprehension
   - Recommended for large n values

8. ITERTOOLS.ACCUMULATE:
   - Time: O(n), Space: O(n)
   - Creates all intermediate sums
   - Useful when you need cumulative results
   - Overkill for just final sum

RECOMMENDATIONS:
----------------
- For learning: Use FOR LOOP or WHILE LOOP
- For production: Use MATHEMATICAL FORMULA (most efficient)
- For large n: Use GENERATOR EXPRESSION or FORMULA
- For functional style: Use REDUCE or LIST COMPREHENSION
- Avoid RECURSION for large n due to stack overflow risk

MATHEMATICAL BACKGROUND:
------------------------
The sum of first n natural numbers follows the formula:
    Sum = 1 + 2 + 3 + ... + n = n(n + 1) / 2

This formula was discovered by Carl Friedrich Gauss as a child.
It eliminates the need for loops and provides constant-time solution.
""")

