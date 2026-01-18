def Factorial(No):
  Fact = 1
  i=1
  while(i<=No):
    Fact*=i
    i+=1
  return Fact

def main():
  No = int(input("Enter Any Number : "))
  Res = Factorial(No)
  print("Factorial Of ",No,"=",Res)

if __name__ == "__main__" :
  main()