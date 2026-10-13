
print("""
***********************
      CALCULATOR
***********************
""")

while True:
    print("""
ENTER 1 for +  (Addition)
ENTER 2 for -  (Subtraction)
ENTER 3 for *  (Multiplication)
ENTER 4 for ** (Power)
ENTER 5 for %  (Modulus)
ENTER 6 for /  (Division)
ENTER 7 to Exit
""")

    try:
        operator_choice = int(input("ENTER NUMBER FOR OPERATION: "))

        if operator_choice == 7:
            print("Thank you for using the calculator!")
            break

        if operator_choice not in [1, 2, 3, 4, 5, 6]:
            print("Please enter a valid choice!")
            continue

        num1 = float(input("ENTER FIRST NUMBER: "))
        num2 = float(input("ENTER SECOND NUMBER: "))

        match operator_choice:
            case 1:
                result = num1 + num2
            case 2:
                result = num1 - num2
            case 3:
                result = num1 * num2
            case 4:
                result = num1 ** num2
            case 5:
                if num2 == 0:
                    print("Error: Modulus by zero is not allowed!")
                    continue
                result = num1 % num2
            case 6:
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2

        print("RESULT:", result)

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except OverflowError:
        print("Error: The result is too large to calculate.")