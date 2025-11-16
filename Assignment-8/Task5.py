from typing import Union
import re

def convert_date_format(date_str: Union[str, int, None]) -> Union[str, bool]:
    if not isinstance(date_str, str):
        return False
    
    date_str = date_str.strip()
    
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        return False
    
    parts = date_str.split('-')
    year, month, day = parts[0], parts[1], parts[2]
    
    try:
        year_int = int(year)
        month_int = int(month)
        day_int = int(day)
        
        if month_int < 1 or month_int > 12:
            return False
        if day_int < 1 or day_int > 31:
            return False
        if year_int < 1000 or year_int > 9999:
            return False
        
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
            days_in_month[1] = 29
        
        if day_int > days_in_month[month_int - 1]:
            return False
        
        return f"{day:0>2}-{month:0>2}-{year}"
    
    except ValueError:
        return False

def run_tests():
    test_cases = [
        ("2023-10-15", "15-10-2023", "Standard date conversion"),
        ("2020-01-01", "01-01-2020", "First day of year"),
        ("2023-12-31", "31-12-2023", "Last day of year"),
        ("2000-06-15", "15-06-2000", "Year 2000"),
        ("1999-03-20", "20-03-1999", "Year 1999"),
        ("2024-02-29", "29-02-2024", "Leap year date"),
        ("2020-02-29", "29-02-2020", "Leap year February 29"),
        ("2100-01-01", "01-01-2100", "Future century"),
        ("1900-12-25", "25-12-1900", "Historical date"),
        ("2023-01-31", "31-01-2023", "Month with 31 days"),
        ("2023-04-30", "30-04-2023", "Month with 30 days"),
        ("2023-02-28", "28-02-2023", "February non-leap year"),
        ("2000-02-29", "29-02-2000", "Leap year divisible by 400"),
        ("1900-02-28", "28-02-1900", "Non-leap year (1900 not leap)"),
        ("2023-09-15", "15-09-2023", "Mid-month date"),
        ("2023-05-05", "05-05-2023", "Single digit day and month"),
        ("2023-10-01", "01-10-2023", "Single digit day"),
        ("2023-01-15", "15-01-2023", "Single digit month"),
        ("9999-12-31", "31-12-9999", "Maximum year"),
        ("1000-01-01", "01-01-1000", "Minimum valid year"),
        ("2023-10-15 ", "15-10-2023", "Trailing whitespace"),
        (" 2023-10-15", "15-10-2023", "Leading whitespace"),
        (" 2023-10-15 ", "15-10-2023", "Both leading and trailing whitespace"),
        ("2023-10-32", False, "Invalid day (32)"),
        ("2023-13-15", False, "Invalid month (13)"),
        ("2023-00-15", False, "Invalid month (00)"),
        ("2023-10-00", False, "Invalid day (00)"),
        ("2023-02-30", False, "Invalid February date"),
        ("2021-02-29", False, "February 29 in non-leap year"),
        ("999-10-15", False, "Year too short"),
        ("10000-10-15", False, "Year too long"),
        ("2023/10/15", False, "Wrong separator (slash)"),
        ("2023.10.15", False, "Wrong separator (dot)"),
        ("10-15-2023", False, "Wrong format (DD-MM-YYYY)"),
        ("15-10-2023", False, "Already converted format"),
        ("2023-10", False, "Incomplete date"),
        ("2023-10-15-01", False, "Extra date component"),
        ("abcd-10-15", False, "Non-numeric year"),
        ("2023-ab-15", False, "Non-numeric month"),
        ("2023-10-ab", False, "Non-numeric day"),
        ("", False, "Empty string"),
        ("2023-10-15\n", "15-10-2023", "Newline character"),
        (None, False, "None input"),
        (20231015, False, "Integer input"),
        (2023.1015, False, "Float input"),
        ([], False, "List input"),
        ({}, False, "Dictionary input"),
    ]
    
    passed = 0
    failed = 0
    
    print("=" * 90)
    print("DATE FORMAT CONVERSION TEST SUITE")
    print("=" * 90)
    print("\nConverting from YYYY-MM-DD to DD-MM-YYYY\n")
    
    for date_input, expected, description in test_cases:
        result = convert_date_format(date_input)
        status = "PASS" if result == expected else "FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"[{status}] {description}")
        print(f"    Input: '{date_input}' (type: {type(date_input).__name__})")
        print(f"    Expected: {expected}")
        print(f"    Got: {result}")
        print()
    
    print("=" * 90)
    print(f"Test Results: {passed} passed, {failed} failed out of {len(test_cases)} total")
    pass_percentage = (passed / len(test_cases)) * 100
    print(f"Pass Rate: {pass_percentage:.1f}%")
    print("=" * 90)

if __name__ == "__main__":
    run_tests()
