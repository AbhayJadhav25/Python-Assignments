def FactorAddition(num):
  Sum = 0 
  for i in range(1 , num//2+1):
    if(num % i ==0):
      Sum+=i
    
  return Sum

def main():
  num = int(input("Enter Any Number : "))
  Result = FactorAddition(num)
  print("Factor Addition = ",Result)

if __name__ == "__main__":
  main()