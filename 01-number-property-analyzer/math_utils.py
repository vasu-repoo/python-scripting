'''What you build: A program that checks properties of numbers and performs calculations.'''
'''For example, if the input is 153, it checks whether it's prime, Armstrong, or a palindrome, and can calculate its factorial or the average of a list.'''

def is_prime(number: int) -> bool:
    """Return True if number is prime."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def is_armstrong(number: int) -> bool:
    """Return True if number is an Armstrong number."""
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    return total == number


def is_palindrome(number: int) -> bool:
    """Return True if number reads the same backward."""
    if number < 0:
        return False

    digits = str(number)
    return digits == digits[::-1]


def factorial(number: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def calculate_sum(numbers: list[int | float]) -> int | float:
    """Return the sum of the numbers."""
    return sum(numbers)


def calculate_average(numbers: list[int | float]) -> float:
    """Return the average of the numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    while True:
        print("\n===== NUMBER PROPERTY ANALYZER =====")
        print("1. Number Analyzer")
        print("2. List Analyzer")
        print("3. Both Analyzers")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1" or choice == "3":
            try:
                number = int(input("\nEnter an integer: "))

                print("\n--- Number Analysis ---")
                print("Number:", number)
                print("Prime:", is_prime(number))
                print("Armstrong:", is_armstrong(number))
                print("Palindrome:", is_palindrome(number))

                try:
                    print("Factorial:", factorial(number))
                except ValueError as error:
                    print("Factorial error:", error)

            except ValueError:
                print("Invalid input! Please enter an integer.")

        if choice == "2" or choice == "3":
            try:
                user_input = input(
                    "\nEnter numbers separated by spaces: "
                ).strip()

                if not user_input:
                    print("Please enter at least one number.")
                    continue

                numbers = [
                    float(value) for value in user_input.split()
                ]

                print("\n--- List Analysis ---")
                print("List:", numbers)
                print("Sum:", calculate_sum(numbers))
                print("Average:", calculate_average(numbers))

            except ValueError:
                print("Invalid input! Enter numbers separated by spaces.")

        elif choice == "4":
            print("Thank you for using the analyzer!")
            break

        elif choice not in ("1", "2", "3"):
            print("Invalid choice! Please select 1, 2, 3, or 4.")