import os
import sys
import shutil
def copyOperation(SourceDir , DestDir):
  if(not(os.path.exists(SourceDir))):
    print("No Such directory Avilable.")
    return
  
  if(not(os.path.isdir(SourceDir))):
    print("Unable to scan . This is not directory.")
    return
  
  ret = os.path.exists(DestDir)

  if(ret == True):
    ret = os.path.isdir(DestDir)
    if(ret == False):
      print("Unable to copy.")
      return
  else:
    os.makedirs(DestDir , exist_ok=True)

  for folder , subfolder , file in os.walk(SourceDir):
    print("Folder : ",folder)
    copied_files = []
    cnt = 0
    for fname in file:
      src_path = os.path.join(folder , fname)
      relative = os.path.relpath(src_path,SourceDir)
      dest_path = os.path.join(DestDir , relative)
      os.makedirs(os.path.dirname(dest_path),exist_ok=True)
      shutil.copy2(src_path , dest_path)
      copied_files.append(relative)
      cnt+=1
    print("Total Copied Files : ",cnt)

def main():
  copyOperation(sys.argv[1] , sys.argv[2])

if __name__ == "__main__":
  main()