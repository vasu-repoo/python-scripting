import time                                   # gives you time.sleep()

my_time = int(input("Enter the time in seconds: "))   # user types seconds, converted to a number

for x in range(my_time, 0, -1):               # counts DOWN from my_time to 1
    seconds = x % 60                          # leftover seconds after removing full minutes
    minutes = int(x / 60) % 60                # full minutes, wrapped at 60
    hours = int(x / 3600)                     # full hours
    print(f"{hours:02}:{minutes:02}:{seconds:02}")   # prints like 01:00:05
    time.sleep(1)                             # waits 1 second between prints

print("TIME'S UP!")                           # runs after the loop ends