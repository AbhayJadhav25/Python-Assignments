import sys
import os

def renameFile( DirectoryName,srcExtension , destExtension):

  if(not(os.path.exists(DirectoryName))):
    print("Such Directory not exists.")
    return 
  
  if(not(os.path.isdir(DirectoryName))):
    print("Unable to scan . Such file is not directory.")
    return
  Fobj = open("Answer.txt" , 'w')
  border = "-"*10
  Fobj.write(f"{border} Question 2 {border}"+"\n")
  for Folder , subFolder , File in os.walk(DirectoryName):

    for Fname in File:

      if Fname.endswith(srcExtension) :

        old_path = os.path.join(Folder , Fname)
        NewFname = os.path.splitext(Fname)[0] + destExtension
        new_path = os.path.join(Folder , NewFname)
        os.rename(old_path , new_path)

  Fobj.write(f"{border}Operation Sucessful{border}"+"\n")
  Fobj.write(f"{border}Question 3 {border}"+"\n")
  Fobj.close()

def main():
  renameFile(sys.argv[1] , sys.argv[2] , sys.argv[3])
if __name__ == "__main__":
  main()