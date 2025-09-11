#Dictionary
OpDict = {
    "Arithmetic": "+, -, *, /, %",
    "Assignment": "=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=",
    "Comparison": "==, !=, >, <, >=, <=",
    "Logical": "and, or, not"
}
print("Arithmetic Operators: ")
print(OpDict["Arithmetic"], "\n")
print("Assignment Operators: ")
print(OpDict["Assignment"], "\n")
print("Comparison Operators: ")
print(OpDict["Comparison"], "\n")
print("Logical Operators: ")
print(OpDict["Logical"], "\n")

#Arithmetic Operators
x = 1;
y = 2;

sum = x + y
difference = x - y
product =  x * y
quotient = x / y
modulus = x % y

print("Arithmetic Operators\n")
print("The sum of", x, "and", y, " is equal to ", + sum)
print("The difference of", x, "and", y, " is equal to ", + difference)
print("The product of", x, "and", y, " is equal to ", + product)
print("The quotient of", x, "and", y, " is equal to ", + quotient)
print("The remainder of", x, "and", y, " is equal to ", + modulus)
print("")

#Assignment Operators
print("Assignment Operators: \n")
fNum = (int(input("Enter first number: \n")))
sNum = (int(input("Enter second number: \n")))
print("")

if fNum > sNum:
    print(f"{fNum} is greater than {sNum}\n")
if fNum < sNum:
    print(f"{fNum} is less than {sNum}\n")
if fNum == sNum:
    print(f"{fNum} is equal to {sNum}\n")
if fNum != sNum:
    print(f"{fNum} is not equal to {sNum}\n")

a = 5
a += 1

b = 5
b -= 1

c = 5
c *= 1

d = 5
d /= 1

e = 5
e %= 2

print(f"{a} += 1 is ", a)
print(f"{b} -= 1 is ", b)
print(f"{c} *= 1 is ", c)
print(f"{d} /= 1 is ", d)
print(f"{e} %= 2 is ", e, "\n")

#Comparison and Logical Operators
print("Comparison and Logical Operators: \n")
print("Let g = 1 and h = 1")
g = 1
h = 1

print("g == h is ", g == h)
print("g > h is ",g > h)
print("g < h is ", g < h)
print("g != is ", g != h)
print("g >= is ", g >= h)
print("g <= is ", g <= h, "\n")
print("Let i = True and j = False")

i = "True"
j = "False"

print("i and j is ", i and j)
print("i or k is ", i or j)
print(not(i and j))

