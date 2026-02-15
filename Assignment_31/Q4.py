import sys
import os
import shutil
def copyFiles(sourceDir , destDir , extension):
  if(not(os.path.exists(sourceDir))):
    print("Source Directory is not avilable")
    return
  
  if(not(os.path.isdir(sourceDir))):
    print("Unable to scan.")

  os.makedirs(destDir , exist_ok= True)

  for folder , subFolder , file in os.walk(sourceDir):

    for fname in file:
      src_path = os.path.join(folder , fname)
      relative = os.path.relpath(src_path , sourceDir)
      dest_path = os.path.join(destDir , relative)

      os.makedirs(os.path.dirname(dest_path),exist_ok=True)

      if(fname.endswith(extension)):
        shutil.copy2(src_path , dest_path)

def main():
  copyFiles(sys.argv[1] , sys.argv[2] , sys.argv[3])

if __name__ == "__main__":
  main()