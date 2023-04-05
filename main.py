print("Hello There! Welcome to Easy Bank :)")
account_num = input("Account Number: ")
pin = input("PIN: ")
menu_choice = input("\nMenu:\nCreate Account\nLog In\nExit\n")
if menu_choice.capitalize() == "Create Account":
    print("Create A New Account")
elif menu_choice.capitalize() == "Log In":
    print("Log In")
elif menu_choice.capitalize() == 'Exit':
    print("Exit. Goodbye! ")
else:
    print("Please choose an option from the menu")
