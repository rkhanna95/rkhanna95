def calculate_tax_and_salary(gross_salary):
    """
    Calculate income tax and in-hand salary based on gross salary.
    Uses simplified tax brackets for old regime.
    Includes monthly breakdown.
    """
    # Standard deduction
    standard_deduction = 50000
    
    # Taxable income after standard deduction
    taxable_income = max(0, gross_salary - standard_deduction)
    
    # Tax brackets (old regime example)
    if taxable_income <= 250000:
        tax_rate = 0.0
        tax_amount = 0
    elif taxable_income <= 500000:
        tax_rate = 0.05
        tax_amount = (taxable_income - 250000) * tax_rate
    elif taxable_income <= 1000000:
        tax_rate = 0.20
        tax_amount = 12500 + (taxable_income - 500000) * tax_rate  # 5% on first 250k, 20% on next
    else:
        tax_rate = 0.30
        tax_amount = 12500 + 100000 + (taxable_income - 1000000) * tax_rate  # plus 30% on excess
    
    # Add 4% cess
    cess = tax_amount * 0.04
    total_tax = tax_amount + cess
    
    in_hand_salary = gross_salary - total_tax
    
    # Monthly breakdown
    monthly_gross = gross_salary / 12
    monthly_tax = total_tax / 12
    monthly_in_hand = monthly_gross - monthly_tax
    
    # Month-by-month details (assuming uniform)
    monthly_details = []
    cumulative_tax = 0
    cumulative_in_hand = 0
    for month in range(1, 13):
        cumulative_tax += monthly_tax
        cumulative_in_hand += monthly_in_hand
        monthly_details.append({
            "month": month,
            "monthly_gross": monthly_gross,
            "monthly_tax_deduction": monthly_tax,
            "monthly_in_hand": monthly_in_hand,
            "cumulative_tax": cumulative_tax,
            "cumulative_in_hand": cumulative_in_hand
        })
    
    return {
        "gross_salary": gross_salary,
        "standard_deduction": standard_deduction,
        "taxable_income": taxable_income,
        "tax_amount": tax_amount,
        "cess": cess,
        "total_tax": total_tax,
        "tax_rate": tax_rate * 100,
        "in_hand_salary": in_hand_salary,
        "monthly_gross": monthly_gross,
        "monthly_tax": monthly_tax,
        "monthly_in_hand": monthly_in_hand,
        "monthly_details": monthly_details
    }


def main():
    print("=== Detailed Income Tax & In-Hand Salary Calculator ===\n")
    
    try:
        gross_salary = float(input("Enter your gross annual salary: "))
        
        if gross_salary < 0:
            print("Salary cannot be negative!")
            return
        
        result = calculate_tax_and_salary(gross_salary)
        
        print(f"\nAnnual Summary:")
        print(f"Gross Salary:          ₹{result['gross_salary']:,.2f}")
        print(f"Standard Deduction:     ₹{result['standard_deduction']:,.2f}")
        print(f"Taxable Income:         ₹{result['taxable_income']:,.2f}")
        print(f"Tax Amount (before cess): ₹{result['tax_amount']:,.2f}")
        print(f"Cess (4%):              ₹{result['cess']:,.2f}")
        print(f"Total Tax:              ₹{result['total_tax']:,.2f}")
        print(f"Effective Tax Rate:     {result['tax_rate']:.1f}%")
        print(f"Annual In-Hand Salary:  ₹{result['in_hand_salary']:,.2f}")
        
        print(f"\nMonthly Breakdown:")
        print(f"Monthly Gross:          ₹{result['monthly_gross']:,.2f}")
        print(f"Monthly Tax Deduction:  ₹{result['monthly_tax']:,.2f}")
        print(f"Monthly In-Hand:        ₹{result['monthly_in_hand']:,.2f}")
        
        print(f"\nMonth-by-Month Details:")
        print(f"{'Month':<5} {'Gross':<10} {'Tax Ded.':<10} {'In-Hand':<10} {'Cum. Tax':<10} {'Cum. In-Hand':<12}")
        print("-" * 70)
        for detail in result['monthly_details']:
            print(f"{detail['month']:<5} ₹{detail['monthly_gross']:<9,.0f} ₹{detail['monthly_tax_deduction']:<9,.0f} ₹{detail['monthly_in_hand']:<9,.0f} ₹{detail['cumulative_tax']:<9,.0f} ₹{detail['cumulative_in_hand']:<11,.0f}")
    
    except ValueError:
        print("Please enter a valid number!")


if __name__ == "__main__":
    main()