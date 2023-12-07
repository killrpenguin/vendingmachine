import os
import numpy as np
balance = "0"
options = np.array([['A1', 'Chips', 5, 1.25], # array key: key, name, inventory amount, cost
                    ['A2', 'Crackers', 7, 2.00],
                    ['A3', 'Cookies', 0, 2.50],
                    ['B1', 'Candys', 10, 1.00],
                    ['B2', 'Pastrys', 3, 2.25],
                    ['B3', 'Pies', 3, 1.75],
                    ['C1', 'Gum Packets', 12, .75],
                    ['C2', 'Mint Tubes', 15, .50]
                    ])


def vending_machine():
    while True:
        os.system('cls')
        print('******** Vending Machine ******')
        print("1: Print Balance \n2: Add to Balance \n3: Display Menu \n4: Make Selection \n5: Exit")
        print('*******************************')
        if balance != '0':
            print(f"\nBalance: ${balance}")
        vend = input("\nWhat would you Like to do?  ")

        if vend == "1" or vend == "print balance":
            os.system('cls')
            print(f"Balance ${balance}")
            x = input("Add money? (Y/N) ")
            if x == 'y' or x == 'Y':
                money_in()
                os.system('cls')
        elif vend == "2" or vend == "add to balance":
            os.system('cls')
            money_in()
        elif vend == "3" or vend == "display menu":
            os.system('cls')
            menu()
        elif vend == "4" or vend == "select item":
            os.system('cls')
            order_item()
        elif vend == "5" or vend == "exit":
            break


def money_in():
    global balance
    add_bal = input("Insert change here: ")
    if add_bal.isdigit():
        a = float(balance) + float(add_bal)
        print(f"Balance: ${a}")
        balance = str(a)
    else:
        print("Enter a number")


def menu():
    os.system('cls')
    for i in options:
        print('We have ' + i[2], i[1])
    a = input('\nWould you like to make a selection? (Y/N) ')
    if a == 'y' or a == 'Y':
        order_item()


def order_item():
    os.system('cls')
    global balance
    for i in options:
        print(i[0] + ':', i[1], '$' + i[3])
    selection = input('\nUsing the left column please make a selection: ')
    for j in options:
        if selection == j[0] and float(balance) >= float(j[3]):
            if int(j[2]) >= 1:
                x = float(balance) - float(j[3])
                os.system('cls')
                print('\nHere are your ' + j[1] + '. \nYour new balance is: $' + str(x))
                balance = x
            else:
                b = input('Sorry, we are out. Would you like to make another selection? (Y/N) ')
                if b == 'Y' or 'y':
                    order_item()
                else:
                    break

        elif float(balance) < float(j[3]):
            a = input('Insufficient funds. Would you like to add to balance? (Y/N) ')
            if a == 'Y' or 'y':
                money_in()
            else:
                break




vending_machine()