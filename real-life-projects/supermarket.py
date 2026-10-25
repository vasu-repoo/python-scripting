import sqlite3

con = sqlite3.connect("supermarket.db")
con.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    price REAL CHECK(price >= 0),
    stock INTEGER CHECK(stock >= 0)
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total REAL,
    date TEXT DEFAULT CURRENT_TIMESTAMP
)
""")
con.commit()


def add_product():
    name = input("Product name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        if price < 0 or stock < 0:
            print("Invalid price or stock.")
            return

        con.execute(
            "INSERT INTO products(name,price,stock) VALUES(?,?,?)",
            (name, price, stock)
        )
        con.commit()
        print("Product saved.")
    except (ValueError, sqlite3.IntegrityError):
        print("Invalid details or product already exists.")


def show_products():
    for p in con.execute("SELECT * FROM products"):
        print(f"{p[0]} | {p[1]} | Rs.{p[2]:.2f} | Stock: {p[3]}")


def checkout():
    cart = {}
    while True:
        show_products()
        choice = input("Product ID (0 to checkout): ")
        if choice == "0":
            break

        try:
            pid = int(choice)
            qty = int(input("Quantity: "))
            p = con.execute(
                "SELECT * FROM products WHERE id=?", (pid,)
            ).fetchone()

            if not p or qty <= 0:
                print("Invalid product or quantity.")
            elif cart.get(pid, 0) + qty > p[3]:
                print("Not enough stock.")
            else:
                cart[pid] = cart.get(pid, 0) + qty
        except ValueError:
            print("Enter valid numbers.")

    if not cart:
        print("Cart is empty.")
        return

    try:
        con.execute("BEGIN")
        total = 0

        for pid, qty in cart.items():
            p = con.execute(
                "SELECT * FROM products WHERE id=?", (pid,)
            ).fetchone()
            total += p[2] * qty

        discount = float(input("Discount amount: "))
        if discount < 0 or discount > total:
            raise ValueError("Invalid discount")

        total -= discount

        for pid, qty in cart.items():
            cur = con.execute(
                "UPDATE products SET stock=stock-? "
                "WHERE id=? AND stock>=?",
                (qty, pid, qty)
            )
            if cur.rowcount != 1:
                raise ValueError("Stock changed. Try again.")

        con.execute("INSERT INTO sales(total) VALUES(?)", (total,))
        con.commit()
        print(f"TOTAL BILL: Rs.{total:.2f}")

    except (ValueError, sqlite3.Error) as e:
        con.rollback()
        print("Checkout failed:", e)


while True:
    print("\n--- SUPERMARKET ---")
    print("1. Add product")
    print("2. View products")
    print("3. Checkout")
    print("4. Sales history")
    print("0. Exit")

    choice = input("> ")

    if choice == "1":
        add_product()
    elif choice == "2":
        show_products()
    elif choice == "3":
        checkout()
    elif choice == "4":
        for s in con.execute("SELECT * FROM sales ORDER BY id DESC"):
            print(s)
    elif choice == "0":
        break
    else:
        print("Invalid choice.")

con.close()