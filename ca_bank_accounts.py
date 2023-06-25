# Assignment: BankAccount
# For this assignment, don't worry about putting any user information in the BankAccount class. We'll take care of that in the next lesson!
# Let's first just get some more practice writing classes by writing a new BankAccount class.
# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)
# The class should also have the following methods:
# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
# This means we need a class that looks something like this:

class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []

    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= (amount + 5)
        self.balance -= amount
        return self

    def display_account_info(self):
        # your code here
        print("Balance: $", self.balance)
        return self

    def yield_interest(self, int_rate):
        # your code here
        if self.balance > 0:
            self.balance = self.balance + (self.balance * int_rate)
        return self

# Create 2 accounts
mrBallerAccount = BankAccount(.05, 100000)
mrsBlingAccount = BankAccount(.02, 350000)
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the accounts info all in one line of code (i.e.chaining)
mrBallerAccount.deposit(50000).deposit(500000).deposit(1000000).withdraw(9500).yield_interest(.05).display_account_info()
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
mrsBlingAccount.deposit(9000).deposit(45000).withdraw(6900).withdraw(8800).withdraw(5000).withdraw(9500).yield_interest(.02).display_account_info()