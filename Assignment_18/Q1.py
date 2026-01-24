# from functools import reduce
# def Add(No1 , No2):
#   return No1+No2 

# Addition = lambda lst : int(reduce(Add,lst))

def Addi(lst):
  Sum = 0
  for element in lst:
    Sum+=element
  
  return Sum

def main():
  print("Enter Number of Elements : ")
  N = int(input())
  lst = []
  print("Enter",N,"Elements in List : ")
  for i in range(N):
    Elments = int(input())
    lst.append(Elments)

  Res = Addi(lst)
  print("Addition of Elements : ",Res)

if __name__ == "__main__":
  main()