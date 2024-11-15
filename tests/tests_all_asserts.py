import unittest
import os
from unittest import mock
from unit_testing_python.bank_account import BankAccount


class AllAssertsTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(2000, 'test_log.txt')
        self.other_account = BankAccount(1000, 'test_log2.txt')
        with mock.patch('builtins.input', return_value='no'):
            self.account_with_no_log = BankAccount(2000)

    def test_assert_equal(self):
        new_balance = self.account.deposit(1000)
        self.assertEqual(new_balance, 3000)

    def test_assert_not_equal(self):
        new_balance = self.account.deposit(1000)
        self.assertNotEqual(new_balance, 2000)

    def test_assert_true(self):
        new_balance = self.account.deposit(1000)
        self.assertTrue(new_balance == 3000)

    def test_assert_false(self):
        new_balance = self.account.deposit(1000)
        self.assertFalse(new_balance == 2000)

    def test_assert_is(self):
        new_balance = self.account.deposit(1000)
        copy_balance = new_balance
        self.assertIs(new_balance, copy_balance)

    def test_assert_is_not(self):
        new_balance = self.account.deposit(1000)
        self.assertIsNot(new_balance, 2000)

    def test_assert_is_none(self):
        self.assertIsNone(self.account_with_no_log.get_log_file())

    def test_assert_is_not_none(self):
        self.assertIsNotNone(self.account.get_log_file())

    def test_assert_in(self):
        self.assertIn('test_log', self.account.get_log_file())

    def test_assert_not_in(self):
        self.assertNotIn('log_test', self.account.get_log_file())

    def test_assert_is_instance(self):
        self.assertIsInstance(self.account, BankAccount)

    def test_assert_not_is_instance(self):
        self.assertNotIsInstance(self.account, str)

    def test_assert_greater(self):
        new_balance = self.account.deposit(1000)
        self.assertGreater(new_balance, 2000)

    def test_assert_greater_equal(self):
        new_balance = self.account.deposit(1000)
        self.assertGreaterEqual(new_balance, 3000)

    def test_assert_less(self):
        new_balance = self.account.deposit(1000)
        self.assertLess(new_balance, 4000)

    def test_assert_less_equal(self):
        new_balance = self.account.deposit(1000)
        self.assertLessEqual(new_balance, 3000)

    def test_assert_almost_equal(self):
        """
        The assertAlmostEqual method is used to check if two values are almost equal.
        The places parameter is used to specify the number of decimal places to consider.
        The numbers are rounded to the number of decimal places specified by the places parameter.
        """
        new_balance = self.account.deposit(1000.4)
        self.assertAlmostEqual(new_balance, 3000.0, places=0)

    def test_assert_not_almost_equal(self):
        new_balance = self.account.deposit(1000.6)
        self.assertNotAlmostEqual(new_balance, 3000.0, places=0)

    def test_assert_regex(self):
        self.assertRegex(self.account.get_log_file(), r'[a-z]+_[a-z]+\.txt')

    def test_assert_not_regex(self):
        self.assertNotRegex(self.account.get_log_file(), r'[0-9]+_[0-9]+\.txt')

    def test_assert_count_equal(self):
        self.account.deposit(1000)
        content = self._list_file_content(self.account.get_log_file())
        self.assertCountEqual(content, ['Account created with balance: 2000\n', 'Deposited: 1000\n'])

    def test_assert_multi_line_equal(self):
        self.account.deposit(1000)
        content = self._list_file_content(self.account.get_log_file())
        self.assertMultiLineEqual(''.join(content), 'Account created with balance: 2000\nDeposited: 1000\n')

    def test_assert_sequence_equal(self):
        self.account.deposit(1000)
        content = self._list_file_content(self.account.get_log_file())
        self.assertSequenceEqual(content, ['Account created with balance: 2000\n', 'Deposited: 1000\n'],
                                 'Messages are not equal', seq_type=list)

    def test_assert_list_equal(self):
        self.account.deposit(1000)
        content = self._list_file_content(self.account.get_log_file())
        self.assertListEqual(content, ['Account created with balance: 2000\n', 'Deposited: 1000\n'],
                             'Messages are not equal')

    def test_assert_tuple_equal(self):
        self.account.deposit(1000)
        content = self._list_file_content(self.account.get_log_file())
        self.assertTupleEqual(tuple(content), ('Account created with balance: 2000\n', 'Deposited: 1000\n'),
                              'Messages are not equal')

    def test_assert_set_equal(self):
        self.account.deposit(1000)
        content = self._list_file_content(self.account.get_log_file())
        self.assertSetEqual(set(content), {'Account created with balance: 2000\n', 'Deposited: 1000\n'},
                            'Messages are not equal')

    def test_assert_dict_equal(self):
        self.account.deposit(1000)
        content = self._list_file_content(self.account.get_log_file())
        self.assertDictEqual({1: content[0], 2: content[1]}, {1: 'Account created with balance: 2000\n',
                                                              2: 'Deposited: 1000\n'}, 'Messages are not equal')

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-1000)

    def test_assert_raises_regex(self):
        with self.assertRaisesRegex(ValueError, r'Amount must be greater than 0'):
            self.account.deposit(-1000)

    @staticmethod
    def _list_file_content(file_name):
        with open(file_name, 'r') as file:
            content = file.readlines()
            return content

    def tearDown(self):
        if self.account.get_log_file():
            os.remove(self.account.get_log_file())
        if self.other_account.get_log_file():
            os.remove(self.other_account.get_log_file())
