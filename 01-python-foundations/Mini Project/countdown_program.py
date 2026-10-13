import time

def get_seconds():
    while True:
        try:
            seconds = int(input("Enter the time in seconds: "))
            if seconds > 0:
                return seconds
            print("Please enter a number greater than 0.")
        except ValueError:
            print("That's not a number. Try again.")

def countdown(total):
    try:
        for x in range(total, 0, -1):
            minutes, seconds = divmod(x, 60)
            hours, minutes = divmod(minutes, 60)
            print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="", flush=True)
            time.sleep(1)
        print("\rTIME'S UP!   ")
    except KeyboardInterrupt:
        print("\nTimer cancelled.")

countdown(get_seconds())