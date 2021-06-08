class BankAccount:
    bank_name = "Second Rate Bank"
    all_accounts = []
    def __init__(self, int_rate=1.02, balance=500):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        self.int_rate
        self.balance
        return self
    def yield_interest(self):
        self.balance *= 1.02
        return self
acct_1 = BankAccount()
acct_2 = BankAccount()

acct_1.deposit(100).deposit(200).deposit(500).withdrawl(50).yield_interest().display_account_info()
print(acct_1.balance)
acct_2.deposit(500).deposit(250).withdrawl(75).withdrawl(100).withdrawl(100).withdrawl(50).yield_interest().display_account_info()
print(acct_2.balance)
