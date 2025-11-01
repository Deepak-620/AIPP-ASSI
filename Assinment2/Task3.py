import math
from typing import Optional
"""Calculate area of various shapes from user input and print the result."""

def calculate_area(shape: str, **dimensions) -> Optional[float]:
        """Return the area for supported shapes or None if shape is unknown."""
        shape = shape.lower()
        if shape == "circle":
            radius = float(dimensions.get("radius", 0))
            return math.pi * radius * radius
        elif shape == "rectangle":
            width = float(dimensions.get("width", 0))
            height = float(dimensions.get("height", 0))
            return width * height
        elif shape == "triangle":
            base = float(dimensions.get("base", 0))
            height = float(dimensions.get("height", 0))
            return 0.5 * base * height
        elif shape == "square":
            side = float(dimensions.get("side", 0))
            return side * side
        return None


def _prompt_float(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt).strip())
            except ValueError:
                print("Please enter a valid number.")


def main():
        print("Area calculator. Supported shapes: circle, rectangle, triangle, square")
        while True:
            shape = input("\nEnter shape (or 'quit' to exit): ").strip().lower()
            if shape in ("quit", "exit"):
                print("Goodbye.")
                break

            if shape == "circle":
                r = _prompt_float("Enter radius: ")
                area = calculate_area("circle", radius=r)
            elif shape == "rectangle":
                w = _prompt_float("Enter width: ")
                h = _prompt_float("Enter height: ")
                area = calculate_area("rectangle", width=w, height=h)
            elif shape == "triangle":
                b = _prompt_float("Enter base: ")
                h = _prompt_float("Enter height: ")
                area = calculate_area("triangle", base=b, height=h)
            elif shape == "square":
                s = _prompt_float("Enter side length: ")
                area = calculate_area("square", side=s)
            else:
                print("Shape not recognized. Try again.")
                continue

            if area is None:
                print("Could not calculate area.")
            else:
                print(f"Area of the {shape}: {area:.4f}")


if __name__ == "__main__":
        main()
