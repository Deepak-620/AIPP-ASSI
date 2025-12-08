"""Calculates the factorial of a number using recursion."""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    for i in [5, 0]:
        result = factorial(i)
        print(f"Input: {i} → Output: Factorial = {result}")

if __name__ == "__main__":
    main()