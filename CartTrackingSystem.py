def cart_Ops(username):
    with open(f'cart_{username}.txt', 'a+') as reads:
        reads.read()
    menu = ["CART MENU", "1. View Carts", "2. Add Carts", "3. Exit"]
    for options in menu:
        print(options)
    option = int(input("Enter Option in Menu: "))

    while option == 1:
        try:
            with open(f'cart_{username}.txt', 'r') as carts:
                carts.seek(0)
                print(carts.read())
                cart_Ops(username)
                break
        except ValueError:
            print("Error within input")

    while option == 2:
        try:
            with open(f'cart_{username}.txt', 'a+') as add:
                add.read()
                add.tell()
                add.seek(add.tell())
                newCart = input("Enter new cart name: ")
                add.write(f"{newCart}\n")
            break
        except FileNotFoundError:
            print("File does not exists creating new files")
            with open(f'cart_{username}.txt', 'w') as create:
                newCart = input("Enter new cart name: ")
                create.write(f"{newCart}\n")
                cart_Ops(username)
            break
    
    while option == 3:
        print("Exiting Program")
        break

#Needs Debugging
def create_user():
    choice = input("[L]ogin or [R]egister: ")

    while choice == "L" or choice == "l":
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")

            with open(f'{username}.txt', 'r') as users:
                content = users.read()
                lines = content.split(":")

                if username in lines and password in lines:
                    print("Login Successful")
                    cart_Ops(username)
                    break
                else:
                    print("Login Failed")
                    create_user()
                    break
        except FileNotFoundError:
            print("Does not exist")
            create_user()
            break
        break

    while choice == "R" or choice == "r":
            try:
                username = input("Enter username: ")
                password = input("Enter password: ")
                with open(f'{username}.txt', 'w') as users:
                    users.write(f"{username}:{password}")
                    print("Registration Successful")
                break
            except ValueError:
                print("Error within input")
                break
            
create_user()