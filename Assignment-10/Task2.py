def find_common(a, b):
    return list(set(a) & set(b))

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(find_common(a, b))   # Output: [3, 4]
