name = str(input("Enter full name: "))
section = input("Enter Section: ")
grade = float(input("Enter Grades: "))

if grade >= 97 and grade < 101:
    print(f"{name} of section {section}. You are a Summa Cum Laude")
elif grade >= 94 and grade < 97:
    print(f"{name} of section {section}. You are a Magna Cum Laude")
elif grade >= 91 and grade < 94:
    print(f"{name} of section {section}. You are a Cum Laude")
elif grade >= 75 and grade < 91:
    print(f"{name} of section {section}. Graduate lang")
else:
    print(f"{name} of section {section}. You are Summa Langit")