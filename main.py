print("Hello There! Welcome to Easy Bank :)")
account_num = input("Account Number: ")
pin = input("PIN: ")
menu_choice = input("\nMenu:\nCreate Account\nLog In\nExit\n")
if menu_choice.capitalize() == "Create Account":
    print("Create A New Account")
    name = input("Name: ")
    birth_day = input("Date of Birth: ")
    pin_num = input("PIN: ")
    print(f"New user created. Welcome, {name.capitalize()}.")
elif menu_choice.capitalize() == "Log In":
    print("Log In")
    # using account number find name and display
    print("Welcome -name-!")
    login_choice = input("\nMenu:\nCheck Balance\nDeposit Money\nWithdraw\nEdit Account\nExit\n")
    if login_choice.capitalize() == "Check Balance":
        # using info find balance and display
        print("Your balance is: $-balance-")
    elif login_choice.capitalize() == "Deposit Money":
        deposit_amount = input("How much money would you like to deposit? ")
        deposit_choice = input ("Deposit\nCancel\n")
        if deposit_choice.capitalize() == "Deposit":
            print("You deposited $-amount-. You now have $-moneyleft- in your account.")
            #function to go back to main menu
            print("Go back to main menu.")
        elif deposit_choice.capitalize() == "Cancel":
            # diplay main menu again (while loop prob)
            print("main menu")
    elif login_choice.capitalize() == "Withdraw":
        withdraw_amount = input("How much would you like to withdraw? ")
        # deposit choice function (again from deposit money - reuse code)
    elif login_choice.capitalize() == "Edit Account":
        # allow edit access & ability to close account, edit name, change pin number, personal identification, etc.
        print("Edit access")
    elif login_choice.capitalize() == "Exit":
        print("Exit. Bye.")
    else:
        print("Please choose a valid option")
elif menu_choice.capitalize() == 'Exit':
    print("Exit. Goodbye! ")
else:
    print("Please choose an option from the menu")
