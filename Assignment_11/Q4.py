def  ReverseNumber(No):
  Reverse=0
  while(No>0):
    rem = No%10
    Reverse = (Reverse * 10)+rem
    import math
    No = math.floor(No/10)

  return Reverse

def main():
  No = int(input("Enter Any Number : "))
  Res = ReverseNumber(No)
  print("Reverse Number = ",Res)
  
if __name__ == "__main__" :
  main()