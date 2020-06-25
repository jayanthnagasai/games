print()
print("Welcome to Jay's Roll-A-Dice!")

import random

def RollDice(rolls):
    for i in range(0, rolls):
        number = random.randint(1, 6)
        print(str(number))
    Menu()

def Menu():
    print()
    print("1. Roll a dice")
    print("2. Roll multiple dice")
    print("3. Exit the program")
    print()
    choice = int(input("Enter here:"))

    if (choice == 1):
        RollDice(1)
    if (choice == 2):
        rolls = int(input("How many rolls:  "))
        RollDice(rolls)
    if (choice == 3):
        exit()

Menu()


