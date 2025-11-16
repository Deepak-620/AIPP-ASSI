from typing import Union

def assign_grade(score: Union[int, float]) -> str:
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        return "Invalid input: score must be a number"
    
    if score < 0 or score > 100:
        return "Invalid input: score must be between 0 and 100"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def run_tests():
    test_cases = [
        (100, "A", "Upper boundary - perfect score"),
        (90, "A", "Lower boundary for A grade"),
        (89, "B", "Just below A boundary"),
        (80, "B", "Lower boundary for B grade"),
        (79, "C", "Just below B boundary"),
        (70, "C", "Lower boundary for C grade"),
        (69, "D", "Just below C boundary"),
        (60, "D", "Lower boundary for D grade"),
        (59, "F", "Just below D boundary"),
        (0, "F", "Lowest valid score"),
        (95, "A", "Mid-range A score"),
        (85, "B", "Mid-range B score"),
        (75, "C", "Mid-range C score"),
        (65, "D", "Mid-range D score"),
        (30, "F", "Low F score"),
        (-5, "Invalid input: score must be between 0 and 100", "Negative score"),
        (105, "Invalid input: score must be between 0 and 100", "Score exceeds 100"),
        (150, "Invalid input: score must be between 0 and 100", "Score far exceeds 100"),
        ("eighty", "Invalid input: score must be a number", "String input"),
        ("90", "Invalid input: score must be a number", "String number"),
        (None, "Invalid input: score must be a number", "None input"),
        ([], "Invalid input: score must be a number", "List input"),
        ({}, "Invalid input: score must be a number", "Dictionary input"),
        (90.5, "A", "Floating point A score"),
        (85.3, "B", "Floating point B score"),
        (72.7, "C", "Floating point C score"),
        (61.1, "D", "Floating point D score"),
        (45.9, "F", "Floating point F score"),
        (True, "Invalid input: score must be a number", "Boolean input"),
        (False, "Invalid input: score must be a number", "Boolean False input"),
    ]
    
    passed = 0
    failed = 0
    
    print("=" * 80)
    print("GRADE ASSIGNMENT TEST SUITE")
    print("=" * 80)
    
    for score, expected, description in test_cases:
        result = assign_grade(score)
        status = "PASS" if result == expected else "FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"\n[{status}] {description}")
        print(f"    Input: {score} (type: {type(score).__name__})")
        print(f"    Expected: {expected}")
        print(f"    Got: {result}")
    
    print("\n" + "=" * 80)
    print(f"Test Results: {passed} passed, {failed} failed out of {len(test_cases)} total")
    print("=" * 80)

if __name__ == "__main__":
    run_tests()
