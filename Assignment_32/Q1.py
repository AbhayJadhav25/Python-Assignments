import sys
import hashlib
import os
def calculateCheckSum(fname):
  hobj = hashlib.md5()

  fobj = open(fname , "rb")

  while True:
    data = fobj.read(1024)

    if not data:
      break
    else:
      hobj.update(data)
    
  return hobj.hexdigest()

  pass
def checkSum(Directory):
  if(not(os.path.exists(Directory))):
    print("No such Directory Avilable")
    return
  
  if(not(os.path.isdir(Directory))):
    print("Unable to Scan")
    return
  
  fobj = open("Answe1.txt","w")
  for folder , subfolder , file in os.walk(Directory):

    for fname in file:
      src_path = os.path.join(folder , fname)
      checksum = calculateCheckSum(src_path)
      fobj.write(f"{fname} = {checksum}\n")

def main():
  checkSum(sys.argv[1])
if __name__ == "__main__":
  main()
