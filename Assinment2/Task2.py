"""Check if a string is a palindrome."""

def is_palindrome(s):
    """Return True if the string s is a palindrome, False otherwise."""
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1]  # Check if the string is the same forwards and backwards

def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()