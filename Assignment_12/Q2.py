def PrintFactors(No):
  import math
  for i in range(1, No+1):
    if(No % i == 0):
      print(i , end=" ")
def main():
  No = int(input("Enter Any Number : "))
  PrintFactors(No)
  
if __name__ == "__main__" :
  main()