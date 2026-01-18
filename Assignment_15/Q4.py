from functools import reduce 
def Add(No1 ,No2):
  return No1+No2

Elements_addition = lambda lst : int(reduce(Add , lst))

def main():
  print("Enter number of elements : ")
  n = int(input())
  lst = list()
  print("Enter Elements : ")
  for i in range(n):
    Elements = int(input())
    lst.append(Elements)
  Result = Elements_addition(lst)
  print("Addition = ",Result)
  
if __name__ == "__main__" :
  main()