class Student:
    """
    Represents a student with a name, age, and a list of marks.
    """

    def __init__(self, name, age, marks):
        """
        Initialize a new Student instance.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            marks (list[int] or tuple[int]): List or tuple of the student's marks.
        """
        self.name = name
        self.age = age
        self.marks = list(marks)

    def details(self):
        """
        Prints the student's name and age in a readable format.
        """
        print(f"Name: {self.name}, Age: {self.age}")

    def total(self):
        """
        Returns the total of the student's marks.

        Returns:
            int: The sum of all marks.
        """
        return sum(self.marks)
