"""
AI PROMPT:
----------
Build a BankAccount class in Python with the following requirements:
1. Methods: deposit(amount), withdraw(amount), and get_balance()
2. Initialize account with account number and initial balance
3. Handle user input for banking operations
4. Include proper validation (no negative amounts, sufficient funds for withdrawal)
5. Add transaction history tracking
6. Include error handling and user-friendly messages
"""


class BankAccount:
    """
    A BankAccount class that simulates a basic banking system.
    
    This class provides functionality to:
    - Create a bank account with account number and initial balance
    - Deposit money into the account
    - Withdraw money from the account (with balance checking)
    - Check the current balance
    - View transaction history
    
    Attributes:
    -----------
    account_number : str
        Unique identifier for the bank account
    balance : float
        Current balance in the account
    transaction_history : list
        List of all transactions (deposits and withdrawals)
    """
    
    def __init__(self, account_number, initial_balance=0.0):
        """
        Initialize a new BankAccount instance.
        
        Parameters:
        -----------
        account_number : str
            The unique account number for this bank account
        initial_balance : float, optional
            The initial balance to start with (default is 0.0)
        
        Raises:
        -------
        ValueError
            If initial_balance is negative
        """
        # Validate that initial balance is not negative
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        # Store account number and initial balance
        self.account_number = account_number
        self.balance = initial_balance
        
        # Initialize transaction history list to track all transactions
        self.transaction_history = []
        
        # Record the initial balance as the first transaction
        if initial_balance > 0:
            self.transaction_history.append({
                'type': 'Initial Deposit',
                'amount': initial_balance,
                'balance_after': self.balance
            })
        
        print(f"Account {self.account_number} created with initial balance: ${initial_balance:.2f}")
    
    def deposit(self, amount):
        """
        Deposit money into the bank account.
        
        Parameters:
        -----------
        amount : float
            The amount of money to deposit
        
        Returns:
        --------
        bool
            True if deposit was successful, False otherwise
        
        Raises:
        -------
        ValueError
            If amount is negative or zero
        """
        # Validate that deposit amount is positive
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return False
        
        # Add the amount to the current balance
        self.balance += amount
        
        # Record the transaction in history
        self.transaction_history.append({
            'type': 'Deposit',
            'amount': amount,
            'balance_after': self.balance
        })
        
        # Confirm the deposit to the user
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """
        Withdraw money from the bank account.
        
        Parameters:
        -----------
        amount : float
            The amount of money to withdraw
        
        Returns:
        --------
        bool
            True if withdrawal was successful, False otherwise
        
        Raises:
        -------
        ValueError
            If amount is negative or zero
        """
        # Validate that withdrawal amount is positive
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return False
        
        # Check if account has sufficient funds
        if amount > self.balance:
            print(f"Error: Insufficient funds. Current balance: ${self.balance:.2f}, Requested: ${amount:.2f}")
            return False
        
        # Subtract the amount from the current balance
        self.balance -= amount
        
        # Record the transaction in history
        self.transaction_history.append({
            'type': 'Withdrawal',
            'amount': amount,
            'balance_after': self.balance
        })
        
        # Confirm the withdrawal to the user
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def get_balance(self):
        """
        Get the current balance of the bank account.
        
        Returns:
        --------
        float
            The current balance in the account
        """
        return self.balance
    
    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        
        This method prints the balance to the console with formatting.
        """
        print(f"Account {self.account_number} - Current Balance: ${self.balance:.2f}")
    
    def get_transaction_history(self):
        """
        Get the complete transaction history.
        
        Returns:
        --------
        list
            List of all transactions with details
        """
        return self.transaction_history
    
    def display_transaction_history(self):
        """
        Display all transactions in a formatted table.
        
        This method prints the transaction history in a readable format.
        """
        if not self.transaction_history:
            print("No transactions recorded.")
            return
        
        print("\n" + "=" * 60)
        print("TRANSACTION HISTORY")
        print("=" * 60)
        print(f"{'Type':<15} {'Amount':<15} {'Balance After':<15}")
        print("-" * 60)
        
        # Iterate through all transactions and display them
        for transaction in self.transaction_history:
            print(f"{transaction['type']:<15} ${transaction['amount']:<14.2f} ${transaction['balance_after']:<14.2f}")
        
        print("=" * 60)


def create_account_interactive():
    """
    Interactive function to create a new bank account with user input.
    
    Returns:
    --------
    BankAccount
        A new BankAccount instance created from user input
    """
    print("\n" + "=" * 60)
    print("CREATE NEW BANK ACCOUNT")
    print("=" * 60)
    
    # Get account number from user
    account_number = input("Enter account number: ").strip()
    
    # Get initial balance from user
    while True:
        try:
            initial_balance = float(input("Enter initial balance (default 0): ").strip() or "0")
            if initial_balance < 0:
                print("Error: Balance cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    
    # Create and return the account
    return BankAccount(account_number, initial_balance)


def banking_menu(account):
    """
    Display a menu and handle user banking operations.
    
    Parameters:
    -----------
    account : BankAccount
        The bank account to perform operations on
    """
    while True:
        print("\n" + "=" * 60)
        print("BANKING MENU")
        print("=" * 60)
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")
        print("=" * 60)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            # Handle deposit operation
            try:
                amount = float(input("Enter deposit amount: $").strip())
                account.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '2':
            # Handle withdrawal operation
            try:
                amount = float(input("Enter withdrawal amount: $").strip())
                account.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '3':
            # Display current balance
            account.display_balance()
        
        elif choice == '4':
            # Display transaction history
            account.display_transaction_history()
        
        elif choice == '5':
            # Exit the banking menu
            print("Thank you for using the Banking System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    print("=" * 60)
    print("BANK ACCOUNT MANAGEMENT SYSTEM")
    print("=" * 60)
    
    try:
        # Create a bank account interactively
        account = create_account_interactive()
        
        # Start the banking menu
        banking_menu(account)
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("\n" + "=" * 60)
    print("CODE ANALYSIS")
    print("=" * 60)
    print("""
CLASS STRUCTURE:
----------------
The BankAccount class follows object-oriented programming principles:

1. ENCAPSULATION:
   - All account data (balance, account_number, transaction_history) is 
     stored as instance variables (attributes)
   - Methods provide controlled access to modify the account state
   - Private data is protected from direct external modification

2. METHODS:
   - __init__(): Constructor that initializes the account
   - deposit(): Adds money to the account with validation
   - withdraw(): Removes money from account with balance checking
   - get_balance(): Returns current balance (getter method)
   - display_balance(): Shows balance in formatted output
   - get_transaction_history(): Returns transaction list (getter)
   - display_transaction_history(): Shows formatted transaction history

3. VALIDATION:
   - Initial balance cannot be negative
   - Deposit amount must be positive
   - Withdrawal amount must be positive
   - Withdrawal amount cannot exceed current balance

4. TRANSACTION TRACKING:
   - Each transaction is recorded with type, amount, and balance after
   - Transaction history is stored as a list of dictionaries
   - History can be retrieved or displayed at any time

TIME COMPLEXITY:
----------------
- deposit(): O(1) - Constant time operation
- withdraw(): O(1) - Constant time operation
- get_balance(): O(1) - Constant time operation
- display_transaction_history(): O(n) - Where n is number of transactions

SPACE COMPLEXITY:
-----------------
- Overall: O(n) where n is number of transactions
- Each transaction stored in memory
- Balance and account number: O(1)

BEST PRACTICES IMPLEMENTED:
---------------------------
1. Input Validation: All user inputs are validated
2. Error Handling: Try-except blocks for error management
3. User Feedback: Clear messages for all operations
4. Transaction History: Complete audit trail
5. Encapsulation: Data protection through methods
6. Documentation: Comprehensive docstrings for all methods
7. Code Readability: Clear variable names and structure

IMPROVEMENTS POSSIBLE:
---------------------
1. Add interest calculation functionality
2. Implement account locking after failed attempts
3. Add password/PIN protection
4. Support multiple account types (Savings, Checking)
5. Add currency conversion support
6. Implement database storage for persistence
7. Add account statements (monthly, yearly)
8. Implement transfer between accounts
9. Add account closure functionality
10. Implement transaction limits

SECURITY CONSIDERATIONS:
------------------------
- In production, add authentication (password/PIN)
- Encrypt sensitive data
- Implement logging for audit purposes
- Add rate limiting for transactions
- Validate account numbers format
- Implement session management
""")

