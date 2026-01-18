def SumOfN(No):
  Sum = 0
  for i in range(1 , No+1):
    Sum+=i

  return Sum
def main():
  No = int(input("Enter any Number : "))
  Res = SumOfN(No)

  print("Sum of first ",No,"Number = ",Res)
if __name__ == "__main__" :
  main()