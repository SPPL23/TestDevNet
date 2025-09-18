
#IF function

def ifcalc(fN, sN, op):
    
    print("This function was made using if statements")

    if op == '+' or op == "Addition" or op == "Add":
        sum = fN + sN
        print("If sum: ", sum)
    elif op == '-' or op == "Subtraction"  or op == "Minus":
        difference = fN - sN
        print("If difference: ", difference)
    elif op == '*' or op == "Multiplication"  or op == "Times":
        product = fN * sN
        print("If product:", product)
    elif op == '/' or op == "Division"  or op == "Divide":
        quotient = fN / sN
        print("If quotient", quotient)
    else:
        print("Invalid")

    return(fN, sN, op)

