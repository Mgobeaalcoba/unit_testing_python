import pytest
from unit_testing_python.bank_account import BankAccount


@pytest.mark.parametrize(
    'amount, expected',
    [
        (0, 1000),
        (1000, 2000),
        (500, 1500),
        (200, 1200),
        (300, 1300),
    ])
def test_deposit_multiple_amounts(amount, expected):
    account = BankAccount(balance=1000, log_file='test.log')
    if amount == 0:
        with pytest.raises(ValueError):
            account.deposit(amount)
    else:
        assert account.deposit(amount) == expected

