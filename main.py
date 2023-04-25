# Testing
import sys
import mysql.connector
import time

connection = mysql.connector.connect(user ='root', database = 'example', password = '12345')
connection.autocommit = True

# variables
balance = 0
menu_choice = 0
name = None
pin_num = 0
birth_day = 0
withdraw_amount = None
deposit_amount = None
withdraw_choice = 0
account_num = 0

def check_balance(account_num, pin_num):
    try: 
        balance_cursor = connection.cursor()
        find_balance = f"SELECT balance FROM bank WHERE accountnumber = '{account_num}' AND pin = '{pin_num}'"
        balance_cursor.execute(find_balance)
        result = balance_cursor.fetchone()
        if result:
            balance = result[0]
            print(f"\nYour current balance is: ${balance:.2f}")
            time.sleep(1)
        else:
            print("Invalid account number or PIN.")
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        balance_cursor.close()

def deposit(deposit_amount, account_num, pin_num):
    deposit_choice = 0
    valid_deposit = None
    while deposit_choice < 1 or deposit_choice > 2 or valid_deposit == False:
        deposit_choice = int(input("1) Deposit\n2) Cancel\n\nPlease enter option 1 or 2: "))
        if deposit_choice == 1:
            deposit_cursor = connection.cursor()
            balance = f"SELECT balance FROM bank WHERE accountnumber = '{account_num}' AND pin = '{pin_num}'"
            deposit_cursor.execute(balance)
            result = deposit_cursor.fetchone()
            if result is None:
                print("Invalid account number or pin.")
                return
            deposit_amount = float(input("\nHow much money would you like to deposit into your account? "))
            if deposit_amount != 0:
                current_balance = int(result[0])
                new_balance = current_balance + deposit_amount
                deposit_cursor.execute(f"UPDATE bank SET balance = '{new_balance}' WHERE accountnumber = '{account_num}' and pin = '{pin_num}'")
                connection.commit()
                print(f"\nYour deposit of ${deposit_amount:.2f} was successful. The new balance is: ${new_balance:.2f}")
                time.sleep(1)
                deposit_cursor.close()
                valid_deposit = True
            else: 
                print(f"\nInvalid Amount: Please choose an amount greater than $0.")
                valid_deposit = False
        elif deposit_choice == 2:
            print("\nDeposit canceled.")
            break
        else:
            print("\nInvalid Choice: please choose either 1 or 2.")

def withdraw(withdraw_amount, withdraw_choice, account_num, pin_num):
    withdraw_choice = 0
    valid_withdrawal = False
    while withdraw_choice < 1 or withdraw_choice > 2 or valid_withdrawal == False:
        withdraw_choice = int(input("1) Withdraw\n2) Cancel\n\nPlease enter option 1 or 2: "))
        if withdraw_choice == 1:
            withdraw_cursor = connection.cursor()
            balance = f"SELECT balance FROM bank WHERE accountnumber = '{account_num}' AND pin = '{pin_num}'"
            withdraw_cursor.execute(balance)
            result = withdraw_cursor.fetchone()
            if result is None:
                print("Invalid account number or pin.")
                return
            withdraw_amount = float(input("\nHow much money would you like to withdraw from your account? "))
            current_balance = int(result[0])
            if withdraw_amount == 0:
                print(f"\nPlease choose an amount greater than $0.")
                valid_withdrawal = False
            elif withdraw_amount > current_balance:
                print(f"\nSorry, you don't have ${withdraw_amount:.2f} in your account. You can only withdraw up to your current balance of ${current_balance:.2f}.\n")
                valid_withdrawal = False
            else: 
                new_balance = current_balance - withdraw_amount
                withdraw_cursor.execute(f"UPDATE bank SET balance = '{new_balance}' WHERE accountnumber = '{account_num}' and pin = '{pin_num}'")
                connection.commit()
                print(f"\nYour withdrawal of ${withdraw_amount:.2f} was successful. The new balance is: ${new_balance:.2f}")
                time.sleep(1)
                withdraw_cursor.close()
                valid_withdrawal = True
        elif withdraw_choice == 2:
            print("\nWithdrawal canceled.")
            break
        else:
            print("\nInvalid Choice: please choose either 1 or 2.")

def create_account(name, account_num, birth_day, pin_num):
    print("\nWelcome! Create a new account by entering some basic information below:\n")
    name = str(input("First & Last Name: "))
    account_num = int(input("Account Number: "))
    birth_day = input("Date of Birth: ")
    pin_num = int(input("PIN: "))
    balance = float(input("Balance: "))
    mycursor = connection.cursor()
    sql = (f"INSERT INTO bank (name, accountnumber, pin, birthday, balance) VALUES ('{name}', '{account_num}', '{pin_num}', '{birth_day}', '{balance}')")
    mycursor.execute(sql)
    print(f"\nNew user created. Welcome, {name.title()}.\n\nHere is your account information:\nAccount Number: {account_num}\nPIN: {pin_num}\nBirthday: {birth_day}\nBalance: ${balance:.2f}")
    time.sleep(1)
    mycursor.close()

def delete_account(account_num, pin_num, name):
    # delete account
    delete_cursor = connection.cursor()
    delete_choice = 0
    while delete_choice < 1 or delete_choice > 2:
        delete_choice = int(input("\nAre you sure you want to delete your account?\n1) Delete Account\n2) Cancel\n\nPlease choose an option (number 1 or 2): "))
        if delete_choice == 1:
            sql = f"DELETE FROM bank WHERE accountnumber = '{account_num}' and pin = '{pin_num}'"
            delete_cursor.execute(sql)
            print(f"Account number {account_num} deleted. Goodbye, {name.title()}.")
            time.sleep(1)
            repeat_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num)
        else:
            print("\nCanceled.")
    
def modify_account(account_num, pin_num):
    # allow edit access & ability to close account, edit name, change pin number, personal identification, etc.
    modify_cursor = connection.cursor()
    print("\nEnter your edited information below:\n")
    new_name = str(input("Updated First & Last Name: "))
    new_pin_num = int(input("Updated PIN: "))
    sql = f"UPDATE bank SET name = '{new_name}', pin = '{new_pin_num}' WHERE accountnumber = '{account_num}' and pin = '{pin_num}'"
    modify_cursor.execute(sql)
    print(f"\nAccount number {account_num} has been modified. Your updated name is {new_name.title()}, and your new PIN is now {new_pin_num}.")
    time.sleep(1)

def repeat_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num):
    menu_choice = 0
    display_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num)

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
            time.sleep(1)
            log_in = True
            login_choice = 0
            while login_choice < 1 or login_choice > 8:
                login_choice = int(input("\n ~ Menu ~\n1) Return Home\n2) Check Account Balance\n3) Make A Deposit\n4) Make A Withdrawal\n5) Edit Account\n6) Close Your Account\n7) Create An Account\n8) Exit\n\nPlease choose an option (number 1-8): "))
                if login_choice == 1:
                    login_cursor.close()
                    repeat_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num)
                elif login_choice == 2:
                    check_balance(account_num, pin_num)
                    login_choice = 0
                elif login_choice == 3:
                    deposit(deposit_amount, account_num, pin_num)
                    login_choice = 0
                elif login_choice == 4:
                    withdraw(withdraw_amount, withdraw_choice, account_num, pin_num)
                    login_choice = 0
                elif login_choice == 5:
                    modify_account(account_num, pin_num)
                    login_choice = 0
                elif login_choice == 6:
                    delete_account(account_num, pin_num, name)
                    login_choice = 0
                elif login_choice == 7:
                    create_account(name, account_num, birth_day, pin_num)
                    login_choice = 0
                elif login_choice == 8:
                    print("\nExiting: See you next time :)")
                    sys.exit()
                else:
                    print("Please choose a valid option of 1-8.")
        else:
            print("\nERROR: You have entered an invalid account number or PIN. Please try again.\n")
            log_in = False

def display_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num):
    while menu_choice < 1 or menu_choice > 3:
        menu_choice = int(input("\n  ~ Home Menu ~\n1) Create An Account\n2) Log In\n3) Exit\n\nPlease choose an option (number 1-3): "))
        display_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num)
        if menu_choice == 1:
            create_account(name, account_num, birth_day, pin_num)
            repeat_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num)
        elif menu_choice == 2:
            bank_login(account_num, pin_num, menu_choice)
        elif menu_choice == 3:
            print("\nExiting: Goodbye!\n")
            sys.exit()
        else:
            print("Please choose a VALID option from the menu 1-3.")
        break

# main
print("""
== == == == == == == == == == == == == == == == == == == == ==\n
            Hello There. Welcome to Easy Bank!\n
== == == == == == == == == == == == == == == == == == == == ==
""")

display_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num)

connection.close()