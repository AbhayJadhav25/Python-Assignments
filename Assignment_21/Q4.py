import threading
from functools import reduce

def Add(no1 , no2):
  return no1+no2


def MUL(no1 , no2):
  return no1 * no2

def Addition(lst , result):
    result[0] =  int(reduce(Add , lst)) 

def Multiplication(lst , result):
    result[1] =  int(reduce(MUL , lst))

def main():
  print("Enter number of Elements : ")
  N = int(input())
  lst = []
  print("Enter Elements in List : ")
  for i in range(N):
    Element = int(input())
    lst.append(Element)
  result = [0 , 0]
  Thread1 = threading.Thread(target = Addition , args = (lst,result)) 
  Thread2 = threading.Thread(target = Multiplication , args = (lst,result)) 

  Thread1.start()
  Thread2.start()
  Thread1.join()
  Thread2.join()

  print("Addition = ",result[0])
  print("Multiplication = ",result[1])


if __name__ == "__main__":
  main()