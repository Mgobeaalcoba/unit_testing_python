class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self.get_balance()
        else:
            raise ValueError("Amount must be greater than 0")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return self.get_balance()
        else:
            raise ValueError("Amount must be greater than 0 and less than or equal to balance")

    def transfer(self, amount, account):
        if 0 < amount <= self._balance:
            self.withdraw(amount)
            account.deposit(amount)
            return self.get_balance()
        else:
            raise ValueError("Amount must be greater than 0 and less than or equal to balance")

    def get_balance(self):
        return self._balance

