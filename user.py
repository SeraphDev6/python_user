class User:
    def __init__(self,name,intial_deposit=0):
        self.name=name
        self.balance=0
        self.make_deposit(intial_deposit)

    def make_deposit(self,amount):
        self.balance+=amount
        print(f"Successfully deposited ${amount} into {self.name}'s account.")
        print(f"{self.name}'s current balance is ${self.balance}")

    def make_withdrawl(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f"Successfully withdrew ${amount} from {self.name}'s account.")
            print(f"{self.name}'s current balance is ${self.balance}")
        else:
            print(f"{self.name} does not have enough funds to make this withdrawl")
            print(f"{self.name}'s current balance is ${self.balance}")

    def display_user_balance(self):
        print(f"{self.name}'s current balance is ${self.balance}")

    def transfer_money(self,other_user ,amount):
        if self.balance >= amount:
            other_user.balance+=amount
            self.balance-=amount
            print(f"Successfully transfered ${amount} from {self.name} to ${other_user.name}")
            print(f"{self.name}'s current balance is ${self.balance}")
            print(f"{other_user.name}'s current balance is ${other_user.balance}")
        else:
            print(f"{self.name} does not have enough funds to make this transfer")
            print(f"{self.name}'s current balance is ${self.balance}")

wesley=User("Wesley",2050)
peter=User("Peter",9001)
marius=User("Marius",700)

wesley.make_deposit(200)
wesley.make_deposit(900)
wesley.make_deposit(210)
wesley.make_withdrawl(3000)
wesley.display_user_balance()

peter.make_deposit(900)
peter.make_deposit(210)
peter.make_withdrawl(3000)
peter.make_withdrawl(500)
peter.display_user_balance()

marius.make_withdrawl(3000)
marius.make_deposit(21000)
marius.make_withdrawl(3000)
marius.make_withdrawl(500)
marius.display_user_balance()