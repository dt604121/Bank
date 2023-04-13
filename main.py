# import mysql.connector

# connection = mysql.connector.connect(
#     user ='root', database = 'example', password = '12345')

# cursor = connection.cursor()


# testQuery = ("SELECT * FROM students")

# cursor.execute(testQuery)

# for item in cursor:

#     print(item)

# cursor.close()
# connection.close()

# variables
balance = 0
menu_choice = 0
name = 0

def check_balance(balance):
    #use mysql info to find and pull balance and display
    print(f"Your balance is: ${balance}")

def deposit(balance):
    deposit_amount == 0
    money_left = 0
    while deposit_choice != 1 or deposit_choice != 2:
        deposit_choice = input("1) Deposit\n2) Cancel\n")
        if deposit_choice.capitalize() == "Deposit":
            deposit_amount = input("How much money would you like to deposit? ")
            money_left = deposit_amount - balance 
            print(f"You deposited ${deposit_amount}. You now have ${money_left} in your account.")
        elif deposit_choice.capitalize() == "Cancel":
            print("\nOk, canceled")
        else: 
            print("Please choose either option 1 or 2.")
        display_menu(menu_choice)

def withdraw(balance):
    withdraw_amount == 0
    money_left = 0
    while withdraw_choice != 1 or withdraw_choice != 2:
        withdraw_choice = input("1) Withdraw\n2) Cancel\n")
        if withdraw_choice == 1:
            withdraw_amount = input("How much money would you like to deposit? ")
            money_left = withdraw_amount - balance
            print(
                f"You deposited ${withdraw_amount}. You now have ${money_left} in your account.")
        elif withdraw_choice == 2:
            print("\nOk, canceled")
        else:
            print("Please choose either option 1 or 2.")
        display_menu(menu_choice)

def create_account(name):
    pin_num == 0
    birth_day == 0
    print("Create A New Account")
    name = input("Name: ")
    birth_day = input("Date of Birth: ")
    pin_num = int(input("PIN: "))
    print(f"New user created. Welcome, {name.capitalize()}.")

def delete_account():
    # delete account
    input("Which account would you like to delete? ")
    print("Deleted")
    
def modify_account():
    # allow edit access & ability to close account, edit name, change pin number, personal identification, etc.
    print("Edit access")


def display_menu(menu_choice):
    while menu_choice < 1 or menu_choice > 5:
        menu_choice = int(input(
            """\n~ Home ~\n1) Menu\n2) Create Account\n3) Delete Account\n4) Log In\n5) Exit\n\nPlease choose an option (action or the number): """))
        if menu_choice == 1:
            menu_choice == 0
        elif menu_choice == 2:
            create_account(name)
        elif menu_choice == 3:
            delete_account()
        elif menu_choice == 4:
            print("Log In")
            # using account number find name and display
            print("Welcome -name-!")
            login_choice = int(input(
                """\n~ Home ~\n1) Menu\n2) Check Balance\n3) Deposit Money\n4) Withdraw\n5) Edit Account\n6) Exit\n\nPlease choose an option (action or the number): """))
            if login_choice == 2:
                check_balance(balance)
            elif login_choice == 3:
                deposit(balance)
            elif login_choice == 4:
                withdraw(balance)
            elif login_choice == 5:
                modify_account()
            elif login_choice == 5:
                print("\nExit. Bye.")
            else:
                print("Please choose a valid option of 1-6.")
        elif menu_choice == 5:
            print("\nExit. Goodbye! ")
        else:
            print("Please choose an option from the menu 1-5.")

print("""
== == == == == == == == == == == == == == == == == == == == ==\n
            Hello There. Welcome to Easy Bank!\n
== == == == == == == == == == == == == == == == == == == == ==
""")
account_num = int(input("Account Number: "))
pin = int(input("PIN: "))
display_menu(menu_choice)