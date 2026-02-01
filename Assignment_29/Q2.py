import os
def main():
  FileName = input("Enter Filename : ")
  Ret = os.path.exists(FileName)

  if(Ret):
    fobj = open(FileName)
    Data = fobj.read()
    print("Contents of File : ",Data)
  else:
    print("File Does not exist.")
  Ret 
if __name__ == "__main__":
  main()