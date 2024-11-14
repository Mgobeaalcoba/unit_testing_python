import unittest
from unit_testing_python.bank_account import BankAccount


class BackAccountTests(unittest.TestCase):

    def setUp(self):
        """
        This method is called before each test.
        It is used to set up the test environment.
        """
        self.account = BankAccount(2000)

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
        other_account = BankAccount(1000)
        new_balance = self.account.transfer(500, other_account)
        self.assertEqual(new_balance, 1500)
        self.assertEqual(other_account.get_balance(), 1500)

    def test_negative_transfer(self):
        other_account = BankAccount(1000)
        with self.assertRaises(ValueError):
            self.account.transfer(-500, other_account)

    def test_over_transfer(self):
        other_account = BankAccount(1000)
        with self.assertRaises(ValueError):
            self.account.transfer(5000, other_account)
