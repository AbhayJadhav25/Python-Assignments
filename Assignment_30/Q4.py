import sys
import os

def copyContent(source , dest):
  if(not(os.path.exists(source))):
    print("No such file exists.")
    return
  
  Fobj = open(source , 'r')

  Data = Fobj.read()

  FObj2 = open(dest , 'w')
  FObj2.write(Data)
  print("Data Copied Successfully.")
  FObj2.close()
  Fobj.close()
def main():
  copyContent(sys.argv[1] , sys.argv[2])
if __name__ == "__main__":
  main()