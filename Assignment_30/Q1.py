import sys
import os
def countLines(FileName):

  if(not(os.path.exists(FileName))):
    print("Such file is not avilable.")
    return
  
  Fobj = open(FileName , "r")
  Data = Fobj.readlines()
  # Data = Data.split()


  Fobj.close()
  print(f"File Contains {len(Data)} lines.")
def main():
  FileName = sys.argv[1]
  countLines(FileName)
if __name__ == "__main__":
  main()