import datetime

class Digital_Wallet:
    pass


class User:
    wallet_name = 'Digital Wallet'
    def __init__(self, fname, lname, age, address, balance, tiers):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address
        self.balance = balance
        self.tiers = tiers
        self.withdraw = []


    def deposite(self, amount):
        if amount < 0:
            print('Amount cannot be less than 0.')
        
        self.balance+=amount
        print(f'Your current balance is {self.balance}.')

    
    def withdraw(self, withdraw_amt):

        if withdraw_amt < 0 or withdraw_amt > self.balance:
            print('The amount cannot be less than zero or greater than balance.')
        else:
            self.balance = self.balance - withdraw_amt
            self.withdraw.append(withdraw_amt)
            print(f'You have withdraw {withdraw_amt} for your account at date {datetime.datetime.now()}')
        print(f'Your current balance is {self.balance}.')
    


obj = User('Laxman', 'Sharma', 20, 'Samakhusi', 0, "basic")

obj.deposite(2000)
obj.withdraw(1000)

