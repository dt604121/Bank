# Testing
import unittest

if __name__ == 'main':
    unittest.main()

import mysql.connector

connection = mysql.connector.connect(user ='root', database = 'example', password = '12345')
connection.autocommit = True

# variables
balance = 0
menu_choice = 0
name = None
pin_num = 0
birth_day = 0
withdraw_amount = 0
deposit_amount = 0
deposit_sum = 0
withdraw_difference = 0
deposit_choice = 0
withdraw_choice = 0
account_num = 0 

def check_balance(balance, account_num, pin_num):
    balance_cursor = connection.cursor()
    find_balance = f"SELECT balance FROM bank WHERE accountnumber = '{account_num}' AND pin = '{pin_num}'"
    balance_cursor.execute(find_balance)
    result = balance_cursor.fetchone()
    if result:
        balance = result[0]
        print(f"Your balance is: ${balance}")
    else:
        print("Invalid account number or PIN.")
    balance_cursor.close()
    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)

def deposit(balance, deposit_amount, deposit_sum, deposit_choice, account_num):
    money_now = 0
    balance = int(balance)
    deposit_amount = int(deposit_amount)
    while deposit_choice < 1 or deposit_choice > 2:
        deposit_choice = int(
            input("1) Deposit\n2) Cancel\n\nPlease choose an option (number 1 or 2): "))
        if deposit_choice == 1:
            deposit_amount = input("How much money would you like to deposit? ")
            deposit_sum = balance + int(deposit_amount)
            money_now = deposit_sum
            print(f"Depositing from Account: {account_num}. You deposited ${deposit_amount}. You now have ${money_now} in your account.")
        elif deposit_choice == 2:
            print("\nOk, canceled")
        else:
            print("Please choose either option 1 or 2.")

def withdraw(balance, withdraw_amount, withdraw_difference, withdraw_choice, account_num):
    money_left = 0
    balance = int(balance)
    withdraw_amount = int(withdraw_amount)
    while withdraw_choice < 1 or withdraw_choice > 2:
        withdraw_choice = int(input("1) Withdraw\n2) Cancel\n\nPlease choose an option (number 1 or 2): "))
        if withdraw_choice == 1:
            withdraw_amount = input("How much money would you like to withdraw? ")
            withdraw_difference = balance - int(withdraw_amount)
            money_left = withdraw_difference
            print(
                f"Withdrawing from Account: {account_num}. You withdrew ${withdraw_amount}. You now have ${money_left} in your account.")
        elif withdraw_choice == 2:
            print("\nOk, canceled")
        else:
            print("Please choose either option 1 or 2.")

def create_account(name, account_num, birth_day, pin_num, balance):
    print("Create A New Account")
    name = str(input("Name: "))
    account_num = int(input("Account Number: "))
    birth_day = input("Date of Birth: ")
    pin_num = int(input("PIN: "))
    balance = int(input("Balance: "))
    mycursor = connection.cursor()
    sql = (f"INSERT INTO bank (name, accountnumber, pin, birthday, balance) VALUES ('{name}', '{account_num}', '{pin_num}', '{birth_day}', '{balance}')")
    mycursor.execute(sql)
    print(f"New user created. Welcome, {name.capitalize()}.\nPIN: {pin_num}\nBirthday: {birth_day}\nBalance: ${balance}")
    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)

def delete_account(account_num):
    # delete account
    delete_cursor = connection.cursor()
    account_num = input("Which account would you like to delete? ")
    sql = f"DELETE FROM bank WHERE accountnumber = '{account_num}' and pin = '{pin_num}'"
    delete_cursor.execute(sql)
    print(f"Account number: {account_num} deleted.")
    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)
    
def modify_account(account_num, pin_num):
    # allow edit access & ability to close account, edit name, change pin number, personal identification, etc.
    modify_cursor = connection.cursor()
    account_num = int(input("Which account would you like to modify? "))
    print("\nEnter your edited information below:\n")
    new_name = str(input("Updated Name: "))
    new_pin_num = int(input("Updated PIN: "))
    sql = f"UPDATE bank SET name = '{new_name}', pin = '{new_pin_num}' WHERE accountnumber = '{account_num}' and pin = '{pin_num}'"
    modify_cursor.execute(sql)
    print(f"\nAccount number: {account_num} has been modified. Your updated name is {new_name.capitalize()}, and your updated PIN is now {new_pin_num}.")
    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)

def repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num):
    menu_choice = 0
    display_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)

def display_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num):
    while menu_choice < 1 or menu_choice > 5:
        menu_choice = int(input(
            """\n~ Home ~\n1) Menu\n2) Create Account\n3) Delete Account\n4) Log In\n5) Exit\n\nPlease choose an option (number 1-5): """))
        if menu_choice == 1:
            menu_choice = 0
            display_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)
        elif menu_choice == 2:
            create_account(name, account_num, birth_day, pin_num, balance)
        elif menu_choice == 3:
            delete_account(account_num)
        elif menu_choice == 4:
            login_cursor = connection.cursor()
            find_name = f"SELECT name FROM bank WHERE accountnumber = '{account_num}' AND pin = '{pin_num}'"
            login_cursor.execute(find_name)
            result = login_cursor.fetchone()
            if result:
                name = result[0]
                print(f"\nWelcome {name.capitalize()}! You are now logged in :).")
                login_choice = int(input(
                    """\n~ Home ~\n1) Menu\n2) Check Balance\n3) Deposit Money\n4) Withdraw\n5) Edit Account\n6) Exit\n\nPlease choose an option (number 1-6): """))
                if login_choice == 1:
                    login_cursor.close()
                    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice,
                                withdraw_amount, withdraw_difference, withdraw_choice, account_num)
                elif login_choice == 2:
                    check_balance(balance, account_num, pin_num)
                    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice,
                                withdraw_amount, withdraw_difference, withdraw_choice, account_num)
                elif login_choice == 3:
                    deposit(balance, deposit_amount, deposit_sum, deposit_choice, account_num)
                    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice,
                                withdraw_amount, withdraw_difference, withdraw_choice, account_num)
                elif login_choice == 4:
                    withdraw(balance, withdraw_amount, withdraw_difference, withdraw_choice, account_num)
                    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice,
                                withdraw_amount, withdraw_difference, withdraw_choice, account_num)
                elif login_choice == 5:
                    modify_account(account_num, pin_num)
                    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice,
                                withdraw_amount, withdraw_difference, withdraw_choice, account_num)
                elif login_choice == 6:
                    print("\nExit log in options. Going back home :)")
                    break
                else:
                    print("Please choose a valid option of 1-6.")
            else:
                print("Invalid account number or PIN.")
        elif menu_choice == 5:
            print("\nExit. Goodbye!\n")
            break
        else:
            print("Please choose an option from the menu 1-5.")
            

# main
print("""
== == == == == == == == == == == == == == == == == == == == ==\n
            Hello There. Welcome to Easy Bank!\n
== == == == == == == == == == == == == == == == == == == == ==
""")
account_num = int(input("Account Number: "))
pin_num = int(input("PIN: "))
display_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)

connection.close()