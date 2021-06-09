#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
class BankAccount:
    bank_name = "Second Rate Bank"
    list_all_accounts = []
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.list_all_accounts.append(self)
    def deposit(self, amount):
        self.balance += (amount)
        return self
    def withdrawl(self, amount):
        self.balance -= (amount)
        return self
    def display_account_info(self):
        self.int_rate
        self.balance
        return self
    def yield_interest(self):
        self.balance *= 0.02
        return self


    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.list_all_accounts:
            sum += account.balance
        return sum
print(BankAccount.bank_name)
print(BankAccount.all_balances())
# print(all_balances())




class User:
    def __init__(self, name, email_address):
        # self.account = []
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    # def new_account(self, int_rate = 0.02, balance = 0):
    #     new_acct = BankAccount(int_rate, balance)
    #     self.account.append(new_acct)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self

    def display_user_balance(self):
        print (f"User: {self.name}, Balance: {self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdrawl(amount)
        other_user.account.deposit(amount)
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
karl = User("Karl Oatmeal", "karl@oatmeal.com")
# karl.new_account(0.02,1500)
# karl.new_account(0.02, 2500)
print(guido.name)
print(monty.name)
print(karl.name)


guido.make_deposit(1000).make_deposit(200).make_deposit(500).make_withdrawl(50).display_user_balance().transfer_money(karl,200)

monty.make_deposit(50).make_deposit(250).make_withdrawl(75).make_withdrawl(100).display_user_balance()

karl.make_deposit(5000).make_withdrawl(100).make_withdrawl(100).make_withdrawl(100).display_user_balance()

print(f"Guido's dough = {guido.account.balance}")
print(f"Monty's dough = {monty.account.balance}")
print(f"Karl's dough = {karl.account.balance}")

print(f"Guido's dough = {guido.account.balance}")
print(f"Karl's dough = {karl.account.balance} -Thanks, Guido!!")
