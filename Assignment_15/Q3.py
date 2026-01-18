def ChkEven(No):
  return not(No%2==0)

OddList = lambda lst : list(filter(ChkEven , lst))

def main():
  n = int(input("Number of elements in list : "))
  lst = list()
  print("Enter Elements in List : ")
  for i in range (n):
    Elements = int(input())
    lst.append(Elements)
  Res = OddList(lst)
  print(Res)
if __name__ == "__main__" :
  main()