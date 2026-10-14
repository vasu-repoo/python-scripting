print("""
*************************
    COMPOUND iNTEREST
*************************
""")


while True:
    print("ENTER EXT to exit")

    p_i = input("Enter principal amount : ")

    if p_i == "EXT":
        print("Program closed THANKS.")
        break
    
    p = float(p_i)

    if p < 0:
        print("Negative value not allowed. Try again.")
        continue

    r_i = input("Enter interest rate: ")

    if r_i == "EXT":
        print("Program closed THANKS.")
        break

    r = float(r_i)

    if r < 0:
        print("Negative value not allowed. Start again.")
        continue

    t_i = input("Enter time in years: ")

    if t_i == "EXT":
        print("Program closed THANKS.")
        break
    
    t = float(t_i)

    if t < 0:
        print("Negative value not allowed. Start again.")
        continue

    amount = p * (1 + r / 100) ** t
    ci = amount - p

    print("Final Amount:", amount)
    print("Compound Interest:", ci)
