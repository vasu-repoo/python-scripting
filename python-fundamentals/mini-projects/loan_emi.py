
print("===== LOAN EMI CALCULATOR =====")

principal = float(input("Enter loan amount (Rs.): "))
annual_rate = float(input("Enter annual interest rate (%): "))
months = int(input("Enter loan duration (months): "))

if principal <= 0 or annual_rate < 0 or months <= 0:
    print("Invalid input. Please enter valid values.")
else:
    monthly_rate = annual_rate / 1200

    if monthly_rate == 0:
        emi = principal / months
    else:
        factor = (1 + monthly_rate) ** months
        emi = principal * monthly_rate * factor / (factor - 1)

    total_payment = emi * months
    total_interest = total_payment - principal

    print("\n========== LOAN SUMMARY ==========")
    print(f"Loan Amount:       Rs. {principal:.2f}")
    print(f"Annual Rate:       {annual_rate:.2f}%")
    print(f"Loan Duration:     {months} months")
    print(f"Monthly EMI:       Rs. {emi:.2f}")
    print(f"Total Interest:    Rs. {total_interest:.2f}")
    print(f"Total Repayment:   Rs. {total_payment:.2f}")
