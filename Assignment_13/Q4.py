def BinaryEquivalent(No):
  Res = ""
  while(No>0):
    import math
    rem = No%2
    Res = Res + str(rem)
    No = No//2

  print(int(Res[::-1]))

def main():
  No = int(input("Enter Any Number : "))
  BinaryEquivalent(No)
  
if __name__ == "__main__" :
  main()