import threading
def evenFactors(num):
  sum = 0
  for i in range(1 , num//2 +1):
    if(num % i == 0):
      if(i % 2 == 0):
        sum+=i
  print("Addition of Even Factors : ",sum)

def oddFactors(num):
  sum = 0
  for i in range(1 , num//2 +1):
    if(num % i == 0):
      if(not(i % 2 == 0)):
        sum+=i
  print("Addition of Odd Factors : ",sum)

def main():
  num = int(input("Enter any Number : "))
  EvenFactor = threading.Thread(target = evenFactors , args =(num , ))

  OddFactor = threading.Thread(target = oddFactors , args =(num , ))

  EvenFactor.start()
  OddFactor.start()
  EvenFactor.join()
  OddFactor.join()

  print("Exit From main.")

if __name__ == "__main__":
  main()