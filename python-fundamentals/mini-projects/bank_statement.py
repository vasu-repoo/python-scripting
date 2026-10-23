
from datetime import datetime

transactions = []
balance = 0.0

print("===== MINI BANK STATEMENT GENERATOR =====")
name = input("Enter customer name: ")
account = input("Enter account number: ")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. View Statement")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice in ("1", "2"):
        amount = float(input("Enter amount (Rs.): "))

        if amount <= 0:
            print("Amount must be positive.")
            continue

        if choice == "2" and amount > balance:
            print("Insufficient balance!")
            continue

        if choice == "1":
            balance += amount
            transaction_type = "Deposit"
        else:
            balance -= amount
            transaction_type = "Withdrawal"

        transactions.append({
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "type": transaction_type,
            "amount": amount,
            "balance": balance
        })

        print(f"{transaction_type} successful!")
        print(f"Current balance: Rs. {balance:.2f}")

    elif choice == "3":
        print("\n========== BANK STATEMENT ==========")
        print("Customer:", name)
        print("Account:", account)
        print("-" * 65)
        print(f"{'Date':<18} {'Type':<12} {'Amount':>10} {'Balance':>12}")

        for t in transactions:
            print(f"{t['date']:<18} {t['type']:<12} "
                  f"{t['amount']:>10.2f} {t['balance']:>12.2f}")

        print("-" * 65)
        print(f"Available Balance: Rs. {balance:.2f}")

    elif choice == "4":
        print("Thank you for using the Mini Bank Statement Generator!")
        break

    else:
        print("Invalid choice. Try again.")
