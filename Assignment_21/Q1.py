import threading
def primeNums(lst):
  prime = []
  for element in lst :
    isPrime = True
    for i in range(2 , element//2+1):
      if(element % i == 0):
        isPrime = False
    
    if(isPrime):
      prime.append(element)
  print("Prime Numbers : ",prime)


def nonPrimeNums(lst):
  nonPrime = []
  for element in lst :
    isPrime = True
    for i in range(2 , element//2+1):
      if(element % i == 0):
        isPrime = False
        
    if(isPrime == False):
      nonPrime.append(element)
  print("Non Prime Numbers : ",nonPrime)

def main():
  print("Enter number of Elements : ")
  N = int(input())
  lst = []
  print("Enter Elements in List : ")
  for i in range(N):
    Element = int(input())
    lst.append(Element)

  Prime = threading.Thread(target = primeNums , args = (lst,)) 
  NonPrime = threading.Thread(target = nonPrimeNums , args = (lst,)) 

  Prime.start()
  NonPrime.start()
  Prime.join()
  NonPrime.join()

if __name__ == "__main__":
  main()