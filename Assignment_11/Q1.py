import math
def  ChkPrime(No):
  isPrime = True
  for i in range(2 , math.floor(math.sqrt(No)+1)):
    if(No%i == 0):
      isPrime = False
    
  return isPrime

def main():
  No = int(input("Enter Any Number : "))
  Res = ChkPrime(No)
  if(Res):
    print(No,"is Prime Number")
  else:
    print(No,"is not Prime Number")
    

if __name__ == "__main__" :
  main()