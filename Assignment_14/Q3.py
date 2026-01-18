Maximum = lambda No1,No2 : No1 if No1> No2 else No2

def main():
  No1 = int(input("Enter First Number : "))
  No2 = int(input("Enter Second Number : "))
  Res = Maximum(No1,No2)
  print("Maximum Number  = ",Res)
  
if __name__ == "__main__" :
  main()