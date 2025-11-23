def bubble_sort(lst):
    """
    Sort the list 'lst' in ascending order using the Bubble Sort algorithm.
    Returns a new sorted list (does not modify the original list).
    """
    items = lst.copy()  # work on a copy to avoid changing the original
    n = len(items)

    for i in range(n):
        # After each pass, the largest element among the unsorted part
        # is bubbled to its correct position at the end.
        swapped = False
        for j in range(0, n - 1 - i):
            if items[j] > items[j + 1]:
                # Swap the elements
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        # If no two elements were swapped by inner loop, list is already sorted
        if not swapped:
            break

    return items


if __name__ == "__main__":
    # Example list to sort
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", data)

    sorted_data = bubble_sort(data)
    print("Sorted list:  ", sorted_data)

    # Simple check to confirm output is sorted
    print("Is correctly sorted?", sorted_data == sorted(data))


