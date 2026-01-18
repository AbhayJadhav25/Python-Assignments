def Square(No):
  return No*No

def main():
  No = int(input("Enter any Number : "))
  Res = Square(No)
  print("Square of ",No,"=",Res)
  
if __name__ == "__main__" :
  main()