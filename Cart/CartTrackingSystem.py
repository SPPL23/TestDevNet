def cart_Ops(username):
    try:
        with open(f'cart_{username}.txt', 'a+') as reads:
            reads.seek(0)
            content = reads.read()
    except FileNotFoundError:
        content = ""
    
    menu = ["CART MENU", "1. View Carts", "2. Add Carts", "3. Remove Cart", "4. Exit"]
    for options in menu:
        print(options)
    option = int(input("Enter Option in Menu: "))

    while option == 1:
        print("CART CONTENTS:")
        if content:
            print(content)
        else:
            print("Your cart is empty.")
        cart_Ops(username)
        break

    while option == 2:
        newCart = input("Enter new cart name: ")
        with open(f'cart_{username}.txt', 'a+') as add:
            add.write(f"{newCart}\n")
        print("Cart added.")
        cart_Ops(username)
        break

    while option == 3:
        remove_cart = input("Enter the name of the cart to remove: ")
        with open(f'cart_{username}.txt', 'r') as carts:
            lines = carts.readlines()
        
        with open(f'cart_{username}.txt', 'w') as carts:
            for line in lines:
                if line.strip() != remove_cart:
                    carts.write(line)
                else:
                    print(f"Cart '{remove_cart}' removed.")
        cart_Ops(username)
        break

    while option == 4:
        print("Exiting Cart Menu...")
        return

def create_user():
    choice = input("[L]ogin or [R]egister: ")

    while choice == "L" or choice == "l":
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            with open('user.txt', 'r') as users:
                content = users.read()
                user_found = False
                for line in content.splitlines():
                    stored_username, stored_password = line.split(',')
                    if stored_username == username and stored_password == password:
                        user_found = True
                        print("Login Successful")
                        cart_Ops(username)
                        break
                if not user_found:
                    print("Login Failed: Invalid username or password")
                    create_user()
        except FileNotFoundError:
            print("No users registered yet.")
            create_user()
        break

    while choice == "R" or choice == "r":
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            with open('user.txt', 'a') as users:
                users.write(f"{username},{password}\n")
                print("Registration Successful")
                cart_Ops(username)
                break
        except Exception as e:
            print(f"Error during registration: {e}")
            break

create_user()
