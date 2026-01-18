def  SumOfDigits(No):
  Sum=0
  for i in range(1 , No+1):
    rem = No%10
    Sum+=rem
    import math
    No = math.floor(No/10)
  return Sum
def main():
  No = int(input("Enter Any Number : "))
  Res = SumOfDigits(No)
  print("Sum of Digits = ",Res)
  
if __name__ == "__main__" :
  main()