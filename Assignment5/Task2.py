from dataclasses import dataclass
from typing import Optional
import random

@dataclass
class LoanApplication:
    applicant_name: str
    age: int
    annual_income: float
    credit_score: int
    employment_years: float
    loan_amount: float
    gender: str
    occupation: str

class LoanApprovalSystem:
    def __init__(self):
        self.min_credit_score = 650
        self.min_income_ratio = 0.3
        self.min_age = 18
        self.max_age = 65
    
    def evaluate_application(self, application: LoanApplication) -> tuple[bool, str, float]:
        if application.age < self.min_age or application.age > self.max_age:
            return False, "Age requirements not met", 0.0
            
        if application.credit_score < self.min_credit_score:
            return False, "Credit score too low", 0.0
            
        monthly_payment = application.loan_amount / 36
        monthly_income = application.annual_income / 12
        
        if monthly_payment / monthly_income > self.min_income_ratio:
            return False, "Debt-to-income ratio too high", 0.0
            
        risk_score = self.calculate_risk_score(application)
        interest_rate = self.calculate_interest_rate(risk_score)
        
        return True, "Loan approved", interest_rate
    
    def calculate_risk_score(self, application: LoanApplication) -> float:
        base_score = (
            (application.credit_score / 850) * 40 +
            (min(application.employment_years, 10) / 10) * 30 +
            (min(application.annual_income / 100000, 1)) * 30
        )
        return base_score
    
    def calculate_interest_rate(self, risk_score: float) -> float:
        base_rate = 5.0
        return round(base_rate + (100 - risk_score) * 0.1, 2)

def test_loan_approval_system():
    system = LoanApprovalSystem()
    
    test_applications = [
        LoanApplication("Sarah Johnson", 30, 75000, 720, 5, 150000, "Female", "Engineer"),
        LoanApplication("Michael Chen", 35, 80000, 750, 7, 200000, "Male", "Doctor"),
        LoanApplication("Maria Garcia", 28, 65000, 680, 3, 120000, "Female", "Teacher"),
        LoanApplication("James Wilson", 45, 90000, 800, 15, 250000, "Male", "Manager"),
        LoanApplication("Aisha Patel", 32, 70000, 700, 6, 180000, "Female", "Architect"),
        LoanApplication("David Kim", 29, 60000, 640, 2, 100000, "Male", "Designer"),
        LoanApplication("Emma Thompson", 38, 85000, 760, 8, 220000, "Female", "Lawyer"),
        LoanApplication("Ahmed Hassan", 33, 72000, 690, 4, 160000, "Male", "Accountant")
    ]
    
    print("\nLoan Application Results:")
    print("-" * 80)
    
    for application in test_applications:
        approved, reason, rate = system.evaluate_application(application)
        result = "APPROVED" if approved else "DENIED"
        rate_str = f"@ {rate}%" if approved else ""
        
        print(f"{application.applicant_name} ({application.gender}, {application.occupation})")
        print(f"Income: ${application.annual_income:,.2f} | Credit Score: {application.credit_score}")
        print(f"Result: {result} {rate_str}")
        print(f"Reason: {reason}")
        print("-" * 80)

if __name__ == "__main__":
    test_loan_approval_system()
