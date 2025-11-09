def classify_age_if_elif_else(age):
    if age < 0:
        return "Invalid Age"
    elif age <= 12:
        return "Child"
    elif age <= 17:
        return "Teen"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"


def classify_age_match_case(age):
    if age < 0:
        return "Invalid Age"
    elif age <= 12:
        category = "child"
    elif age <= 17:
        category = "teen"
    elif age <= 64:
        category = "adult"
    else:
        category = "senior"
    
    match category:
        case "child":
            return "Child"
        case "teen":
            return "Teen"
        case "adult":
            return "Adult"
        case "senior":
            return "Senior"
        case _:
            return "Invalid Age"


def classify_age_ternary(age):
    return ("Invalid Age" if age < 0 else
            "Child" if age <= 12 else
            "Teen" if age <= 17 else
            "Adult" if age <= 64 else
            "Senior")


def classify_age_dictionary(age):
    age_ranges = {
        (0, 12): "Child",
        (13, 17): "Teen",
        (18, 64): "Adult",
        (65, 200): "Senior"
    }
    
    if age < 0:
        return "Invalid Age"
    
    for (min_age, max_age), category in age_ranges.items():
        if min_age <= age <= max_age:
            return category
    return "Invalid Age"


def classify_age_nested_if(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        else:
            if age <= 17:
                return "Teen"
            else:
                if age <= 64:
                    return "Adult"
                else:
                    return "Senior"
    else:
        return "Invalid Age"


if __name__ == "__main__":
    print("=" * 60)
    print("AGE CLASSIFICATION SYSTEM")
    print("=" * 60)
    
    test_ages = [5, 15, 25, 70, -5]
    
    print("\nImplementation #1: if-elif-else")
    print("-" * 60)
    for age in test_ages:
        result = classify_age_if_elif_else(age)
        print(f"Age {age}: {result}")
    
    print("\nImplementation #2: Match-Case")
    print("-" * 60)
    for age in test_ages:
        result = classify_age_match_case(age)
        print(f"Age {age}: {result}")
    
    print("\nImplementation #3: Ternary Operator")
    print("-" * 60)
    for age in test_ages:
        result = classify_age_ternary(age)
        print(f"Age {age}: {result}")
    
    print("\nImplementation #4: Dictionary-Based")
    print("-" * 60)
    for age in test_ages:
        result = classify_age_dictionary(age)
        print(f"Age {age}: {result}")
    
    print("\nImplementation #5: Nested If-Else")
    print("-" * 60)
    for age in test_ages:
        result = classify_age_nested_if(age)
        print(f"Age {age}: {result}")
    
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\nEnter an age (or 'quit' to exit): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thank you for using Age Classification System!")
                break
            
            age = int(user_input)
            
            print(f"\nAge Classification Results:")
            print(f"  if-elif-else:     {classify_age_if_elif_else(age)}")
            print(f"  Match-Case:       {classify_age_match_case(age)}")
            print(f"  Ternary:          {classify_age_ternary(age)}")
            print(f"  Dictionary:       {classify_age_dictionary(age)}")
            print(f"  Nested If-Else:   {classify_age_nested_if(age)}")
            
        except ValueError:
            print("Error: Please enter a valid integer age.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
