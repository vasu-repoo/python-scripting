def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to deposit: $"))

    if amount <= 0:
        print("That's not a valid amount.")
        return 0

    return amount


def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: $"))

    if amount <= 0:
        print("That's not a valid amount.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount


def main():
    balance = 0

    while True:
        print("\n********************")
        print("   Banking Program")
        print("********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance += deposit()

        elif choice == "3":
            balance -= withdraw(balance)

        elif choice == "4":
            print("Thank you! Have a nice day.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()