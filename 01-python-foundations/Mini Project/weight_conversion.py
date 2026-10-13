print("""
************************
    WEIGHT CONVERTER
************************
""")

print("""
1. Kilograms to Pounds
2. Pounds to Kilograms
3. Kilograms to Grams
4. Grams to Kilograms
5. Kilograms to Ounces
6. Ounces to Kilograms
7. Exit
""")
# reattemting process
while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice == 7:
            print("Thank you for using the converter!")
            break

        if choice not in [1, 2, 3, 4, 5, 6]:
            print("Invalid choice! Try again.")
            continue

        weight = float(input("Enter weight: "))

        if weight < 0:
            print("Weight cannot be negative!")
            continue

        match choice:
            case 1:
                result = weight * 2.20462
                unit = "pounds"

            case 2:
                result = weight / 2.20462
                unit = "kilograms"

            case 3:
                result = weight * 1000
                unit = "grams"

            case 4:
                result = weight / 1000
                unit = "kilograms"

            case 5:
                result = weight * 35.274
                unit = "ounces"

            case 6:
                result = weight / 35.274
                unit = "kilograms"

        print("Converted weight:", round(result, 2), unit)

    except ValueError:
        print("Invalid input! Please enter a number.")