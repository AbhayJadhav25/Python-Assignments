def ChkPrime(num):
  isPrime = True
  import math
  for i in range(2 , math.floor(math.sqrt(num))+1):
    if(num % i == 0):
      isPrime = False
      break
  
  return isPrime

def main():
  num = int(input("Enter Any Number : "))
  Result = ChkPrime(num)
  if(Result):
   print(num,"is prime number")
  else :
    print(num,"is not a prime number")

if __name__ == "__main__":
  main()