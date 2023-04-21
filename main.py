# Testing
import unittest
from unittest.mock import MagicMock
import main

# Test Check Balance
class TestCheckBalance(unittest.TestCase):
    def test_check_balance(self):
        # Create a MagicMock for the cursor
        cursor_mock = MagicMock()
        cursor_mock.fetchone.return_value = (1000,)

        # Set the cursor to the MagicMock
        main.cnx.cursor.return_value = cursor_mock

        # Call the function you want to test
        result = main.check_balance('01234567')

        # Assert that the cursor was called with the correct query
        cursor_mock.execute.assert_called_once_with('SELECT balance FROM accounts WHERE account_number = %s', ('01234567',))

        # Assert that the result is correct
        self.assertEqual(result, 1000)

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
                f"\nWithdrawing from Account: {account_num}. You withdrew ${withdraw_amount}. You now have ${money_left} in your account.")
        elif withdraw_choice == 2:
            print("\nOk, canceled")
        else:
            print("Please choose either option 1 or 2.")

def create_account(name, account_num, birth_day, pin_num, balance):
    print("\nWelcome! Create a new account by entering some basic information below:\n")
    name = str(input("First & Last Name: "))
    account_num = int(input("Account Number: "))
    birth_day = input("Date of Birth: ")
    pin_num = int(input("PIN: "))
    balance = int(input("Balance: "))
    mycursor = connection.cursor()
    sql = (f"INSERT INTO bank (name, accountnumber, pin, birthday, balance) VALUES ('{name}', '{account_num}', '{pin_num}', '{birth_day}', '{balance}')")
    mycursor.execute(sql)
    print(f"\nNew user created. Welcome, {name.title()}.\nHere is your account information:\nAccount Number: {account_num}\nPIN: {pin_num}\nBirthday: {birth_day}\nBalance: ${balance}")

def delete_account(account_num):
    # delete account
    delete_cursor = connection.cursor()
    delete_choice = 0
    while delete_choice < 1 or delete_choice > 2:
        delete_choice = int(input("\nAre you sure you want to delete your account?\n1) Delete Account\n2) Cancel\n\nPlease choose an option (number 1 or 2): "))
        if delete_choice == 1:
            sql = f"DELETE FROM bank WHERE accountnumber = '{account_num}' and pin = '{pin_num}'"
            delete_cursor.execute(sql)
            print(f"Account number: {account_num} deleted.")
        else:
            print("Canceled.")
    
def modify_account(account_num, pin_num):
    # allow edit access & ability to close account, edit name, change pin number, personal identification, etc.
    modify_cursor = connection.cursor()
    print("\nEnter your edited information below:\n")
    new_name = str(input("Updated First & Last Name: "))
    new_pin_num = int(input("Updated PIN: "))
    sql = f"UPDATE bank SET name = '{new_name}', pin = '{new_pin_num}' WHERE accountnumber = '{account_num}' and pin = '{pin_num}'"
    modify_cursor.execute(sql)
    print(f"\nAccount number: {account_num} has been modified. Your updated name is {new_name.title()}, and your updated PIN is now {new_pin_num}.")

def repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num):
    menu_choice = 0
    display_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)

def bank_login(account_num, pin_num, menu_choice):
    log_in = False
    while log_in != True:
        login_cursor = connection.cursor()
        account_num = int(input("Account Number: "))
        pin_num = int(input("PIN: "))
        find_name = f"SELECT name FROM bank WHERE accountnumber = '{account_num}' AND pin = '{pin_num}'"
        login_cursor.execute(find_name)
        result = login_cursor.fetchone()
        if result:
            name = result[0]
            print(f"\nWelcome {name.title()}! You are now logged in :).")
            log_in = True
            login_choice = 0
            while login_choice >= 1 or login_choice <= 8:
                login_choice = int(input("\n ~ Menu ~\n1) Return Home\n2) Check Account Balance\n3) Make A Deposit\n4) Make A Withdrawal\n5) Edit Account\n6) Delete An Account\n7) Create An Account\n8) Exit\n\nPlease choose an option (number 1-8): "))
                if login_choice == 1:
                    login_cursor.close()
                    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)
                elif login_choice == 2:
                    check_balance(balance, account_num, pin_num)
                elif login_choice == 3:
                    deposit(balance, deposit_amount, deposit_sum,
                            deposit_choice, account_num)
                elif login_choice == 4:
                    withdraw(balance, withdraw_amount,
                                withdraw_difference, withdraw_choice, account_num)
                elif login_choice == 5:
                    modify_account(account_num, pin_num)
                elif login_choice == 6:
                    delete_account(account_num)
                elif login_choice == 7:
                    create_account(name, account_num, birth_day, pin_num, balance)
                elif login_choice == 8:
                    print("\nExiting: See you next time :)")
                    menu_choice = 0
                    break
                else:
                    print("Please choose a valid option of 1-8.")
        else:
            print("\nERROR: You have entered an invalid account number or PIN. Please try again.\n")
            log_in = False

def display_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num):
    exit = True
    while menu_choice < 1 or menu_choice > 3 and exit != False:
        menu_choice = int(input("\n  ~ Home Menu ~\n1) Create An Account\n2) Log In\n3) Exit\n\nPlease choose an option (number 1-3): "))
        display_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)
        if menu_choice == 1:
            create_account(name, account_num, birth_day, pin_num, balance)
            repeat_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice,
                        withdraw_amount, withdraw_difference, withdraw_choice, account_num)
        elif menu_choice == 2:
            bank_login(account_num, pin_num, menu_choice)
        elif menu_choice == 3:
            exit = False
            print("\nExiting: Goodbye!\n")
            break
        else:
            print("Please choose an option from the menu 1-3.")

# main
print("""
== == == == == == == == == == == == == == == == == == == == ==\n
            Hello There. Welcome to Easy Bank!\n
== == == == == == == == == == == == == == == == == == == == ==
""")

display_menu(menu_choice, name, balance, deposit_amount, deposit_sum, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice, account_num)

connection.close()