def grade(score):
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

# Test Outputs
print(grade(95))
print(grade(82))
print(grade(74))
print(grade(67))
print(grade(40))
