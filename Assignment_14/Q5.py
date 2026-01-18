ChkEven = lambda No : True if No%2==0 else False

def main():
  No = int(input("Enter Any Number : "))
  Res = ChkEven(No)
  print("Result = ",Res)
  
if __name__ == "__main__" :
  main()