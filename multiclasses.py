class Account:
  def __init__(self,account_name,account_number ):
    self.account_name=account_name
    self.account_number=account_number
    self.balance=0
    self.deposits=[]
    self.withdrawals=[]
  def deposit(self,amount):
    self.deposits.append(amount)
  
    if amount<=0:
      return f"hello{self.account_name}you have deposited {amount}and your new balance is {self.balance}"
    else:
      self.balance+=amount
    return f"You have deposited {self.balance}"

  def withdraw(self,amount):
    self.withdrawals.append(amount)
    self.transaction=100
    if amount>self.balance:
      return f"your balance is {self.balance}you cant withdraw{amount}"
    elif amount>self.balance:
      return f"you cannot withdraw{amount}."
  
    else:
      self.balance-=amount+self.transaction
      return f"hello{self.account_name},you have withdrawn{amount}your balance is {self.balance}your withdrarals are {self.withdrawals}"
  def deposit_stmnt(self):
      for depo in self.deposits:
       print(depo, end="/n")

  def withdrawals_stmnt(self):
      for drawals in self.withdrawls:
         print(drawals,end="/n")
  def current_balance(self):
      return self.balance


   
     
