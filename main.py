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

def check_balance():
    #using info find balance and display
    print("Your balance is: $-balance-")

def deposit():
    deposit_amount == 0
    deposit_choice = input("Deposit\nCancel\n")
    if deposit_choice.capitalize() == "Deposit":
        deposit_amount = input("How much money would you like to deposit? ")
        print("You deposited $-amount-. You now have $-moneyleft- in your account.")
        # function to go back to main menu
        print("Go back to main menu.")
    elif deposit_choice.capitalize() == "Cancel":
        # diplay main menu again (while loop prob)
        print("main menu")

def withdraw():
    withdraw_amount == 0
    withdraw_amount = input("How much would you like to withdraw? ")
    # deposit choice function (again from deposit money - reuse code)

def create_account():
    birth_day == 0
    pin_num == 0
    print("Create A New Account")
    name = input("Name: ")
    birth_day = input("Date of Birth: ")
    pin_num = input("PIN: ")
    print(f"New user created. Welcome, {name.capitalize()}.")

def delete_account():
    # delete account
    input("Which account would you like to delete? ")
    print("Deleted")
    
def modify_account():
    # allow edit access & ability to close account, edit name, change pin number, personal identification, etc.
    print("Edit access")


print("""
== == == == == == == == == == == == == == == == == == == == ==\n\n
            Hello There. Welcome to Easy Bank!\n\n
== == == == == == == == == == == == == == == == == == == == ==
""")
account_num = input("Account Number: ")
pin = input("PIN: ")
menu_choice = input("""
1) Menu:\n2) Create Account\n3) Delete Account\n4) Log In\n5) Exit
""")
if menu_choice.capitalize() == "Create Account":
    create_account()
elif menu_choice.capitalize() == "Delete Account":
    delete_account()
elif menu_choice.capitalize() == "Log In":
    print("Log In")
    # using account number find name and display
    print("Welcome -name-!")
    login_choice = input("\n1) Menu:\n2) Check Balance\n3) Deposit Money\n4) Withdraw\n5) Edit Account\n6) Exit\n")
    if login_choice.capitalize() == "Check Balance":
        check_balance()
    elif login_choice.capitalize() == "Deposit Money":
        deposit()
    elif login_choice.capitalize() == "Withdraw":
        withdraw()
    elif login_choice.capitalize() == "Edit Account":
        modify_account()
    elif login_choice.capitalize() == "Exit":
        print("Exit. Bye.")
    else:
        print("Please choose a valid option")
elif menu_choice.capitalize() == 'Exit':
    print("Exit. Goodbye! ")
else:
    print("Please choose an option from the menu")
