# Function to reverse a string
def reverse_string(s: str) -> str:
	"""Return the reverse of the input string `s`.

	This implementation is straightforward and handles Unicode characters.

	Examples:
	>>> reverse_string('abc')
	'cba'
	>>> reverse_string('')
	'A'
	"""
	# Using Python slicing which is efficient and concise.
	return s[::-1]


if __name__ == "__main__":
	# quick demo when run directly
	examples = ["hello", "AIPP", "12345", "RAM"]
	for ex in examples:
		print(f"{ex} -> {reverse_string(ex)}")

# Recursive factorial implementation
def factorial_recursive(n: int) -> int:
	"""Compute n! recursively.

	- Raises ValueError for negative inputs.
	- Uses the mathematical definition:
		0! = 1
		n! = n * (n-1)!  for n > 0

	Note: recursion is simple and readable, but for large n it may hit
	Python's recursion limit.
	"""
	if n < 0:
		raise ValueError("factorial is not defined for negative numbers")
	if n <= 1:
		return 1
	return n * factorial_recursive(n - 1)


# Iterative factorial implementation
def factorial_iterative(n: int) -> int:
	"""Compute n! using an iterative loop.

	- Raises ValueError for negative inputs.
	- Preferred in Python for large n because it avoids recursion depth
	  and function call overhead.
	"""
	if n < 0:
		raise ValueError("factorial is not defined for negative numbers")
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


if __name__ == "__main__":
	# quick demo when run directly
	examples = ["hello", "AIPP", "12345", "RAM"]
	for ex in examples:
		print(f"{ex} -> {reverse_string(ex)}")

	# factorial demo
	nums = [0, 1, 5, 7]
	print("\nFactorial demos:")
	for n in nums:
		print(f"{n}! (recursive) = {factorial_recursive(n)}")
		print(f"{n}! (iterative) = {factorial_iterative(n)}")
