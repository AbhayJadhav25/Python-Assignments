class BankkAccount :
  Rate_of_Interest = 10.5
  def __init__(self):
    self.Name = input("Enter Account Holder Name :  ")
    self.Amount = int(input("Enter amouont : "))

  def Disply(self):
    print(f"Acount Holder : {self.Name} \n Current Balance : {self.Amount}")

  def Deposit(self):
    credit = int(input("Enter Amount to Credit : "))
    self.Amount += credit
    self.Disply()

  def Withdraw(self):
    debit = int(input("Enter Amount to Debit  :"))
    if(self.Amount < debit):
      print("No sufficient Balance>")
    else:
      self.Amount -= debit
    self.Disply()
    
 
  def CalculateInterest(self):
    self.Amount += (self.Amount * BankkAccount.Rate_of_Interest)/100
    self.Disply()

def main():
  Holder1 = BankkAccount()
  Holder1.Disply()
  Holder1.Deposit()
  Holder1.Withdraw()
  Holder1.CalculateInterest()

  print("-"*10)
  Holder2 = BankkAccount()
  Holder2.Disply()
  Holder2.Deposit()
  Holder2.Withdraw()
  Holder2.CalculateInterest()

if __name__ == "__main__":
  main()

  