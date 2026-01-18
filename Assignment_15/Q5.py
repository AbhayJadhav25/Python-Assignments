from functools import reduce
def MaximumNum(No1 , No2):
  if(No1>No2):
    return No1
  else :
    return No2

Maximum = lambda lst : int(reduce(MaximumNum , lst))

def main():
  print("Enter number of elements : ")
  n = int(input())
  lst = list()
  print("Enter Elements in List : ")
  for i in range(n):
    Elements = int(input())
    lst.append(Elements)

  Result = Maximum(lst)
  print("Maximum Result : ",Result)

if __name__ == "__main__":
  main()