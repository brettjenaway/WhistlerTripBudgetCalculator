
#!/usr/bin/env python
# coding: utf-8

## This document is a whistler budget calculator

# Initialise global variables
totalBudget = 0
tripLength = 0
dailyBudget = 0

def budget_input():
    """"
    Prompts the user to enter their trip budget in Canadian Dollars
    Future functionality: USD and other currencies

    Parameters: none

    Returns:
        str: The user's input of budget in dollars

    """
    totalBudget = input("Please enter the total trip budget in CAD$: ")
    return totalBudget

def vacation_length_input():
    """"
    Prompts the user to enter the number of days of their trip

    Parameters: none

    Returns:
        str: The user's input of number of days of the trip

    """
    tripLength = input("Please enter the length of the trip in days: ")
    return tripLength

#Basic main code to run/test each function.
menu_flag = False
dailyBudget = 0

print("Welcome to the Whistler Trip Budget Calculator")
while not menu_flag:
    print()
    totalBudget = budget_input()
    tripLength = vacation_length_input()
    dailyBudget = int(totalBudget) / int(tripLength)
    print("You have $" + totalBudget + " to spend over " + tripLength + " days")
    print("This means you have an average of $" + str(dailyBudget) + " per day for your trip")
    print("Enjoy Whistler!")
