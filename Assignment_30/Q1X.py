import sys
import os
def countLines(FileName):

  if(not(os.path.exists(FileName))):
    print("Such file is not avilable.")
    return
  
  Fobj = open(FileName , "r")
  
  count = 0 
  for line in Fobj:
    if line.strip()!="":
      count+=1


  Fobj.close()
  print(f"File Contains {count} lines.")
def main():
  FileName = sys.argv[1]
  countLines(FileName)
if __name__ == "__main__":
  main()