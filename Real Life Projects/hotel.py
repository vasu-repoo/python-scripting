
import sqlite3

db = sqlite3.connect("hotel.db")
db.execute("""
CREATE TABLE IF NOT EXISTS rooms(
    number INTEGER PRIMARY KEY,
    rate REAL NOT NULL,
    guest TEXT,
    checkin TEXT
)
""")
db.executemany(
    "INSERT OR IGNORE INTO rooms(number,rate) VALUES(?,?)",
    [(i, 1500 + (i - 100) * 100) for i in range(101, 111)]
)
db.commit()


def view_rooms():
    for r in db.execute("SELECT * FROM rooms ORDER BY number"):
        status = "Available" if r[2] is None else f"Guest: {r[2]}"
        print(f"Room {r[0]} | Rs.{r[1]}/night | {status}")


def checkin():
    view_rooms()
    try:
        number = int(input("Room number: "))
        guest = input("Guest name: ").strip()
        if not guest:
            print("Guest name required.")
            return

        cur = db.execute("""
            UPDATE rooms SET guest=?, checkin=CURRENT_TIMESTAMP
            WHERE number=? AND guest IS NULL
        """, (guest, number))
        db.commit()
        print("Check-in successful." if cur.rowcount else
              "Room unavailable or does not exist.")
    except ValueError:
        print("Invalid room number.")


def checkout():
    try:
        number = int(input("Room number: "))
        nights = int(input("Number of nights: "))
        if nights <= 0:
            print("Nights must be positive.")
            return

        r = db.execute(
            "SELECT rate,guest FROM rooms WHERE number=?", (number,)
        ).fetchone()

        if not r or r[1] is None:
            print("No active guest in that room.")
            return

        total = r[0] * nights
        print(f"Guest: {r[1]}")
        print(f"Total bill: Rs.{total:.2f}")

        confirm = input("Confirm checkout? (y/n): ").lower()
        if confirm == "y":
            db.execute("""
                UPDATE rooms SET guest=NULL,checkin=NULL WHERE number=?
            """, (number,))
            db.commit()
            print("Checkout complete.")
    except ValueError:
        print("Enter valid numbers.")


while True:
    print("\n--- HOTEL MANAGEMENT ---")
    print("1. View rooms")
    print("2. Check in")
    print("3. Check out")
    print("0. Exit")

    c = input("> ")
    if c == "1":
        view_rooms()
    elif c == "2":
        checkin()
    elif c == "3":
        checkout()
    elif c == "0":
        break
    else:
        print("Invalid choice.")

db.close()
