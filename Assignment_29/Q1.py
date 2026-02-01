import os
def main():
  FileName = input("Enter Filename : ")
  Ret = os.path.exists(FileName)

  if(Ret):
    print("File exists.")
  else:
    print("File Does'nt exist.")

if __name__ == "__main__":
  main()