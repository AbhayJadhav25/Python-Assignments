import os 
import sys

def main():
 
  if(len(sys.argv)!=3):
    print("Please Enter Name of two files")
    return
  
  source , dest = sys.argv[1] , sys.argv[2]

  if(os.path.exists(source)):
    FObj = open(source , "r")
    Data = FObj.read()
    print("Content of Source File : ",Data)

    FObj2 = open(dest , "w")
    FObj2.write(Data)
    FObj2.close()

    FObj2 = open(dest , "r")
    Data = FObj2.read()
    print("Content of Destination File : ",Data)

    FObj.close()
    FObj2.close()


  else:
    print("Source File Does'nt exist.")

if __name__ == "__main__":
  main()