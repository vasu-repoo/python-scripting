products = {
    "Apple": 20,
    "Banana": 10,
    "Milk": 30,
    "Bread": 40,
    "Chocolate": 50
}

cart = {}

while True:
    print("\n===== SHOPPING CART =====")
    print("1. View Products")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Remove Item")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Products:")
        for item, price in products.items():
            print(f"{item} - Rs. {price}")

    elif choice == "2":
        item = input("Enter product name: ").title()

        if item in products:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                cart[item] = cart.get(item, 0) + quantity
                print(item, "added to cart!")
            else:
                print("Quantity must be greater than zero.")
        else:
            print("Product not found!")

    elif choice == "3":
        print("\nYour Shopping Cart:")
        total = 0

        if not cart:
            print("Cart is empty.")
        else:
            for item, quantity in cart.items():
                price = products[item] * quantity
                print(f"{item} x {quantity} = Rs. {price}")
                total += price

            print("Total Amount: Rs.", total)

    elif choice == "4":
        item = input("Enter product name to remove: ").title()

        if item in cart:
            del cart[item]
            print(item, "removed from cart.")
        else:
            print("Item not found in cart.")

    elif choice == "5":
        total = sum(
            products[item] * quantity
            for item, quantity in cart.items()
        )

        print("\n===== BILL =====")
        for item, quantity in cart.items():
            print(f"{item} x {quantity} = Rs. {products[item] * quantity}")

        print("Grand Total: Rs.", total)
        print("Thank you for shopping!")
        cart.clear()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")