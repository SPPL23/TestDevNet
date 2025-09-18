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

import tip_calculator

bill_amount = float(input("Enter bill amount: "))
tip_percentage = float(input("Enter tip percentage (0 - 100): "))

tip = bill_amount * (tip_percentage / 100)

tip_calculator.calculate_tip(bill_amount, tip_percentage)

tip_calculator.calculate_total(bill_amount, tip)