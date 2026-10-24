
import random
import os
import time
import textwrap

# ==========================================
# THE LAST NIGHT: ABANDONED HOSPITAL
# A terminal-based survival horror game
# ==========================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress ENTER to continue...")


def slow_print(text, delay=0.015):
    """Print atmospheric text one character at a time."""
    for char in text:
        print(char, end="", flush=True)
        if char not in " \n":
            time.sleep(delay)
    print()


def banner():
    print(r"""
    +--------------------------------------+
    |          THE LAST NIGHT              |
    |       ABANDONED HOSPITAL             |
    +--------------------------------------+
    """)


def show_status(player):
    print("\n" + "=" * 42)
    print(f" HEALTH:   {player['health']}/100")
    print(f" BATTERY:  {player['battery']}%")
    print(f" SANITY:   {player['sanity']}/100")
    print(f" LOCATION: {player['location']}")
    print("=" * 42)

    if player["inventory"]:
        print(" INVENTORY:", ", ".join(player["inventory"]))
    else:
        print(" INVENTORY: Empty")


def game_over(message):
    print("\n")
    print("#" * 44)
    print(message.center(44))
    print("#" * 44)
    print("\nYour story ends in the darkness...")


def encounter_monster(player):
    """Random encounter with the hospital monster."""
    print("\n!!! SOMETHING IS MOVING !!!")
    slow_print("A tall figure emerges from the darkness...")

    print("\nWhat will you do?")
    print("1. Run")
    print("2. Hide")
    print("3. Use your flashlight")

    choice = input("> ").strip()

    if choice == "1":
        if random.random() < 0.65:
            slow_print("You sprint away. Its footsteps chase you!")
            player["health"] -= random.randint(5, 20)
            player["sanity"] -= 8
            print("You escaped, but you were injured.")
        else:
            slow_print("It catches you before you reach the door.")
            player["health"] -= random.randint(25, 40)

    elif choice == "2":
        if random.random() < 0.70:
            slow_print("You hold your breath behind a cabinet.")
            slow_print("Something sniffs the air, then walks away.")
            player["sanity"] -= 5
        else:
            slow_print("It finds your hiding place!")
            player["health"] -= random.randint(20, 35)

    elif choice == "3":
        if player["battery"] >= 10:
            player["battery"] -= 10
            if random.random() < 0.80:
                slow_print("The bright beam blinds the creature!")
                slow_print("You escape into the next room.")
            else:
                slow_print("It barely reacts to the light!")
                player["health"] -= 20
        else:
            slow_print("Your flashlight flickers and dies.")
            slow_print("The creature attacks in the darkness!")
            player["health"] -= 30

    else:
        print("You freeze in terror!")
        player["health"] -= 15
        player["sanity"] -= 10

    player["health"] = max(0, player["health"])
    player["sanity"] = max(0, player["sanity"])

    print(f"\nHealth: {player['health']}")
    print(f"Sanity: {player['sanity']}")


def explore_room(player, room):
    """Explore a room and discover items or clues."""
    clear()
    banner()

    player["location"] = room
    print(f"\nLOCATION: {room.upper()}\n")

    descriptions = {
        "Reception": (
            "Dust covers the desk. A broken telephone rings "
            "once, then goes silent."
        ),
        "Patient Ward": (
            "Rows of empty beds stand beneath flickering lights. "
            "Something has scratched the walls."
        ),
        "Storage Room": (
            "Medical supplies litter the floor. A metal cabinet "
            "hangs open."
        ),
        "Basement": (
            "The air smells of rust and damp concrete. "
            "You hear breathing behind the pipes."
        ),
        "Security Office": (
            "Dead monitors line the walls. One screen still "
            "shows a hallway behind you."
        ),
        "Exit Corridor": (
            "An emergency exit stands at the end of the corridor. "
            "A heavy electronic lock blocks the door."
        )
    }

    slow_print(descriptions.get(room, "The room is cold and silent."))

    # One-time room discoveries
    if room not in player["visited"]:
        player["visited"].add(room)

        if room == "Reception":
            if "Basement Key" not in player["inventory"]:
                print("\nYou find a rusty key inside the desk.")
                player["inventory"].append("Basement Key")

        elif room == "Patient Ward":
            if "Medical Kit" not in player["inventory"]:
                print("\nYou discover an unopened medical kit.")
                player["inventory"].append("Medical Kit")
                print("You can use it to restore 30 health.")

        elif room == "Storage Room":
            if "Battery" not in player["inventory"]:
                print("\nA fresh battery lies beneath a shelf.")
                player["inventory"].append("Battery")

        elif room == "Basement":
            if "Exit Keycard" not in player["inventory"]:
                print("\nInside a locked drawer, you find a keycard.")
                player["inventory"].append("Exit Keycard")

        elif room == "Security Office":
            if "Secret Note" not in player["inventory"]:
                print("\nA note reads:")
                print('"The exit requires a keycard. '
                      'The creature fears bright light."')
                player["inventory"].append("Secret Note")

    # Random events
    if room != "Reception" and random.random() < 0.30:
        player["sanity"] = max(0, player["sanity"] - 5)
        slow_print("\nA whisper crawls through the walls...")
        print("Sanity -5")

    if random.random() < 0.30:
        encounter_monster(player)

    pause()


def main():
    player = {
        "health": 100,
        "battery": 60,
        "sanity": 100,
        "inventory": [],
        "visited": set(),
        "location": "Entrance"
    }

    rooms = {
        "1": "Reception",
        "2": "Patient Ward",
        "3": "Storage Room",
        "4": "Basement",
        "5": "Security Office",
        "6": "Exit Corridor"
    }

    clear()
    banner()

    print("11:47 PM. A storm rages outside.")
    slow_print(
        "\nYou wake up on the floor of an abandoned hospital. "
        "The front doors are chained shut."
    )
    slow_print(
        "Somewhere in the building, something drags its nails "
        "along the walls."
    )
    print("\nOBJECTIVE: Find the exit keycard and escape alive.")
    pause()

    while True:
        clear()
        banner()
        show_status(player)

        if player["health"] <= 0:
            game_over("YOU DIED")
            break

        if player["sanity"] <= 0:
            game_over("YOU LOST YOUR MIND")
            break

        if player["battery"] <= 0:
            print("\nYour flashlight is completely dead.")

        print("\nWhat would you like to do?")
        print("1. Explore Reception")
        print("2. Explore Patient Ward")
        print("3. Explore Storage Room")
        print("4. Explore Basement")
        print("5. Explore Security Office")
        print("6. Go to Exit Corridor")
        print("7. Use an item")
        print("8. Check inventory")
        print("9. Rest for a moment")
        print("0. Quit game")

        choice = input("\nYour choice > ").strip()

        if choice in rooms:
            room = rooms[choice]

            if room == "Basement":
                if "Basement Key" not in player["inventory"]:
                    print("\nThe basement door is locked.")
                    print("You need the Basement Key.")
                    pause()
                    continue

            if room == "Exit Corridor":
                if "Exit Keycard" not in player["inventory"]:
                    print("\nACCESS DENIED.")
                    print("The exit needs an electronic keycard.")
                    pause()
                    continue

                clear()
                banner()
                slow_print(
                    "You swipe the keycard. The lock flashes green."
                )
                slow_print(
                    "\nThe door opens. Cold rain hits your face. "
                    "Behind you, something screams."
                )
                print("\n" + "*" * 42)
                print("       YOU ESCAPED THE HOSPITAL!")
                print("*" * 42)
                print("\nYou survived the last night.")
                break

            # Exploring consumes flashlight battery
            if player["battery"] > 0:
                player["battery"] = max(0, player["battery"] - 5)

            explore_room(player, room)

        elif choice == "7":
            clear()
            print("USE AN ITEM")
            print("-" * 25)

            usable = [
                item for item in player["inventory"]
                if item in ("Medical Kit", "Battery")
            ]

            if not usable:
                print("You have no usable items.")
                pause()
                continue

            for index, item in enumerate(usable, start=1):
                print(f"{index}. {item}")

            print("0. Cancel")
            item_choice = input("> ").strip()

            if item_choice == "0":
                continue

            if item_choice.isdigit():
                index = int(item_choice) - 1

                if 0 <= index < len(usable):
                    item = usable[index]

                    if item == "Medical Kit":
                        if player["health"] == 100:
                            print("Your health is already full.")
                        else:
                            player["health"] = min(
                                100, player["health"] + 30
                            )
                            player["inventory"].remove("Medical Kit")
                            print("You patch your wounds. Health restored!")

                    elif item == "Battery":
                        if player["battery"] == 100:
                            print("Your battery is already full.")
                        else:
                            player["battery"] = min(
                                100, player["battery"] + 40
                            )
                            player["inventory"].remove("Battery")
                            print("Flashlight battery recharged!")

                else:
                    print("Invalid item number.")
            else:
                print("Invalid choice.")

            pause()

        elif choice == "8":
            print("\nYOUR INVENTORY")
            print("-" * 25)

            if player["inventory"]:
                for item in player["inventory"]:
                    print(f"- {item}")
            else:
                print("Nothing but empty pockets.")

            pause()

        elif choice == "9":
            print("\nYou lean against a cold wall...")
            player["sanity"] = max(0, player["sanity"] - 3)

            if random.random() < 0.50:
                slow_print("A distant scream echoes through the hospital.")
                if random.random() < 0.50:
                    encounter_monster(player)
            else:
                print("For a moment, everything is silent.")

            pause()

        elif choice == "0":
            print("\nYou abandon the hospital...")
            print("GAME OVER.")
            break

        else:
            print("Invalid choice. Enter a number from 0 to 9.")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nYou left the nightmare. Goodbye!")
