class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item of the stack without removing it.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def __len__(self):
        """Return the number of items in the stack."""
        return len(self.items)


# Testing edge cases
if __name__ == "__main__":
    s = Stack()
    # Test pop and peek on empty stack (should raise exceptions)
    try:
        s.pop()
    except IndexError as e:
        print(f"Pop on empty: {e}")

    try:
        s.peek()
    except IndexError as e:
        print(f"Peek on empty: {e}")

    # Test normal behavior
    s.push(10)
    s.push(20)
    print(s.peek())   # Should print 20
    print(s.pop())    # Should print 20
    print(len(s))     # Should print 1

    # Test popping all elements
    print(s.pop())    # Should print 10
    print(s.is_empty())  # Should print True

    # Should raise again
    try:
        s.pop()
    except IndexError as e:
        print(f"Pop on empty again: {e}")

"""
Improvements:
- Used exceptions to provide clear error reporting for invalid pop/peek operations.
- Added `is_empty` and `__len__` for easier usability and checking stack state.
- Included basic tests to check edge case and normal usage.
"""
