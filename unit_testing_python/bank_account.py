import random


class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self._account_number = random.randint(100000, 999999)
        self._balance = balance
        self._log_file = log_file
        self._log_transaction(f"Account created with balance: {balance}")

    def _log_transaction(self, message):
        if self._log_file:
            with open(self._log_file, 'a') as file:
                file.write(message + '\n')
        else:
            create_log = input("Do you want to create a log file? (yes/no): ")
            if create_log.lower() == 'yes':
                file_name = input("Enter the file name: ")
                with open(file_name, 'a') as file:
                    file.write(message + '\n')
            else:
                print("No log file created")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log_transaction(f"Deposited: {amount}")
            return self.get_balance()
        else:
            raise ValueError("Amount must be greater than 0")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._log_transaction(f"Withdrew: {amount}")
            return self.get_balance()
        else:
            raise ValueError("Amount must be greater than 0 and less than or equal to balance")

    def transfer(self, amount, account):
        if 0 < amount <= self._balance:
            self.withdraw(amount)
            self._log_transaction(f"Transferred: {amount} to account: {account.get_account_number()}")
            account.deposit(amount)
            return self.get_balance()
        else:
            raise ValueError("Amount must be greater than 0 and less than or equal to balance")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def get_log_file(self):
        return self._log_file
