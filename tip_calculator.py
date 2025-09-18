"""
Create a module called tip_calculator.py that contains two functions:
calculate_tip(bill_amount, tip_percentage): This function should calculate the tip amount based on the given bill amount and tip percentage.
calculate_total(bill_amount, tip): This function should calculate the total bill including the tip.
In the main.py file:
Import the tip_calculator module.
Ask the user for the total bill amount and the tip percentage.
Call the calculate_tip function to compute the tip and the calculate_total function to compute the total bill (bill + tip).
Display the calculated tip and the total amount (including tip).
"""

#calculate_tip

def calculate_tip(bill_amount, tip_percentage):

    while bill_amount > 0:
        try:
            tip = bill_amount * (tip_percentage / 100)
            if tip_percentage == 0:
                print("Your bill is ", bill_amount, "tips were not provided")
                break
            elif tip_percentage > 100:
                print("You cannot enter a tip greater than 100%")
                break
            else:
                print(f"Your tip of {tip_percentage}% will be in addition of {bill_amount} + ", tip, "\n")
                break
        except ValueError:
            print("Enter valid amount")
            continue

if __name__ == "__main__":
    print("")

#calculate_total

def calculate_total(bill_amount, tip):
    print("You will be paying a total of ", bill_amount + tip)

if __name__ == "__main__":
    print("")