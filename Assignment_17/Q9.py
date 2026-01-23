def TotalDigit(num):
  digitCount = 0
  while(num > 0):
    digitCount+=1
    num= num //10

  return digitCount

def main():
  num = int(input("Enter Any Number : "))
  Result = TotalDigit(num)
  print("Total Digit : ",Result)

if __name__ == "__main__":
  main()