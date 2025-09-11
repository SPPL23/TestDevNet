def calc():
    fN = input("Enter first num: ")
    sN = input("Enter second num: ")
    op = input("Enter operator [+, -, *, /]")

    match calc:
        case '+':
            print(op = fN + sN)
        case '-':
            print(op = fN - sN)
        case '*':
            print(op = fN * sN)
        case '/':
            print(op = fN / sN)
    return

def sample():
    x = int(input("Enter [1 or 2]: "))

    while True:
        try:
            if x == 1:
                print("True")
                calc()
                break
            elif x == 2:
                print("False")
                break
            else:
                sample()
                break
        except ValueError:
            print("Invalid Input")
            break

sample()