import unittest
import os
from unittest import mock
from unit_testing_python.bank_account import BankAccount


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

    def test_withdraw(self):
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 1500)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-1000)

    def test_negative_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-1000)

    def test_over_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(5000)

    def test_transfer(self):
        new_balance = self.account.transfer(500, self.other_account)
        self.assertEqual(new_balance, 1500)
        self.assertEqual(self.other_account.get_balance(), 1500)

    def test_negative_transfer(self):
        with self.assertRaises(ValueError):
            self.account.transfer(-500, self.other_account)

    def test_over_transfer(self):
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

    def test_log_file_is_created_and_messages_are_logged(self):
        """
        This test case tests if the log file is created and messages are logged in the file.
        Also, it tests the number and the content of messages logged in the file.
        This is very important because it ensures that the log file is created and messages are logged correctly.
        Don't add coverage to the test results, because we are not testing the coverage of the code
        but the functionality of the code.

        The log file should be created and messages should be logged in the file.
        """
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
