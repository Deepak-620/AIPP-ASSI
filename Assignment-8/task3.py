import string
from typing import Union

def is_sentence_palindrome(sentence: Union[str, int, None]) -> bool:
    if not isinstance(sentence, str):
        return False
    
    cleaned = ''.join(char.lower() for char in sentence if char.isalnum())
    
    return cleaned == cleaned[::-1]

def run_tests():
    test_cases = [
        ("A man a plan a canal Panama", True, "Classic palindrome with spaces and case"),
        ("race a car", False, "Non-palindrome phrase"),
        ("Was it a car or a cat I saw?", True, "Palindrome with punctuation and question mark"),
        ("Madam, I'm Adam", True, "Palindrome with apostrophe and comma"),
        ("hello", False, "Simple non-palindrome word"),
        ("racecar", True, "Simple palindrome word"),
        ("A", True, "Single character"),
        ("", True, "Empty string"),
        ("aa", True, "Two identical characters"),
        ("ab", False, "Two different characters"),
        ("Able was I ere I saw Elba", True, "Historical palindrome"),
        ("12321", True, "Numeric palindrome"),
        ("12345", False, "Non-palindromic numbers"),
        ("A1B1A", True, "Alphanumeric palindrome"),
        ("Never odd or even", True, "Palindrome with multiple words"),
        ("Do geese see God?", True, "Palindrome with question mark"),
        ("Madam", True, "Palindrome - case insensitive"),
        ("Step on no pets", True, "Palindrome phrase"),
        ("Hello World", False, "Non-palindromic phrase"),
        ("Mr. Owl ate my metal worm", True, "Complex palindrome"),
        (".,!@#$%^&*()", True, "Only special characters"),
        ("   ", True, "Only spaces"),
        ("!@#", True, "Only punctuation"),
        ("A", True, "Single letter"),
        ("NoLemon,NoMelon", True, "Palindrome with punctuation"),
        ("abc123321cba", True, "Mixed alphanumeric palindrome"),
        ("ABC123321CBA", True, "Mixed case alphanumeric palindrome"),
        ("The quick brown fox", False, "Non-palindromic sentence"),
        ("Radar", True, "Common palindrome word"),
        ("Level", True, "Another common palindrome"),
        ("121", True, "Numeric palindrome"),
        ("a", True, "Single lowercase letter"),
        ("Z", True, "Single uppercase letter"),
        ("Noon", True, "Palindrome - case insensitive"),
        ("civic", True, "Palindrome word"),
        ("Dad", True, "Palindrome - case insensitive"),
        ("Mom", True, "Palindrome - case insensitive"),
        ("Go hang a salami, I'm a lasagna hog!", True, "Long complex palindrome"),
        (123, False, "Integer input - invalid"),
        (None, False, "None input - invalid"),
        ([], False, "List input - invalid"),
        ({}, False, "Dictionary input - invalid"),
    ]
    
    passed = 0
    failed = 0
    
    print("=" * 90)
    print("SENTENCE PALINDROME VALIDATOR TEST SUITE")
    print("=" * 90)
    
    for sentence, expected, description in test_cases:
        result = is_sentence_palindrome(sentence)
        status = "PASS" if result == expected else "FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"\n[{status}] {description}")
        print(f"    Input: '{sentence}' (type: {type(sentence).__name__})")
        print(f"    Expected: {expected}")
        print(f"    Got: {result}")
    
    print("\n" + "=" * 90)
    print(f"Test Results: {passed} passed, {failed} failed out of {len(test_cases)} total")
    pass_percentage = (passed / len(test_cases)) * 100
    print(f"Pass Rate: {pass_percentage:.1f}%")
    print("=" * 90)

if __name__ == "__main__":
    run_tests()
