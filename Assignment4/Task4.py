def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# take user input
user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))
