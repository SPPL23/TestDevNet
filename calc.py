
#Match functio
# 
# 

def matchcalc():

    print("This function was made using match case")

    fN = int(input("Enter first num: "))
    sN = int(input("Enter second num: "))
    op = input("Enter operator [+, -, *, /]")

    match op:
        case '+':
            msum = fN + sN
            print("Match sum: ", msum)
        case '-':
            mdifference = fN - sN
            print("Match difference: ", mdifference)
        case '*':
            mproduct = fN * sN
            print("Match product: ", mproduct)
        case '/':
            mquotient = fN / sN
            print("Match quotient", mquotient)
    return(fN, sN, op)

#Prevents the function from automatically running within the main file
if __name__ == "__main__":
    print("calcModule")
