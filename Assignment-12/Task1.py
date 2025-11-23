def linear_search(lst, target):
    """
    Perform a linear search for 'target' in the list 'lst'.
    Returns the index of 'target' if found, otherwise returns -1.
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


# Example usage:
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    x = 30

    result = linear_search(data, x)
    if result != -1:
        print(f"Value {x} found at index {result}")
    else:
        print(f"Value {x} not found in the list")