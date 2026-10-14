def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("-------------------------")
        print(key)

        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(
            questions[key], guess
        )

        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):

    print("\n-------------------------")
    print("         RESULTS")
    print("-------------------------")

    print("Answers: ", end="")

    for answer in questions.values():
        print(answer, end=" ")

    print("\nGuesses: ", end="")

    for guess in guesses:
        print(guess, end=" ")

    score = int((correct_guesses / len(questions)) * 100)

    print(f"\nYour score is: {score}%")


def play_again():

    response = input(
        "\nDo you want to play again? (yes or no): "
    ).lower()

    return response == "yes"


questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "A",
    "Which comedy group inspired Python's name?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk",
     "C. Bill Gates", "D. Mark Zuckerberg"],

    ["A. 1989", "B. 1995",
     "C. 2000", "D. 2010"],

    ["A. Smosh", "B. SNL",
     "C. Monty Python", "D. Lonely Island"],

    ["A. True", "B. False",
     "C. Sometimes", "D. None of these"]
]


new_game()

while play_again():
    new_game()

print("Byeeeeee!")