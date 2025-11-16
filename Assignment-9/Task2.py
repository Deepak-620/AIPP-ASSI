class SRUStudent:
    # Initialize the student object with basic information
    def __init__(self, name: str, roll_no: str, hostel_status: bool):
        # Store the student's name
        self.name = name
        # Store the student's roll number
        self.roll_no = roll_no
        # Store whether the student is in hostel (True) or day scholar (False)
        self.hostel_status = hostel_status
        # Initialize the fee amount to zero
        self.fee_amount = 0.0
    
    # Update the student's fee amount
    def fee_update(self, amount: float) -> bool:
        # Check if the amount is a valid positive number
        if not isinstance(amount, (int, float)) or amount < 0:
            # Return False if amount is invalid
            return False
        # Add the new amount to existing fees
        self.fee_amount += amount
        # Return True to indicate successful fee update
        return True
    
    # Display all student details
    def display_details(self) -> None:
        # Print the student's name
        print(f"Name: {self.name}")
        # Print the student's roll number
        print(f"Roll No: {self.roll_no}")
        # Check hostel status and print appropriate message
        if self.hostel_status:
            # If hostel_status is True, student is in hostel
            print("Hostel Status: Hostel")
        else:
            # If hostel_status is False, student is a day scholar
            print("Hostel Status: Day Scholar")
        # Print the total fee amount with two decimal places
        print(f"Fee Amount: Rs. {self.fee_amount:.2f}")


class SRUStudentAICommented:
    # Initializes a student instance with name, roll number, and hostel residency status
    def __init__(self, name: str, roll_no: str, hostel_status: bool):
        # Assigns the provided name parameter to the instance variable self.name
        self.name = name
        # Assigns the provided roll_no parameter to the instance variable self.roll_no
        self.roll_no = roll_no
        # Assigns the provided hostel_status parameter indicating if student resides in hostel
        self.hostel_status = hostel_status
        # Initializes the fee_amount attribute to 0.0 for tracking accumulated fees
        self.fee_amount = 0.0
    
    # Processes fee updates by accepting a monetary amount and adding it to the student's account
    def fee_update(self, amount: float) -> bool:
        # Validates that amount is numeric (int or float) and non-negative before processing
        if not isinstance(amount, (int, float)) or amount < 0:
            # Returns False if validation fails, indicating unsuccessful fee update operation
            return False
        # Accumulates the new amount to the existing fee_amount balance
        self.fee_amount += amount
        # Returns True to confirm the fee update was successfully processed
        return True
    
    # Outputs formatted student information including personal details and financial status
    def display_details(self) -> None:
        # Prints the student's name using formatted string output
        print(f"Name: {self.name}")
        # Prints the student's roll number using formatted string output
        print(f"Roll No: {self.roll_no}")
        # Evaluates the hostel_status boolean to determine residential classification
        if self.hostel_status:
            # Prints "Hostel" when hostel_status is True, indicating on-campus residence
            print("Hostel Status: Hostel")
        else:
            # Prints "Day Scholar" when hostel_status is False, indicating off-campus residence
            print("Hostel Status: Day Scholar")
        # Formats and prints the total accumulated fee amount with currency label and 2 decimal precision
        print(f"Fee Amount: Rs. {self.fee_amount:.2f}")


def demonstrate_functionality():
    # Create and demonstrate manual comment version
    print("=" * 60)
    print("MANUAL COMMENTS VERSION")
    print("=" * 60)
    
    # Create a new student object with example data
    student1 = SRUStudent("Rajesh Kumar", "SRU2024001", True)
    # Display the student's initial details
    student1.display_details()
    # Add first fee payment
    print("\nUpdating fee with Rs. 5000...")
    student1.fee_update(5000)
    # Display updated details
    student1.display_details()
    # Add second fee payment
    print("\nUpdating fee with Rs. 3000...")
    student1.fee_update(3000)
    # Display final details
    student1.display_details()
    
    print("\n" + "=" * 60)
    print("AI-GENERATED COMMENTS VERSION")
    print("=" * 60)
    
    # Create instance of AI-commented version with same data
    student2 = SRUStudentAICommented("Priya Singh", "SRU2024002", False)
    # Display initial student information
    student2.display_details()
    # Process first fee transaction
    print("\nUpdating fee with Rs. 5500...")
    student2.fee_update(5500)
    # Output updated student record
    student2.display_details()
    # Process second fee transaction
    print("\nUpdating fee with Rs. 2500...")
    student2.fee_update(2500)
    # Display comprehensive student details after all updates
    student2.display_details()
    
    print("\n" + "=" * 60)
    print("TESTING INVALID INPUTS")
    print("=" * 60)
    
    # Create a test student for validation testing
    test_student = SRUStudent("Test Student", "SRU2024003", True)
    
    # Test with negative amount
    print("Testing negative fee (-1000):")
    result = test_student.fee_update(-1000)
    print(f"Update successful: {result}")
    
    # Test with string input
    print("\nTesting string input ('5000'):")
    result = test_student.fee_update("5000")
    print(f"Update successful: {result}")
    
    # Test with valid amount
    print("\nTesting valid input (2000):")
    result = test_student.fee_update(2000)
    print(f"Update successful: {result}")
    
    # Display final state
    test_student.display_details()


if __name__ == "__main__":
    demonstrate_functionality()
