def DigitSum(num):
  Sum = 0
  while(num > 0):
    rem = num % 10
    Sum+=rem
    num= num //10

  return Sum

def main():
  num = int(input("Enter Any Number : "))
  Result = DigitSum(num)
  print("Total Digit Sum : ",Result)

if __name__ == "__main__":
  main()