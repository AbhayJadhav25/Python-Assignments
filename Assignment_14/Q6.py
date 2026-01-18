ChkOdd = lambda No : True if not(No%2==0) else False

def main():
  No = int(input("Enter Any Number : "))
  Res = ChkOdd(No)
  print("Result = ",Res)
  
if __name__ == "__main__" :
  main()