def FilterChk(num):
  isPrime = True
  for i in range(2 , (num//2)+1):
    if(num%i==0):
      isPrime = False
    
  return isPrime

def MultiplyBy2(num):
  return num*2

def Maximum(num1 , num2):
  return max(num1,num2)

def FMROperations(lst):
  Filter = list(filter(FilterChk , lst))
  print("Data After Filter : " , Filter)
  Map = list(map(MultiplyBy2 , Filter))
  print("Data After Mapped : ",Map)
  from functools import reduce
  Reduce = int(reduce( Maximum , Map))
  return Reduce

def main():
  N = int(input("Enter number of Elements : "))
  print("Enter Elements in List : ")
  lst = []
  
  for i in range(N):
    Elements = int(input())
    lst.append(Elements)
  
  Ans = FMROperations(lst)
  print("Maximum = ",Ans)


if __name__ == "__main__":
  main()