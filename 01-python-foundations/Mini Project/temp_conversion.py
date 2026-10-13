print('''
*****************************
    TEMPERATURE CONVERTER
*****************************''')
# for user 
print("""
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
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

        temp = float(input("Enter temperature: "))

        match choice:
            case 1:
                result = (temp * 9/5) + 32
                unit = "Fahrenheit"

            case 2:
                result = (temp - 32) * 5/9
                unit = "Celsius"

            case 3:
                result = temp + 273.15
                unit = "Kelvin"

            case 4:
                result = temp - 273.15
                unit = "Celsius"

            case 5:
                result = (temp - 32) * 5/9 + 273.15
                unit = "Kelvin"

            case 6:
                result = (temp - 273.15) * 9/5 + 32
                unit = "Fahrenheit"

        print("Converted temperature:", round(result, 2), unit)

    except ValueError:
        print("Invalid input! Please enter a number.")
