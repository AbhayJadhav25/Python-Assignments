def Square(No):
  return No*No

List_Square = lambda lst : list(map(Square , lst))

def main():
  n = int(input("Number of Elements in list : "))
  lst = list()

  print("Enter Elemnts in List : ")
  for i in range(n):
    Element = int(input())
    lst.append(Element)

  Res = List_Square(lst)
  print(Res)
if __name__ == "__main__" :
  main()