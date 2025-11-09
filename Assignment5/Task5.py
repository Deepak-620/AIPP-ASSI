def greet_user(name, gender):
    gender = gender.lower()

    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Mrs."
    else:
        title = "Mx."  # Gender-neutral title

    return f"Hello, {title} {name}! Welcome."

# Example calls:
print(greet_user("John", "Male"))
print(greet_user("Priya", "Female"))
print(greet_user("Alex", "Non-binary"))
