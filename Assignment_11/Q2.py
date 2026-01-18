def CountDigits(No):
  cnt = 0
  while(No>0):
    import math
    No = math.floor(No/10)
    cnt+=1

  return cnt
def main():
  No = int(input("Enter Any Number : "))
  Res = CountDigits(No)
  print("Total Digits =",Res)
  
if __name__ == "__main__" :
  main()