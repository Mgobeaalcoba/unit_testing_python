import unittest
import os
from unittest import mock
from unit_testing_python.bank_account import BankAccount

SERVER = os.environ.get('SERVER', 'prod')  # prod is the default value


# Skip all tests
@unittest.skip("Skipping all tests")
class SkipTestTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(2000, 'test_log.txt')
        self.other_account = BankAccount(1000, 'test_log2.txt')
        with mock.patch('builtins.input', return_value='no'):
            self.account_with_no_log = BankAccount(2000)

    @staticmethod
    def test_skip():
        assert 1 == 1

    @staticmethod
    def test_skip_2():
        assert 2 == 2

    @staticmethod
    def test_skip_3():
        assert 3 == 3

    def tearDown(self):
        if self.account.get_log_file():
            os.remove(self.account.get_log_file())
        if self.other_account.get_log_file():
            os.remove(self.other_account.get_log_file())


# Skip a specific test
class SkipSpecificTestTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(2000, 'test_log.txt')
        self.other_account = BankAccount(1000, 'test_log2.txt')
        with mock.patch('builtins.input', return_value='no'):
            self.account_with_no_log = BankAccount(2000)

    @unittest.skip("Skipping this test")
    def test_skip(self):
        assert 1 == 1

    def test_skip_2(self):
        assert 2 == 2

    @unittest.skipIf(SERVER == 'prod', "Skipping this test in prod")
    def test_skip_3(self):
        assert 3 == 3

    @unittest.skipUnless(SERVER == 'prod', "Skipping this test unless in prod")
    def test_skip_4(self):
        assert 4 == 4

    @unittest.expectedFailure
    def test_expected_failure(self):
        assert 5 == 6

    @unittest.expectedFailure
    def test_expected_failure_2(self):
        assert 6 == 7

    @unittest.expectedFailure
    def test_expected_failure_3(self):
        assert 7 == 8

    def tearDown(self):
        if self.account.get_log_file():
            os.remove(self.account.get_log_file())
        if self.other_account.get_log_file():
            os.remove(self.other_account.get_log_file())
