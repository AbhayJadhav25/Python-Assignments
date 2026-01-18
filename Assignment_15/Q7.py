def printStrinng(str):
  if(len(str)>=5):
    return str
  
Str_5 = lambda lst : list(filter(printStrinng , lst))

def main():
  n = int(input("Enter Any Number : "))
  print("Enter Elements in List : ")
  lst = list()
  for i in range(n):
    Elements = input()
    lst.append(Elements)
  
  Result = Str_5(lst)
  print(Result)

if __name__ == "__main__":
  main()