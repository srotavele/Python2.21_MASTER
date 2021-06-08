#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

class User:
    def __init__(self, name, email_address):
         self.name = name
         self.email = email_address
         self.account = BankAccount(int_rate = 1.02, balance = 500)

    def make_deposit(self, amount):
         self.account.deposit += amount
         return self

    def make_withdrawl(self, amount):
         self.account.withdrawl -= amount
         return self

    def display_user_balance(self, name):
         print (f"User: {self.name}, Balance: {self.account.balance}")
         return self

    def transfer_money(self, other_user, amount):
         self.balance -= amount
         other_user.account_balance += amount
         return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
karl = User("Karl Oatmeal", "karl@oatmeal.com")
print(guido.name)
print(monty.name)
print(karl.name)


guido.make_deposit(100).make_deposit(200).make_deposit(500).make_withdrawl(50)

monty.make_deposit(50).make_deposit(250).make_withdrawl(75).make_withdrawl(100).display_user_balance(User)

karl.make_deposit(500).make_withdrawl(100).make_withdrawl(100).make_withdrawl(100)

print(f"Guido's dough = {guido.account.balance}")
print(f"Monty's dough = {monty.account.balance}")
print(f"Karl's dough = {karl.account.balance}")

guido.transfer_money(karl,100)

print(f"Guido's dough = {guido.account.balance}")
print(f"Karl's dough = {karl.account.balance} -Thanks, Guido!!")



