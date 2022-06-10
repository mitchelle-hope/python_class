class Account:
    # school="AkiraChix"
    def __init__(self,name,number,balance,amount):
        self.name=name
        self.number=number
        self.balance=0
        # self.amount=amount
    def deposit(self):
        self.balance+=self.amount
        return self.balance
    def withdraw(self):
        self.balance-=self.amount
        return self.balance    