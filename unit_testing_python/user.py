from unit_testing_python.bank_account import BankAccount
from functools import reduce
from typing import List
from faker import Faker


class User:
    def __init__(self, name: str, email: str, password: str, account: BankAccount = None) -> None:
        self.name = name
        self.email = email
        self._password = password
        self.accounts = []
        if account:
            self.add_account(account)

    def add_account(self, account: BankAccount) -> None:
        self.accounts.append(account)

    def get_full_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_accounts(self) -> List[BankAccount]:
        return self.accounts

    def get_total_balance(self) -> float:
        accounts = self.get_accounts()
        return reduce(lambda x, y: x + y.get_balance(), accounts, 0)

    def set_password(self, password: str) -> None:
        self._password = password

    def set_email(self, email: str) -> None:
        self.email = email

    def __str__(self):
        return f'{self.name} - {self.email}'


if __name__ == '__main__':
    faker = Faker(locale='es_AR')
    user = User(
        name=faker.name(),
        email=faker.email(),
        password=faker.password(),
        account=BankAccount(balance=faker.pyfloat(), log_file=f'{faker.word()}.log')
    )
    print(str(user))
    print(user.get_total_balance())
    print(user.get_accounts())
    print(user.get_email())
    print(user.get_full_name())
    user.set_password(faker.password())
    user.set_email(faker.email())
    print(str(user))
    print(user.get_total_balance())
    print(user.get_accounts())
    print(user.get_email())
    print(user.get_full_name())
