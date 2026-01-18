def  ChkPerfect(No):
  isPerfect = False
  Sum = 0
  import math
  for i in range(1 , math.floor(No/2)+1):
    if(No%i == 0):
      Sum+=i
  
  if(Sum == No):
    isPerfect = True
  return isPerfect
def main():
  No = int(input("Enter Any Number : "))
  Res = ChkPerfect(No)

  if(Res):
    print("Perfect Number")
  else:
    print("Not Perfect")
  
if __name__ == "__main__" :
  main()