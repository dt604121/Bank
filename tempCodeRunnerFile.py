import unittest
from unittest.mock import MagicMock
import main
from unittest.mock import patch
import pytest
from main import deposit, withdraw, create_account, delete_account, bank_login, modify_account, display_menu

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
        cursor_mock.execute.assert_called_once_with(
            'SELECT balance FROM accounts WHERE account_number = %s', ('01234567',))

        # Assert that the result is correct
        self.assertEqual(result, 1000)

class TestDeposit(unittest.TestCase):
    def test_deposit_successful(self):
        deposit_amount = 100.00
        account_num = "1234567890"
        pin_num = "1234"
        deposit_result = deposit(deposit_amount, account_num, pin_num)
        # assert deposit returns None for successful deposit
        self.assertIsNone(deposit_result)

    def test_invalid_account_or_pin(self):
        deposit_amount = 100.00
        account_num = "0000000000"  # invalid account number
        pin_num = "1234"
        deposit_result = deposit(deposit_amount, account_num, pin_num)
        # assert deposit returns None for invalid account number
        self.assertIsNone(deposit_result)

        account_num = "1234567890"
        pin_num = "0000"  # invalid PIN
        deposit_result = deposit(deposit_amount, account_num, pin_num)

        # assert deposit returns None for invalid PIN
        self.assertIsNone(deposit_result)

    def test_invalid_deposit_amount(self):
        deposit_amount = 0  # invalid amount
        account_num = "1234567890"
        pin_num = "1234"
        deposit_result = deposit(deposit_amount, account_num, pin_num)
        # assert deposit returns None for invalid deposit amount
        self.assertIsNone(deposit_result)


class TestWithdraw(unittest.TestCase):
    def test_withdraw_successful(self):
        withdraw_amount = 100.00
        account_num = "1234567890"
        pin_num = "1234"
        withdraw_result = withdraw(withdraw_amount, account_num, pin_num)
        # assert deposit returns None for successful deposit
        self.assertIsNone(withdraw_result)

    def test_invalid_account_or_pin(self):
        withdraw_amount = 100.00
        account_num = "0000000000"  # invalid account number
        pin_num = "1234"
        withdraw_result = withdraw(withdraw_amount, account_num, pin_num)
        # assert deposit returns None for invalid account number
        self.assertIsNone(withdraw_result)

        account_num = "1234567890"
        pin_num = "0000"  # invalid PIN
        withdraw_result = withdraw(withdraw_amount, account_num, pin_num)

        # assert deposit returns None for invalid PIN
        self.assertIsNone(withdraw_result)

    def test_invalid_withdraw_amount(self):
        withdraw_amount = 0  # invalid amount
        account_num = "1234567890"
        pin_num = "1234"
        withdraw_result = deposit(withdraw_amount, account_num, pin_num)
        # assert deposit returns None for invalid withdraw amount
        self.assertIsNone(withdraw_result)

class TestCreateAccount(unittest.TestCase):
    def test_create_account_successful(self):
        # Test a successful account creation
        account_num, pin_num, name, balance, birthday = create_account("1234", "111", "Ruth", "100.2", "1-2-2003")
        self.assert_IsNotNone(account_num)
        self.assert_IsNotNone(pin_num)
        self.assert_IsNotNone(name)
        self.assert_IsNotNone(balance)
        self.assert_IsNotNone(birthday)

    def test_duplicate(self):
        with self.assertRaises(main.DuplicateAccountError):
            create_account("1234", "111", "Bob", "1-2-2003")

class TestDeleteAccount(unittest.TestCase):
    def test_delete_account_successful(self):
        # Test case 1: Delete account successfully
        account_num = "123456789"
        pin_num = "1234"
        name = "John Doe"
        # Create a test account
        create_account(account_num, pin_num, name)
        # Delete the account
        delete_account(account_num, pin_num, name)
        # Check if the account was deleted by trying to log in
        assert bank_login(account_num, pin_num) == None

        # Test case 2: Cancel account deletion
        account_num = "987654321"
        pin_num = "4321"
        name = "Jane Doe"
        # Create a test account
        create_account(account_num, pin_num, name)
        # Mock user input to cancel account deletion
        user_input = "2\n"
        with patch('builtins.input', side_effect=user_input):
            delete_account(account_num, pin_num, name)
        # Check if the account still exists by trying to log in
        assert bank_login(account_num, pin_num) != None
    

class TestModifyAccount(unittest.TestCase):
    def test_modify_account_successfull(self):
        # Test case 1: Modify account information successfully
        account_num = "123456789"
        pin_num = "1234"
        # Create a test account
        create_account(account_num, pin_num, "John Doe")
        # Mock user input for updated information
        user_input = "Jane Smith\n5678\n"
        with patch('builtins.input', side_effect=user_input):
            modify_account(account_num, pin_num)
        # Check if the account information was updated correctly
        account_info = bank_login(account_num, "5678")
        assert account_info == {"name": "Jane Smith", "pin": "5678"}

        # Test case 2: Invalid PIN number
        account_num = "987654321"
        pin_num = "4321"
        # Create a test account
        create_account(account_num, pin_num, "Jane Doe")
        # Mock user input for updated information with invalid PIN number
        user_input = "Jane Smith\nabcd\n"
        with patch('builtins.input', side_effect=user_input):
            # Call modify_account function and catch the raised exception
            with pytest.raises(ValueError, match=r"Invalid PIN number. Please enter a 4-digit number."):
                modify_account(account_num, pin_num)
    

class TestDisplayMenu(unittest.Testcase):
    def test_display_menu(capsys):
        # Test case 1: Display the menu successfully
        menu_choice = 0
        name = "John Doe"
        deposit_amount = 100
        withdraw_amount = 50
        withdraw_choice = 1
        account_num = "123456789"
        # Mock user input for menu choice 1
        user_input = "1\n"
        with patch('builtins.input', side_effect=user_input):
            display_menu(menu_choice, name, deposit_amount, withdraw_amount, withdraw_choice, account_num)
        # Capture the output to check if the menu is displayed correctly
        captured_output = capsys.readouterr()
        expected_output = "\n  ~ Home Menu ~\n1) Create An Account\n2) Log In\n3) Exit\n\nPlease choose an option (number 1-3): "
        assert captured_output.out == expected_output

        # Test case 2: Invalid menu choice
        menu_choice = 0
        name = "Jane Doe"
        deposit_amount = 200
        withdraw_amount = 100
        withdraw_choice = 2
        account_num = "987654321"
        # Mock user input for an invalid menu choice
        user_input = "4\n2\n"
        with patch('builtins.input', side_effect=user_input):
            display_menu(menu_choice, name, deposit_amount,
                        withdraw_amount, withdraw_choice, account_num)
        # Capture the output to check if the error message is displayed correctly
        captured_output = capsys.readouterr()
        expected_output = "\n  ~ Home Menu ~\n1) Create An Account\n2) Log In\n3) Exit\n\nPlease choose an option (number 1-3): Please choose a VALID option from the menu 1-3.\n\n  ~ Home Menu ~\n1) Create An Account\n2) Log In\n3) Exit\n\nPlease choose an option (number 1-3): "
        assert captured_output.out == expected_output

if __name__ == '__main__':
    unittest.main()
