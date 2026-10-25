
import sqlite3
from datetime import datetime

db = sqlite3.connect("hospital.db")
db.execute("""
CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")
db.execute("""
CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor TEXT NOT NULL,
    slot TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Booked',
    FOREIGN KEY(patient_id) REFERENCES patients(id),
    UNIQUE(doctor,slot)
)
""")
db.commit()


def register():
    name = input("Patient name: ").strip()
    phone = input("Phone number: ").strip()

    if not name or not phone:
        print("Both fields are required.")
        return

    db.execute(
        "INSERT INTO patients(name,phone) VALUES(?,?)",
        (name, phone)
    )
    db.commit()
    print("Patient ID:", db.execute(
        "SELECT last_insert_rowid()"
    ).fetchone()[0])


def book():
    try:
        pid = int(input("Patient ID: "))
    except ValueError:
        print("Invalid patient ID.")
        return

    if not db.execute(
        "SELECT id FROM patients WHERE id=?", (pid,)
    ).fetchone():
        print("Patient not found.")
        return

    doctor = input("Doctor name: ").strip()
    slot = input("Date and time (YYYY-MM-DD HH:MM): ").strip()

    try:
        datetime.strptime(slot, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date format.")
        return

    try:
        db.execute("""
            INSERT INTO appointments(patient_id,doctor,slot)
            VALUES(?,?,?)
        """, (pid, doctor, slot))
        db.commit()
        print("Appointment booked.")
    except sqlite3.IntegrityError:
        print("Doctor already has an appointment at that time.")


while True:
    print("\n--- HOSPITAL MANAGEMENT ---")
    print("1. Register patient")
    print("2. Book appointment")
    print("3. View patients")
    print("4. View appointments")
    print("5. Cancel appointment")
    print("0. Exit")

    c = input("> ")

    if c == "1":
        register()
    elif c == "2":
        book()
    elif c == "3":
        for p in db.execute("SELECT * FROM patients"):
            print(p)
    elif c == "4":
        for a in db.execute("""
            SELECT appointments.id,patients.name,appointments.doctor,
                   appointments.slot,appointments.status
            FROM appointments JOIN patients
            ON patients.id=appointments.patient_id
            ORDER BY appointments.slot
        """):
            print(a)
    elif c == "5":
        try:
            aid = int(input("Appointment ID: "))
            cur = db.execute("""
                UPDATE appointments SET status='Cancelled'
                WHERE id=? AND status='Booked'
            """, (aid,))
            db.commit()
            print("Cancelled." if cur.rowcount else "Appointment not found.")
        except ValueError:
            print("Invalid ID.")
    elif c == "0":
        break
    else:
        print("Invalid choice.")

db.close()
