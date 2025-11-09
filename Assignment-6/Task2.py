def print_multiples_for(number):
    for i in range(1, 11):
        multiple = number * i
        print(f"{number} × {i} = {multiple}")


def print_multiples_while(number):
    i = 1
    while i <= 10:
        multiple = number * i
        print(f"{number} × {i} = {multiple}")
        i += 1


def print_multiples_enumerate(number):
    numbers_list = list(range(1, 11))
    for index, multiplier in enumerate(numbers_list, start=1):
        multiple = number * multiplier
        print(f"{number} × {multiplier} = {multiple}")


def print_multiples_comprehension(number):
    multiples = [f"{number} × {i} = {number * i}" for i in range(1, 11)]
    print("\n".join(multiples))


if __name__ == "__main__":
    test_number = 7
    
    print("Implementation #1: FOR Loop")
    print_multiples_for(test_number)
    
    print("\nImplementation #2: WHILE Loop")
    print_multiples_while(test_number)
    
    print("\nImplementation #3: FOR Loop with Enumerate")
    print_multiples_enumerate(test_number)
    
    print("\nImplementation #4: List Comprehension")
    print_multiples_comprehension(test_number)
