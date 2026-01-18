def ChkEven(No):
  return No%2==0

EvenList = lambda lst : list(filter(ChkEven , lst))

def main():
  n = int(input("Number of elements in list : "))
  lst = list()
  print("Enter Elements in List : ")
  for i in range (n):
    Elements = int(input())
    lst.append(Elements)
  Res = EvenList(lst)
  print(Res)
if __name__ == "__main__" :
  main()