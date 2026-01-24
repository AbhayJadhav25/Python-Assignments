import math
def Minimum(lst):
  # return min(lst)
  Min = float('inf') #Positive Infinity for Negative infinity use float('-inf)
  for element in lst:
    if(element < Min):
      Min = element
    
  return Min

def main():
  print("Enter Number of Elements : ")
  N = int(input())
  lst = []
  print("Enter",N,"Elements in List : ")
  for i in range(N):
    Elments = int(input())
    lst.append(Elments)

  Res = Minimum(lst)
  print("Minimum : ",Res)

if __name__ == "__main__":
  main()