import math
def CountFrequency(lst , num):
  cnt = 0
  for element in lst:
    if(element == num):
      cnt+=1
    
  return cnt

def main():
  print("Enter Number of Elements : ")
  N = int(input())
  lst = []
  print("Enter",N,"Elements in List : ")
  for i in range(N):
    Elments = int(input())
    lst.append(Elments)

  print("Enter Number to Count : ")
  num = int(input())
  Res = CountFrequency(lst , num)
  print("Number Occurance : ",Res)

if __name__ == "__main__":
  main()