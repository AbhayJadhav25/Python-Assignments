def ChkGreater(No1 , No2) :
  Greater = No1 if No1 > No2 else No2
  return Greater
def main():
  No1 = int(input("Enter First Number : "))
  No2 = int(input("Enter Second Number : "))
  Res = ChkGreater(No1 , No2)
  print("Greater Number : ",Res)
if __name__ == "__main__" :
  main()