from functools import reduce

def Multiplication(No1 , No2):
  return No1 * No2

ListProduct = lambda lst : int(reduce(Multiplication , lst))

def main():
  n = int(input("Enter Number of Elements : "))
  print("Enter Elements in List : ")
  lst = list()
  for i in range(n):
    Elemnts = int(input())
    lst.append(Elemnts)
  
  Result = ListProduct(lst)
  print(Result)

if __name__ == "__main__":
  main()