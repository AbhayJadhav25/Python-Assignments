import os
def main():
  FileName = input("Enter File Name : ")

  if(os.path.exists(FileName)):
    Fobj = open(FileName , "r")
    Data = Fobj.read()
    SplitData = Data.split()
    String = input("Enter String to count Frequency : ")
    Count = 0
    for key in SplitData:
      print(key)
      if(String == key):
        Count+=1

    if(Count == 0):
      print(f"{String} does not occurs.")
    elif(Count==1):
      print(f"{String} occurs {Count} time.")
    else:
      print(f"{String} occurs {Count} times.")

  else:
    print("File Does not exists.")

  
if __name__ == "__main__":
  main()