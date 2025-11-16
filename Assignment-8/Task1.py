import re
from typing import List, Tuple

def is_valid_email(email: str) -> bool:
    if not email or not isinstance(email, str):
        return False
    
    if email.count('@') != 1:
        return False
    
    if email.startswith(('.', '@', '-', '_')) or email.endswith(('.', '@', '-', '_')):
        return False
    
    local_part, domain_part = email.split('@')
    
    if not local_part or not domain_part:
        return False
    
    if '.' not in domain_part:
        return False
    
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    
    if '..' in email:
        return False
    
    valid_chars_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+$'
    if not re.match(valid_chars_pattern, email):
        return False
    
    domain_labels = domain_part.split('.')
    for label in domain_labels:
        if not label or not re.match(r'^[a-zA-Z0-9-]+$', label):
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
    
    return True

def run_tests() -> None:
    test_cases: List[Tuple[str, bool, str]] = [
        ("user@example.com", True, "Valid email with standard format"),
        ("john.doe@company.co.uk", True, "Valid email with dot in local part and multi-level domain"),
        ("test_email@domain.com", True, "Valid email with underscore in local part"),
        ("user123@test-domain.com", True, "Valid email with numbers and hyphen in domain"),
        
        ("invalidemail", False, "Missing @ character"),
        ("user@domain", False, "Missing . in domain"),
        ("user@@domain.com", False, "Multiple @ characters"),
        ("user@domain@com", False, "Multiple @ characters"),
        
        (".user@domain.com", False, "Starts with special character (dot)"),
        ("@user@domain.com", False, "Starts with @ character"),
        ("-user@domain.com", False, "Starts with hyphen"),
        ("_user@domain.com", False, "Starts with underscore"),
        ("user@domain.com.", False, "Email ends with dot"),
        ("user@domain.com@", False, "Ends with @ character"),
        ("user@domain.com-", False, "Ends with hyphen"),
        
        ("user@.domain.com", False, "Domain starts with dot"),
        ("user@domain..com", False, "Double dots in domain"),
        ("user..name@domain.com", False, "Double dots in local part"),
        
        ("", False, "Empty string"),
        ("   ", False, "Whitespace only"),
        ("user @domain.com", False, "Space in email"),
        ("user@dom ain.com", False, "Space in domain"),
        
        ("user+tag@example.com", False, "Plus sign not allowed per requirements"),
        ("user#name@domain.com", False, "Hash character not allowed"),
        ("user$name@domain.com", False, "Dollar sign not allowed"),
        
        ("a@b.c", True, "Valid minimal email"),
        ("test123@test456.org", True, "Valid email with numbers"),
        ("first-name@last-name.com", True, "Valid email with hyphens"),
        
        (None, False, "None type"),
        (123, False, "Integer type"),
    ]
    
    print("Email Validator Test Cases")
    print("=" * 80)
    
    passed = 0
    failed = 0
    
    for email, expected, description in test_cases:
        try:
            result = is_valid_email(email)
            status = "PASS" if result == expected else "FAIL"
            
            if result == expected:
                passed += 1
            else:
                failed += 1
            
            print(f"{status}: {description}")
            print(f"       Input: {repr(email)}")
            print(f"       Expected: {expected}, Got: {result}")
            print("-" * 80)
        except Exception as e:
            failed += 1
            print(f"ERROR: {description}")
            print(f"       Input: {repr(email)}")
            print(f"       Exception: {str(e)}")
            print("-" * 80)
    
    print("\n" + "=" * 80)
    print(f"Test Results: {passed} PASSED, {failed} FAILED out of {len(test_cases)} total")
    print(f"Success Rate: {(passed / len(test_cases) * 100):.1f}%")

if __name__ == "__main__":
    run_tests()
