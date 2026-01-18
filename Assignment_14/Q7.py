DivisibleBy5 = lambda No : True if No%5==0 else False

def main():
  No = int(input("Enter Any Number : "))
  Res = DivisibleBy5(No)
  print("Result = ",Res)
  
if __name__ == "__main__" :
  main()