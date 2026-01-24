def FilterChk(num):
  return num>=70 and num<=90 

def Increment10(num):
  return num+10

def Product(num1 , num2):
  return num1* num2

def FMROperations(lst):
  Filter = list(filter(FilterChk , lst))
  print("Data After Filter : " , Filter)
  Map = list(map(Increment10 , Filter))
  print("Data After Mapped : ",Map)
  from functools import reduce
  Reduce = int(reduce( Product , Map))
  return Reduce

def main():
  N = int(input("Enter number of Elements : "))
  print("Enter Elements in List : ")
  lst = []
  
  for i in range(N):
    Elements = int(input())
    lst.append(Elements)
  
  Ans = FMROperations(lst)
  print("After Reduce : ",Ans)


if __name__ == "__main__":
  main()