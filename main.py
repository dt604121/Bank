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
name = None
pin_num = 0
birth_day = 0
withdraw_amount = 0
deposit_amount = 0
deposit_difference = 0
withdraw_difference = 0
deposit_choice = 0
withdraw_choice = 0

def check_balance(balance):
    #use mysql info to find and pull balance and display
    print(f"Your balance is: ${balance}")
    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)

def deposit(balance, deposit_amount, deposit_difference, deposit_choice):
    money_left = 0
    balance = int(balance)
    while deposit_choice < 1 or deposit_choice > 2:
        deposit_choice = int(
            input("1) Deposit\n2) Cancel\n\nPlease choose an option (number 1 or 2): "))
        if deposit_choice == 1:
            deposit_amount = input(
                "How much money would you like to withdraw? ")
            deposit_difference = balance - int(deposit_amount)
            money_left = deposit_difference
            print(
                f"You deposited ${deposit_amount}. You now have ${money_left} in your account.")
        elif deposit_choice == 2:
            print("\nOk, canceled")
        else:
            print("Please choose either option 1 or 2.")

def withdraw(balance, withdraw_amount, withdraw_difference, withdraw_choice):
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
                f"You deposited ${withdraw_amount}. You now have ${money_left} in your account.")
        elif withdraw_choice == 2:
            print("\nOk, canceled")
        else:
            print("Please choose either option 1 or 2.")

def create_account(name, birth_day, pin_num):
    print("Create A New Account")
    name = str(input("Name: "))
    birth_day = input("Date of Birth: ")
    pin_num = int(input("PIN: "))
    print(f"New user created. Welcome, {name.capitalize()}.\nPIN: {pin_num}\nBirthday: {birth_day}")
    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)

def delete_account():
    # delete account
    input("Which account would you like to delete? ")
    print("Deleted")
    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)
    
def modify_account():
    # allow edit access & ability to close account, edit name, change pin number, personal identification, etc.
    print("Edit access")
    repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)


def repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice):
    menu_choice = 0
    display_menu(menu_choice, name, balance, deposit_amount, deposit_difference,
                 deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)

def display_menu(menu_choice, name, balance, deposit_amount, deposit_difference, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice):
    name = input("Name: ")
    while menu_choice < 1 or menu_choice > 5:
        menu_choice = int(input(
            """\n~ Home ~\n1) Menu\n2) Create Account\n3) Delete Account\n4) Log In\n5) Exit\n\nPlease choose an option (number 1-5): """))
        if menu_choice == 1:
            menu_choice = 0
            display_menu(menu_choice, name, balance, deposit_amount, deposit_difference, withdraw_amount, withdraw_difference)
        elif menu_choice == 2:
            create_account(name, birth_day, pin_num)
        elif menu_choice == 3:
            delete_account()
        elif menu_choice == 4:
            # using account number find name and display
            print(f"\nWelcome {name.capitalize()}! You are now logged in :).")
            login_choice = int(input(
                """\n~ Home ~\n1) Menu\n2) Check Balance\n3) Deposit Money\n4) Withdraw\n5) Edit Account\n6) Exit\n\nPlease choose an option (number 1-6): """))
            if login_choice == 1:
                repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)
            elif login_choice == 2:
                check_balance(balance)
                repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference,
                            deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)
            elif login_choice == 3:
                deposit(balance, deposit_amount, deposit_difference, deposit_choice)
                repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference,
                            deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)
            elif login_choice == 4:
                withdraw(balance, withdraw_amount, withdraw_difference, withdraw_choice)
                repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference,
                            deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)
            elif login_choice == 5:
                modify_account()
                repeat_menu(menu_choice, name, balance, deposit_amount, deposit_difference,
                            deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)
            elif login_choice == 6:
                print("\nExit. Bye.")
                break
            else:
                print("Please choose a valid option of 1-6.")
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
pin = int(input("PIN: "))
display_menu(menu_choice, name, balance, deposit_amount, deposit_difference, deposit_choice, withdraw_amount, withdraw_difference, withdraw_choice)
