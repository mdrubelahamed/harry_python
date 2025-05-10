class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("First name must be a string")
        self._first_name = value


# p = Person("John", "Doe")
# print(p.full_name)  # Output: John Doe
# print(p.first_name)  # Output: John

# p.first_name = "Jane"
# print(p.full_name)  # Output: Jane Doe

# try:
#     p.first_name = 123
# except TypeError as e:
#     print(e)  # Output: First name must be a string


# ################## Challenge ##################
"""Problem:
Create a BankAccount class with:
balance attribute.
@property for balance to view it.
@setter for balance:
Prevent setting negative balance directly.
Log every balance change (use a list transactions to store history).

Hints:
Log old and new balance in transactions.
Disallow setting balance < 0 directly"""


class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        self.transactions = []  # instance specific

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance can't be negative.")

        old_balance = self.balance
        self._balance = new_balance
        self.log_transaction(old_balance, new_balance)  # log after setting

    def log_transaction(self, old_balance, new_balance):
        self.transactions.append((old_balance, new_balance))

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return

        print("Transaction History:")
        for old_balance, new_balance in self.transactions:
            print(f"{old_balance} ➔ {new_balance}")

    @property
    def transactions_log(self):
        if not self.transactions:
            return "No transactions yet."

        print("Transaction History:")
        for old_balance, new_balance in self.transactions:
            print(f"{old_balance} ➔ {new_balance}")


b = BankAccount(1000)
# print(b.transactions_log)
# print(b.balance)
b.balance = 1200
b.balance = 1500
b.balance = 1800
b.transactions_log  # Clean, just accessing it like an attribute
# b.show_transactions()  # Explicit, method call
