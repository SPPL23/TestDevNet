myTasks = ["Wakeup", "Eat", "Drink", "Commute", "Work", "Relax", "Sleep"]
print(myTasks)

while True:
    try:
        init = input("Add task? [Y/N]: ")
        if init == "Y" or init == "y":

            taskPosition = int(input("Enter index position: "))
            newTask = input("Enter new task: ")

            myTasks.insert(taskPosition, newTask)
            print(myTasks)
            continue
        elif init == "N" or init == "n":
            print("Skipping Task")

    except ValueError:
        print("Error")
        continue

    try:
        rmit = input("Remove task? [Y/N]")
        if rmit == "Y" or rmit == "y":
            
            rmTask = int(input("Remove Task based on index position: "))

            myTasks.pop(rmTask)
            print(myTasks)
            continue
        elif rmit == "N" or rmit == "n":
            print("Skipping Task")

    except ValueError:
        print("Error")
        continue
    
    try:
        comp = input("Mark the task list if completed completed? [Y/N]: ")

        if comp == "Y" or comp == "y":
            myTasks.append("-Completed")
            print(myTasks)
        elif comp == "N" or comp == "n":
            print("Rerunning Task Assortment")
            continue
        else:
            print("Invalid input")
            continue
    except ValueError:
        print("Error")

    try:
        enum = input("Enumrate Tasks? [Y/N](Y, will end the program): ")

        if enum == "Y" or enum == "y":
            for myTasks in enumerate(myTasks):
                print(myTasks)
            break
        elif enum == "N" or enum == "n":
            print("Cancelling myTasks enumeration")
        else:
            print("Error")
            continue
    except ValueError:
        print("Error")

    try:
        myClear = input("Clear the whole list? [Y/N]: ")

        if myClear == "Y" or myClear == "y":
            myTasks.clear()
            print(myTasks)
            break
        elif myClear == "N" or myClear == "n":
            print("Cancelling clearing of list")
            continue
        else:
            print("Error")
            continue
    except ValueError:
        print("Error")
        continue