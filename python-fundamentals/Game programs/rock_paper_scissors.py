import random

options = ("r", "p", "s")

names = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (r for rock, p for paper, s for scissors): ").lower()

print(f"Player: {names[player]}")
print(f"Computer: {names[computer]}")

if player == computer:
    print("It's a tie!")
elif player == "r" and computer == "s":
    print("You win!")
elif player == "p" and computer == "r":
    print("You win!")
elif player == "s" and computer == "p":
    print("You win!")
else:
    print("You lose!")