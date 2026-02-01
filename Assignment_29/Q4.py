import sys
import os
def main():
  if(not(len(sys.argv)==3)):
    print("Please Enter Name of two files.")
    return
  
  File1 , File2 = sys.argv[1] , sys.argv[2]

  if(not(os.path.exists(File1)) or not(os.path.exists(File2))):
    print("Enter Valid File Names.")
    return
  
  FObj1 = open(File1 , "r")
  FObj2 = open(File2 , "r")

  Data1 = FObj1.read()
  Data2 = FObj2.read()

  if(Data1 == Data2):
    print("Sucess...!Contents of Both Files are same.")
  else:
    print("Failure...!Contents of Both Files are not same.")

  
if __name__ == "__main__":
  main()