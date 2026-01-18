def checkDivisibility(No):
  return (No%3==0 and No%5==0)
def main():
  No = int(input("Enter any Number : "))
  Res = checkDivisibility(No)
  if(Res):
    print(No,"is divisible by 3 & 5")
  else:
    print(No,"is not divisible by 3 & 5")

if __name__ == "__main__" :
  main()