import math
def ChkPrime(num):
  isPrime = True
  for i in range(2 , math.floor(math.sqrt(num))+1):
    if(num % i ==0):
      isPrime = False
  return isPrime
  