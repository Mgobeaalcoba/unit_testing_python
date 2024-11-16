import unittest
import os
from faker import Faker
from unit_testing_python.user import User
from unit_testing_python.bank_account import BankAccount


class UserTests(unittest.TestCase):

    def setUp(self):
        self.faker = Faker(locale='es_AR')
        self.user = User(self.faker.name(), self.faker.email(), self.faker.password())
        self.bank_account = BankAccount(balance=10000.00, log_file='test.log')
        self.bank_account_2 = BankAccount(balance=20000.00, log_file='test2.log')

    def test_user_creation(self):
        name = self.faker.name()
        email = self.faker.email()
        password = self.faker.password()
        user = User(name, email, password)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertEqual(user._password, password)
        self.assertEqual(user.accounts, [])

    def test_user_creation_with_account(self):
        name = self.faker.name()
        email = self.faker.email()
        password = self.faker.password()
        account = self.bank_account
        user = User(name, email, password, account)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertEqual(user._password, password)
        self.assertEqual(user.accounts, [account])

    def test_add_account(self):
        self.user.add_account(self.bank_account)
        self.assertEqual(self.user.accounts, [self.bank_account])

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), self.user.name)
        self.assertIsInstance(self.user.get_full_name(), str)

    def test_get_email(self):
        self.assertEqual(self.user.get_email(), self.user.email)
        self.assertIsInstance(self.user.get_email(), str)

    def test_get_account(self):
        self.assertEqual(self.user.get_accounts(), self.user.accounts)
        self.assertIsInstance(self.user.get_accounts(), list)

    def test_get_total_balance(self):
        self.user.add_account(self.bank_account)
        self.user.add_account(self.bank_account_2)
        self.assertEqual(self.user.get_total_balance(), 30000.00)
        self.assertIsInstance(self.user.get_total_balance(), float)

    def test_set_password(self):
        password = self.faker.password()
        self.user.set_password(password)
        self.assertEqual(self.user._password, password)

    def test_set_email(self):
        email = self.faker.email()
        self.user.set_email(email)
        self.assertEqual(self.user.email, email)

    def test_str(self):
        self.assertEqual(str(self.user), f'{self.user.name} - {self.user.email}')

    def tearDown(self):
        os.remove('test.log')
        os.remove('test2.log')


