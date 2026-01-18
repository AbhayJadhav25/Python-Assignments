Minimum = lambda No1,No2 : No1 if No1< No2 else No2

def main():
  No1 = int(input("Enter First Number : "))
  No2 = int(input("Enter Second Number : "))
  Res = Minimum(No1,No2)
  print("Minimum Number  = ",Res)
  
if __name__ == "__main__" :
  main()