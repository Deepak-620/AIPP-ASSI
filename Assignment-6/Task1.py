# AI-generated Student class

class Student:
    # Constructor to initialize attributes
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    # Method to display student details
    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


# ---- Main Program ----
# Creating an object of Student class
student1 = Student("Ram", 101, "Computer Science")

# Displaying the student details
student1.display_details()
