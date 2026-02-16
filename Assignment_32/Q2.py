import sys
import os
def duplicate_filename(directory):
  if(not(os.path.exists(directory))):
    print("No such file directory avilable.")
    return
  
  if(not(os.path.isdir(directory))):
    print("Unable to scan")
    return
  
  fobj = open("Answer2.txt" , "w")
 
  files = []
  for folder , subfolder , file in os.walk(directory):
    for fname in file:
      src_path = os.path.join(folder , fname)

      if fname in files :
       fobj.write(fname +"->"+src_path+"\n")
      else:
        files.append(fname)
  fobj.close()
def main():
  duplicate_filename(sys.argv[1])
if __name__ == "__main__":
  main()