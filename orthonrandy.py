from random import randint

attempts = 3

while attempts > 0:
    answer = randint(1, 10)
    myanswer = int(input("Enter number: "))

    if myanswer == answer:
        print(f"The number was {answer} and you guessed it!")
        break
    elif myanswer > 10:
        print("That's not an option!")
    else:
        print(f"The number was {answer}, try again!")
        attempts -= 1
        print(f"Attempts: {attempts}")
        if attempts < 1:
            print("You have run out of attempts!")