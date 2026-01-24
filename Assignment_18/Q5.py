from MarvellousSum import ChkPrime

def PrimeSum(lst):
  Sum = 0
  for elements in lst:
    isPrime = ChkPrime(elements)
    if(isPrime):
      print(elements)
      Sum+=elements
  
  return Sum


def main():
  print("Enter Number of Elements : ")
  N = int(input())
  lst = []
  print("Enter",N,"Elements in List : ")
  for i in range(N):
    Elments = int(input())
    lst.append(Elments)

  Result = PrimeSum(lst)
  print("Addition of Prime number : ",Result)
 

if __name__ == "__main__":
  main()