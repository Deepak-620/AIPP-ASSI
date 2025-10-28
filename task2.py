
from typing import Iterable


def is_prime(n: int) -> bool:
	"""Return True if n is prime, otherwise False.

	
	Examples:
	>>> is_prime(2)
	True
	>>> is_prime(15)
	False
	>>> is_prime(17)
	True
	"""
	from typing import Iterable


	def is_prime(n: int) -> bool:
		"""Return True if n is prime, otherwise False.

		Examples:
		>>> is_prime(2)
		True
		>>> is_prime(15)
		False
		>>> is_prime(17)
		True
		"""
		if n <= 1:
			return False
		if n <= 3:
			return True
		if n % 2 == 0 or n % 3 == 0:
			return False

		i = 5
		# check divisors up to sqrt(n), step by 6 (i and i+2 are 6k-1 and 6k+1)
		while i * i <= n:
			if n % i == 0 or n % (i + 2) == 0:
				return False
			i += 6
		return True


	def run_tests(cases: Iterable[int]) -> None:
		"""Run quick checks and print results for given cases."""
		for x in cases:
			print(f"{x}: {'prime' if is_prime(x) else 'composite'}")


	def factorial_recursive(n: int) -> int:
		"""Compute factorial of n using recursion.

		- Raises ValueError for negative inputs.
		- Uses the mathematical definition:
			0! = 1
			n! = n * (n-1)!  for n > 0

		Note: Recursive approach is simple and mirrors the definition, but it
		can lead to deep recursion for large n (Python recursion limit).
		"""
		if n < 0:
			raise ValueError("factorial is not defined for negative numbers")
		if n <= 1:
			return 1
		return n * factorial_recursive(n - 1)


	def factorial_iterative(n: int) -> int:
		"""Compute factorial of n using an iterative loop.

		- Raises ValueError for negative inputs.
		- More efficient in Python for large n because it avoids recursion depth
		  limits and function call overhead.
		"""
		if n < 0:
			raise ValueError("factorial is not defined for negative numbers")
		result = 1
		for i in range(2, n + 1):
			result *= i
		return result


	def interactive_main() -> None:
		"""Prompt the user for integers and report primality and factorials.

		- Enter an integer to test for primality and show its factorial (if
		  reasonably sized). Press Enter on an empty line to exit.
		"""
		print("Prime & Factorial utility — enter an integer to test (press Enter to quit)")
		while True:
			try:
				s = input("Enter integer: ").strip()
			except EOFError:
				print()
				break
			if s == "":
				print("Exiting.")
				break
			try:
				n = int(s)
			except ValueError:
				print("Invalid input. Please enter a valid integer.")
				continue

			# primality
			if is_prime(n):
				print(f"{n} is prime.")
			else:
				print(f"{n} is not prime.")

			# factorial (guarded to avoid huge output)
			if n < 0:
				print("factorial not defined for negative numbers")
			elif n > 1000:
				print("factorial too large to compute/display (n > 1000)")
			else:
				print(f"{n}! = {factorial_iterative(n)}")


	if __name__ == "__main__":
		interactive_main()

