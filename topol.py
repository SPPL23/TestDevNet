"""
currency = (50, 1, 45)

print("Currency:", currency)

print("for:[")
for i in currency:
    print(i)
print("]")

(PHP, USD, CAD) = currency

print("Unpacked:[")
print(USD)
print(PHP)
print(CAD)
print("]")

droga = ("shabu", "Neozep", "marijuana", "lsd", "meth")
tao = ("Polis", "Pushir", "Bisakol", "Tangalog", "Intcheck")

(hard, *bet, _, biogesic) = droga

print("droga:")
print(bet)
print(biogesic)
print(droga.count("marijuana"))
print(droga.index("lsd"))
print(droga + tao)
"""


#print(motor, quantity, price) #('PCX', 5, '220k') ('NMAX', 10, '110k') ('XMAX', 50, '330k')

#print(motor) #('PCX', 5, '220k')

#print(items) #output: [('PCX', 5, '220k'), ('NMAX', 10, '110k'), ('XMAX', 50, '330k')]

#for i in items:
#    print(i)
    #output: ('PCX', 5, '220k')
    #        ('NMAX', 10, '110k')
    #        ('XMAX', 50, '330k')

column = ["Motor", "Quantity", "Price"]
items = [
    ("PCX", 5, 220000),
    ("NMAX", 10, 110000),
    ("XMAX", 50, 330000)
    ]

(c1, c2, c3) = items
(model, quantity, price) = c1
(model2, quantity2, price2) = c2
(model3, quantity3, price3) = c3    

print(f"={column[0]:=^25}{column[1]:=^25}{column[2]:=^25}")
print(f"{model:^25} {quantity:^25} {price:^25}")
print(f"{model2:^25} {quantity2:^25} {price2:^25}")
print(f"{model3:^25} {quantity3:^25} {price3:^25}")

question = input("Would you like to purchase? [Y/N]")

while question == "Y" or question == "y":
    try:
        c_model = input("Enter motor model: ")
        a_quantity = int(input("Enter quantity: "))
        coh = float(input("Enter payment: "))
        match c_model:
            case "PCX":
                print(f"Your change for {c_model} is {coh - (a_quantity * price)}")
                print(f"={column[0]:=^25}{column[1]:=^25}{column[2]:=^25}")
                print(f"{model:^25} {quantity - a_quantity:^25} {price:^25}")
                print(f"{model2:^25} {quantity2:^25} {price2:^25}")
                print(f"{model3:^25} {quantity3:^25} {price3:^25}")
            case "NMAX":
                print(f"Your change for {c_model} is {coh - (a_quantity * price2)}")
                print(f"={column[0]:=^25}{column[1]:=^25}{column[2]:=^25}")
                print(f"{model:^25} {quantity:^25} {price:^25}")
                print(f"{model2:^25} {quantity2 - a_quantity:^25} {price2:^25}")
                print(f"{model3:^25} {quantity3:^25} {price3:^25}")
            case "XMAX":
                print(f"Your change for {c_model} is {coh - (a_quantity * price3)}")
                print(f"={column[0]:=^25}{column[1]:=^25}{column[2]:=^25}")
                print(f"{model:^25} {quantity:^25} {price:^25}")
                print(f"{model2:^25} {quantity2:^25} {price2:^25}")
                print(f"{model3:^25} {quantity3 - a_quantity:^25} {price3:^25}")
            case _:
                print("error")
        break

    except ValueError:
        print("Error")
        break

while question == "N" or question == "n":
    try:
        print("Closing Menu")
        break
    except ValueError:
        break

