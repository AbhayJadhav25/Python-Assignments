# Maximum = lambda No1,No2 , No3: No1 if No1>No2 and No1>No3 else No2 if No2>No1 and No2>No3 else No3

Maximum = lambda No1,No2 , No3: max(No1 , No2 , No3)

def main():
  No1 = int(input("Enter First Number : "))
  No2 = int(input("Enter Second Number : "))
  No3 = int(input("Enter Third Number : "))
  Res = Maximum(No1,No2 , No3)
  print("Addition of Numbers  = ",Res)
  
if __name__ == "__main__" :
  main()