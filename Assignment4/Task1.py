("""Assignment4 Task1: Leap year checker

Provides a small utility to check whether a given year is a leap year
according to the Gregorian calendar rules:

- A year is a leap year if it is divisible by 4,
  except years that are divisible by 100 are not leap years,
  unless they are divisible by 400 (those are leap years).

Example:
>>> is_leap_year(2000)
True
>>> is_leap_year(1900)
False
>>> is_leap_year(2024)
True
>>> is_leap_year(2023)
False
""")

from typing import Union


def is_leap_year(year: int) -> bool:
	
	if not isinstance(year, int):
		raise TypeError("year must be an integer")

	# divisible by 400 -> leap
	if year % 400 == 0:
		return True
	# divisible by 100 -> not leap
	if year % 100 == 0:
		return False
	# divisible by 4 -> leap
	if year % 4 == 0:
		return True
	return False


def _prompt_and_print() -> None:
	"""Prompt the user for a year and print whether it's a leap year."""
	while True:
		s = input("Enter a year (or press Enter to quit): ").strip()
		if s == "":
			print("Exiting.")
			break
		try:
			y = int(s)
		except ValueError:
			print("Please enter a valid integer year.")
			continue
		try:
			res = is_leap_year(y)
		except TypeError as e:
			print(e)
			continue
		print(f"{y} is a leap year." if res else f"{y} is not a leap year.")


if __name__ == "__main__":
	_prompt_and_print()

