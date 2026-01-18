from functools import reduce
def MinimumNum(No1 , No2):
  if(No1<No2):
    return No1
  else :
    return No2

Minimum = lambda lst : int(reduce(MinimumNum , lst))

def main():
  print("Enter number of elements : ")
  n = int(input())
  lst = list()
  print("Enter Elements in List : ")
  for i in range(n):
    Elements = int(input())
    lst.append(Elements)

  Result = Minimum(lst)
  print("Maximum Result : ",Result)

if __name__ == "__main__":
  main()