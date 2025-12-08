"""
Task 4: Data Structures with Functions
Translates a JavaScript function to Python for printing student names.
"""


def print_students(students):
    """
    Print each student name from a list.
    
    Args:
        students (list): A list of student names (strings).
    """
    print("Student List:")
    for student in students:
        print(student)


if __name__ == "__main__":
    # Test with sample student names
    sample_students = ["Alice", "Bob", "Charlie"]
    print_students(sample_students)