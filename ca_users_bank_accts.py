# Assignment: Users with Bank Accounts
# Create a User class that has an association with the BankAccount class. You should not have to change anything in the BankAccount class.
# But our User class does not have a self.account_balance attribute. What it does have is an instance of a BankAccount by the name of self.account. That means that we'll be mirroring the methods created in the BankAccount class like make_deposit (and other methods referencing self.account_balance). But we'll be calling on the BankAccount class to do most of the work! That's the goal of this assignment, and you may find that you do not have to add much logic if any.

class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= (amount + 5)
        self.balance -= amount

    def display_account_info(self):
        print("Balance: $", self.balance)

    def yield_interest(self, int_rate):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * int_rate)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        # other methods

    def make_deposit(self, amount):
        # your code here
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        # your code here
        self.account.withdraw(amount)

    def display_user_balance(self): # <-(missing colon here - ADDED COLON)
        self.account.display_account_info()


# (comments from John - NEED TO FIX!)
# John M.
# Dec 2, 2022
# Users with Bank Accounts
# incomplete missing test cases and has errors in last method - was not tested - 





jsmith = User("Joe Smith", "jsmith@gmail.com")
jdoe = User("Jane Doe", "jdoe@hotmail.com")

jsmith.make_deposit(25000)
jdoe.make_deposit(10000)

jsmith.display_user_balance()
jdoe.display_user_balance()


