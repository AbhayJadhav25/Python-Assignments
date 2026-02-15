import sys
import os

def DisplayFile(DirectoryName , extension):

  if(not(os.path.exists(DirectoryName))):
    print("Such Directory not exists.")
    return 
  
  if(not(os.path.isdir(DirectoryName))):
    print("Unable to scan . Such file is not directory.")
    return
  border = 15*"-"
  Fobj = open("Answer.txt",'a')
  Fobj.write(f"{border} Question 1 {border}"+"\n")
  for Folder , subFolder , File in os.walk(DirectoryName):

    for Fname in File:
      if Fname.endswith(extension):
        Fobj.write(Fname+"\n")
  Fobj.write(f"{border}{border}"+"\n")
  Fobj.close()
def main():
  DisplayFile(sys.argv[1] , sys.argv[2])
if __name__ == "__main__":
  main()