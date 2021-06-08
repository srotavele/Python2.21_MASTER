#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
class User:
        def __init__(self, name, email_address):
         self.name = name
         self.email = email_address
         self.account_balance = 0

        def make_deposit(self, amount):
         self.account_balance += amount

        def make_withdrawl(self, amount):
         self.account_balance -= amount


        def display_user_balance(self, name):
         print (f"User: {self.name}, Balance: {self.account_balance}")

        def transfer_money(self, other_user, amount):
         self.account_balance -= amount
         other_user.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
karl = User("Karl Oatmeal", "karl@oatmeal.com")
print(guido.name)
print(monty.name)
print(karl.name)


guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(500)
guido.make_withdrawl(50)

monty.make_deposit(50)
monty.make_deposit(250)
monty.make_withdrawl(75)
monty.make_withdrawl(100)

karl.make_deposit(500)
karl.make_withdrawl(100)
karl.make_withdrawl(100)
karl.make_withdrawl(100)

print(f"Guido's dough = {guido.account_balance}")
print(f"Monty's dough = {monty.account_balance}")
print(f"Karl's dough = {karl.account_balance}")

monty.display_user_balance(User)
guido.transfer_money(karl,100)

print(f"Guido's dough = {guido.account_balance}")
print(f"Karl's dough = {karl.account_balance}")
