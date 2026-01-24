
def Maximum(lst):
  # return max(lst)
  Max = float('-inf')
  for element in lst:
    if(element > Max):
      Max = element
    
  return Max

def main():
  print("Enter Number of Elements : ")
  N = int(input())
  lst = []
  print("Enter",N,"Elements in List : ")
  for i in range(N):
    Elments = int(input())
    lst.append(Elments)

  Res = Maximum(lst)
  print("Maximum : ",Res)

if __name__ == "__main__":
  main()