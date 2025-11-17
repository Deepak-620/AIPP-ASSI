class Employee:
    """
    Represents an employee with a name and salary.
    Provides methods to adjust salary and display employee information.
    """

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        """
        Increases the employee's salary by a given percentage.
        """
        self.salary += self.salary * (percent / 100)

    def display_info(self):
        """
        Displays formatted information about the employee.
        """
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary:.2f}")
emp1 = Employee("Rahul", 50000)
emp1.increase_salary(10)
emp1.display_info()
