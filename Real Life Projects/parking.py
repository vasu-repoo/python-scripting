
import sqlite3
from datetime import datetime
import math

db = sqlite3.connect("parking.db")
db.execute("""
CREATE TABLE IF NOT EXISTS vehicles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate TEXT NOT NULL,
    kind TEXT NOT NULL,
    entry TEXT NOT NULL,
    exit TEXT,
    fee REAL
)
""")
db.commit()


def entry():
    plate = input("Vehicle number: ").strip().upper()
    kind = input("Vehicle type (car/bike): ").strip().lower()

    if not plate or kind not in ("car", "bike"):
        print("Enter a valid plate and type.")
        return

    active = db.execute(
        "SELECT id FROM vehicles WHERE plate=? AND exit IS NULL",
        (plate,)
    ).fetchone()

    if active:
        print("Vehicle is already parked.")
        return

    db.execute(
        "INSERT INTO vehicles(plate,kind,entry) VALUES(?,?,?)",
        (plate, kind, datetime.now().isoformat(timespec="seconds"))
    )
    db.commit()
    print("Vehicle entry recorded.")


def exit_vehicle():
    plate = input("Vehicle number: ").strip().upper()
    row = db.execute("""
        SELECT id,kind,entry FROM vehicles
        WHERE plate=? AND exit IS NULL ORDER BY id DESC LIMIT 1
    """, (plate,)).fetchone()

    if not row:
        print("Active vehicle not found.")
        return

    start = datetime.fromisoformat(row[2])
    end = datetime.now()
    hours = max(1, math.ceil((end - start).total_seconds() / 3600))
    rate = 30 if row[1] == "car" else 10
    fee = hours * rate

    db.execute(
        "UPDATE vehicles SET exit=?,fee=? WHERE id=? AND exit IS NULL",
        (end.isoformat(timespec="seconds"), fee, row[0])
    )
    db.commit()

    print(f"Parking duration: {hours} hour(s)")
    print(f"Parking fee: Rs.{fee:.2f}")


while True:
    print("\n--- PARKING MANAGEMENT ---")
    print("1. Vehicle entry")
    print("2. Vehicle exit")
    print("3. Active vehicles")
    print("4. Parking history")
    print("0. Exit")

    c = input("> ")

    if c == "1":
        entry()
    elif c == "2":
        exit_vehicle()
    elif c == "3":
        for row in db.execute(
            "SELECT plate,kind,entry FROM vehicles WHERE exit IS NULL"
        ):
            print(row)
    elif c == "4":
        for row in db.execute(
            "SELECT plate,entry,exit,fee FROM vehicles ORDER BY id DESC"
        ):
            print(row)
    elif c == "0":
        break
    else:
        print("Invalid choice.")

db.close()
