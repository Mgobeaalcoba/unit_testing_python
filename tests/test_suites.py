import unittest

from tests.tests_bank_account import BackAccountTests


def bank_account_suite():
    """
    This function creates a test suite for the bank account tests.
    """
    suite = unittest.TestSuite()
    tests = [
        BackAccountTests('setUp'),
        BackAccountTests('test_deposit'),
        BackAccountTests('test_withdraw'),
        BackAccountTests('test_negative_deposit'),
        BackAccountTests('test_negative_withdraw'),
        BackAccountTests('test_over_withdraw'),
        BackAccountTests('test_transfer'),
        BackAccountTests('test_negative_transfer'),
        BackAccountTests('test_over_transfer'),
        BackAccountTests('test_deposit_without_log_file'),
        BackAccountTests('test_deposit_in_account_without_log_file_and_creating_the_same'),
        BackAccountTests('tearDown')
    ]
    suite.addTests(tests)
    return suite


if __name__ == '__main__':
    """
    This block of code runs the test suite.
    """
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())