class Account:
    def __init__(self, owner, account_number, balance):
        self._owner = owner
        self._account_number = account_number
        self._balance = balance

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def __str__(self):
        return str(self._owner) + ', ' + str(self._account_number) + ', ' + str(self._balance)

    owner = property(get_owner, set_owner)
    account_number = property(get_account_number, set_account_number)
    amount = property(get_balance, set_balance)