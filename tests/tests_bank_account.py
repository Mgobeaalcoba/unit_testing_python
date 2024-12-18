import unittest
import os
from unittest import mock
from unittest.mock import patch
from unit_testing_python.bank_account import BankAccount
from unit_testing_python.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError


class BackAccountTests(unittest.TestCase):

    def setUp(self):
        """
        This method is called before each test.
        It is used to set up the test environment.
        """
        self.account = BankAccount(2000, 'test_log.txt')
        self.other_account = BankAccount(1000, 'test_log2.txt')
        with mock.patch('builtins.input', return_value='no'):
            self.account_with_no_log = BankAccount(2000)

    def test_deposit(self):
        new_balance = self.account.deposit(1000)
        self.assertEqual(new_balance, 3000)

    @patch('unit_testing_python.bank_account.datetime')
    def test_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 1500)

    @patch('unit_testing_python.bank_account.datetime')
    def test_negative_deposit(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(ValueError):
            self.account.deposit(-1000)

    @patch('unit_testing_python.bank_account.datetime')
    def test_negative_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(-1000)

    @patch('unit_testing_python.bank_account.datetime')
    def test_withdraw_in_unavailable_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 23
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(500)

    @patch('unit_testing_python.bank_account.datetime')
    def test_over_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(5000)

    @patch('unit_testing_python.bank_account.datetime')
    def test_transfer(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.transfer(500, self.other_account)
        self.assertEqual(new_balance, 1500)
        self.assertEqual(self.other_account.get_balance(), 1500)

    @patch('unit_testing_python.bank_account.datetime')
    def test_negative_transfer(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(ValueError):
            self.account.transfer(-500, self.other_account)

    @patch('unit_testing_python.bank_account.datetime')
    def test_over_transfer(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(ValueError):
            self.account.transfer(5000, self.other_account)

    def test_deposit_without_log_file(self):
        with mock.patch('builtins.input', return_value='no'):
            new_balance = self.account_with_no_log.deposit(1000)
        self.assertEqual(new_balance, 3000)

    def test_deposit_in_account_without_log_file_and_creating_the_same(self):
        """
        This test case tests the deposit method in an account without a log file.
        It also tests creating a log file after the deposit.

        The deposit method should return the new balance and a log file should be created.
        """
        with mock.patch('builtins.input', side_effect=['yes', 'test_log.txt']):
            new_balance = self.account_with_no_log.deposit(1000)
        self.assertEqual(new_balance, 3000)
        self.assertTrue(os.path.exists('test_log.txt'))

    @patch('unit_testing_python.bank_account.datetime')
    def test_log_file_is_created_and_messages_are_logged(self, mock_datetime):
        """
        This test case tests if the log file is created and messages are logged in the file.
        Also, it tests the number and the content of messages logged in the file.
        This is very important because it ensures that the log file is created and messages are logged correctly.
        Don't add coverage to the test results, because we are not testing the coverage of the code
        but the functionality of the code.

        The log file should be created and messages should be logged in the file.
        """
        mock_datetime.now.return_value.hour = 10
        self.account.deposit(1000)
        self.account.withdraw(500)
        self.account.transfer(700, self.other_account)
        log_messages = self._read_file_lines('test_log.txt')
        len_log_messages = self._count_file_lines('test_log.txt')
        self.assertEqual(len(log_messages), 5)
        self.assertEqual(log_messages[0], 'Account created with balance: 2000\n')
        self.assertEqual(log_messages[1], 'Deposited: 1000\n')
        self.assertEqual(log_messages[2], 'Withdrew: 500\n')
        self.assertEqual(log_messages[3], 'Withdrew: 700\n')
        self.assertEqual(log_messages[4], f'Transferred: 700 to account: {self.other_account.get_account_number()}\n')
        self.assertEqual(len_log_messages, 5)

    def test_deposit_various_amounts_two_lists(self):
        """
        This test case tests the deposit method with various amounts.
        It tests the deposit method with amounts 0, 1, 1000, and 10000.

        For this, we use the subTest method to run the same test with different data.
        This example is with two lists, one with the amounts and the other with the expected balances.

        The deposit method should return the new balance.
        """
        amounts = [0, 1, 1000, 10000]
        expected_balances = [2000, 2001, 3001, 13001]
        for amount, expected_balance in zip(amounts, expected_balances):
            with self.subTest(amount=amount, expected_balance=expected_balance):
                if amount == 0:
                    with self.assertRaises(ValueError):
                        new_balance = self.account.deposit(amount)
                        self.assertIsNone(new_balance)
                else:
                    new_balance = self.account.deposit(amount)
                    self.assertEqual(new_balance, expected_balance)

    def test_deposit_various_amount_list_of_dicts(self):
        """
        This test case tests the deposit method with various amounts.
        It tests the deposit method with amounts 0, 1, 1000, and 10000.

        For this, we use the subTest method to run the same test with different data.
        This example is with a list of dictionaries, where each dictionary has the amount and the expected balance.

        The deposit method should return the new balance.
        """
        data = [{'amount': 0, 'expected_balance': 2000},
                {'amount': 1, 'expected_balance': 2001},
                {'amount': 1000, 'expected_balance': 3001},
                {'amount': 10000, 'expected_balance': 13001}]
        for item in data:
            with self.subTest(amount=item['amount'], expected_balance=item['expected_balance']):
                if item['amount'] == 0:
                    with self.assertRaises(ValueError):
                        new_balance = self.account.deposit(item['amount'])
                        self.assertIsNone(new_balance)
                else:
                    new_balance = self.account.deposit(item['amount'])
                    self.assertEqual(new_balance, item['expected_balance'])

    @staticmethod
    def _count_file_lines(file_name):
        with open(file_name, 'r') as file:
            content = file.readlines()
            return len(content)

    @staticmethod
    def _read_file_lines(file_name):
        with open(file_name, 'r') as file:
            content = file.readlines()
            return content

    def tearDown(self):
        """
        This method is called after each test.
        It is used to clean up the test environment.
        """
        # Remove the log files
        if self.account.get_log_file():
            if os.path.exists(self.account.get_log_file()):
                os.remove(self.account.get_log_file())
        if self.other_account.get_log_file():
            if os.path.exists(self.other_account.get_log_file()):
                os.remove(self.other_account.get_log_file())
