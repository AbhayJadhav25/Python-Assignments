def DivisibleBy3Or5(No):
  return  No % 3==0 or No%5==0

Answer = lambda lst : list(filter(DivisibleBy3Or5 , lst))

def main():
  n = int(input("Enter Any Number : "))
  print("Enter Elements in List : ")
  lst = list()
  for i in range(n):
    Elements = int(input())
    lst.append(Elements)

  Res = Answer(lst)
  print(Res)
if __name__ == "__main__":
  main()