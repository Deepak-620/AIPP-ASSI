"""TGNPDCL Electricity Bill Calculator

Calculates electricity bill components for Domestic and Commercial customers:
- EC (Energy Charges)
- FC (Fixed Charges)
- CC (Customer Charges)
- ED (Electricity Duty)

Example rates used (for demonstration):
Domestic:
    - Up to 100 units: ₹3.50/unit
    - 101-200 units: ₹4.60/unit
    - Above 200 units: ₹6.90/unit
    - FC: ₹65
    - CC: ₹35
    - ED: 6% of EC

Commercial:
    - Up to 100 units: ₹6.90/unit
    - Above 100 units: ₹8.50/unit
    - FC: ₹185
    - CC: ₹65
    - ED: 8% of EC
"""

from enum import Enum
from typing import Dict, Tuple


class CustomerType(Enum):
    DOMESTIC = "domestic"
    COMMERCIAL = "commercial"


# Rate constants
RATES = {
    CustomerType.DOMESTIC: {
        "slabs": [(100, 3.50), (200, 4.60), (float('inf'), 6.90)],
        "fc": 65.0,
        "cc": 35.0,
        "ed_percent": 6.0
    },
    CustomerType.COMMERCIAL: {
        "slabs": [(100, 6.90), (float('inf'), 8.50)],
        "fc": 185.0,
        "cc": 65.0,
        "ed_percent": 8.0
    }
}


def calculate_ec(units: float, customer_type: CustomerType) -> float:
    """Calculate Energy Charges (EC) based on units consumed and customer type.
    
    Args:
        units: Number of units consumed
        customer_type: Type of customer (DOMESTIC or COMMERCIAL)
        
    Returns:
        Total EC amount
    """
    remaining_units = units
    total_ec = 0.0
    
    for limit, rate in RATES[customer_type]["slabs"]:
        if remaining_units <= 0:
            break
        
        units_in_slab = min(remaining_units, limit)
        if limit != float('inf'):
            units_in_slab = min(units_in_slab, limit)
        
        total_ec += units_in_slab * rate
        remaining_units -= units_in_slab
        
        if limit == float('inf'):
            break
            
    return total_ec


def calculate_bill_components(units: float, 
                            customer_type: CustomerType) -> Dict[str, float]:
    """Calculate all bill components.
    
    Args:
        units: Number of units consumed
        customer_type: Type of customer (DOMESTIC or COMMERCIAL)
        
    Returns:
        Dictionary containing EC, FC, CC, ED and total amount
    """
    rates = RATES[customer_type]
    
    # Calculate components
    ec = calculate_ec(units, customer_type)
    fc = rates["fc"]
    cc = rates["cc"]
    ed = (ec * rates["ed_percent"]) / 100.0
    
    # Calculate total
    total = ec + fc + cc + ed
    
    return {
        "EC": ec,
        "FC": fc,
        "CC": cc,
        "ED": ed,
        "Total": total
    }


def print_bill(components: Dict[str, float], units: float, 
               customer_type: CustomerType) -> None:
    """Print formatted electricity bill.
    
    Args:
        components: Dictionary containing bill components
        units: Number of units consumed
        customer_type: Type of customer
    """
    print("\n" + "=" * 40)
    print("        TGNPDCL ELECTRICITY BILL")
    print("=" * 40)
    
    print(f"\nCustomer Type: {customer_type.name}")
    print(f"Units Consumed: {units:.2f}")
    
    print("\nBill Components:")
    print("-" * 40)
    
    # Print each component with proper alignment
    print(f"Energy Charges (EC)    : ₹{components['EC']:>10.2f}")
    print(f"Fixed Charges (FC)     : ₹{components['FC']:>10.2f}")
    print(f"Customer Charges (CC)  : ₹{components['CC']:>10.2f}")
    print(f"Electricity Duty (ED)  : ₹{components['ED']:>10.2f}")
    print("-" * 40)
    print(f"Total Amount          : ₹{components['Total']:>10.2f}")
    print("=" * 40)


def get_valid_units() -> float:
    """Get valid number of units from user input."""
    while True:
        try:
            units = float(input("Enter number of units consumed: "))
            if units < 0:
                print("Units cannot be negative.")
                continue
            return units
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_customer_type() -> CustomerType:
    """Get valid customer type from user input."""
    print("\nCustomer Types:")
    print("1. Domestic")
    print("2. Commercial")
    
    while True:
        choice = input("\nEnter customer type (1 or 2): ").strip()
        if choice == "1":
            return CustomerType.DOMESTIC
        elif choice == "2":
            return CustomerType.COMMERCIAL
        else:
            print("Invalid choice. Please enter 1 for Domestic or 2 for Commercial.")


def main():
    """Main program loop."""
    print("TGNPDCL Electricity Bill Calculator")
    print("-" * 35)
    
    while True:
        # Get inputs
        units = get_valid_units()
        customer_type = get_customer_type()
        
        # Calculate and display bill
        components = calculate_bill_components(units, customer_type)
        print_bill(components, units, customer_type)
        
        # Ask to continue
        if input("\nCalculate another bill? (y/n): ").lower() != 'y':
            break
    
    print("\nThank you for using the TGNPDCL Bill Calculator!")


if __name__ == "__main__":
    main()
