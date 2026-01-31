class Numbers :
  def __init__(self):
    self.Value  = int(input("Enter a Number : "))

  def ChkPrime(self):
    Num = self.Value
    isPrime = True
    import math
    for i in range(2 , math.floor(math.sqrt(Num))+1):
      if(Num % i == 0):
        isPrime = False
    
    if(isPrime):
      print(f"{Num} is Prime number ")
    else :
      print(f"{Num} is not prime number")

  def ChkPerfect(self):
    Num = self.Value
    Sum = 0

    for i in range(1 , Num//2 +1):
      if(Num % i == 0):
        Sum+=i

    if(Sum == Num):
      print(f"{self.Value} is a perfect Number ")
    else:
      print(f"{self.Value} is not a perfect number")

  def Factors(self):
    for i in range(1 ,self.Value //2+1):
      if(self.Value % i  == 0):
        print(i ,end = " ")
    print()

  def SumFactors(self):
    Num = self.Value
    Sum = 0

    for i in range(1 , Num//2+1):
      if(Num % i == 0):
        Sum+=i

    print("Sum of factors : ",Sum)

def main():
  Obj1 = Numbers()
  Obj1.ChkPrime()
  Obj1.ChkPerfect()
  Obj1.Factors()
  Obj1.SumFactors()

  print("-"*10)

  Obj2 = Numbers()
  Obj2.ChkPrime()
  Obj2.ChkPerfect()
  Obj2.Factors()
  Obj2.SumFactors()

if __name__ == "__main__":
  main()
