import random
import os
min=1
max=6
choice="yes"
option=["y","yes","Yes"]
print("\t\t\t\t\t\t-----WELCOME TO DICE SIMULATOR-----")
while True:
    print("Dice is rolling....")
    number=random.randint(min,max)
    if number == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    choice=input("\n Do you want to play the game: ")
    if choice not in option:
        print("\t\t\t\t\t\t---- THANKS FOR PLAYING-----")
        break
input("\nPress enter to exit")
