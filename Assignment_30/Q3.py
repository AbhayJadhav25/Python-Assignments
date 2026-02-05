import sys
import os

def printLineByLine(FileName):
  if(not(os.path.exists(FileName))):
    print("No such file exists.")
    return
  
  Fobj = open(FileName , 'r')

  for line in Fobj:
    print(line)

  Fobj.close()
def main():
  printLineByLine(sys.argv[1])
if __name__ == "__main__":
  main()