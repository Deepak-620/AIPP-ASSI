def cm_to_inches(cm: float) -> float:
	return float(cm) / 2.54


if __name__ == "__main__":
	try:
		s = input("Enter length in centimeters: ")
		if s.strip() == "":
			raise SystemExit
		value = float(s)
	except ValueError:
		print("Please enter a valid number")
	else:
		print(f"{value} cm = {cm_to_inches(value):.4f} inches")

