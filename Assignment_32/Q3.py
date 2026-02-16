import sys
import os
import hashlib

def calculate_checksum(src_path):
  
  hobj = hashlib.sha256()
  fobj = open(src_path , "rb")

  while True :
    data = fobj.read(1024)

    if not data:
      break
    else:
      hobj.update(data)

  return hobj.hexdigest() 


def find_duplicate(dir_name):

  if(not(os.path.exists(dir_name))):
    print("No such file directory avilable.")
    return
  
  if(not(os.path.dirname(dir_name))):
    print("Unable to search.")
    return
  
  fobj = open("Answer3.txt","w")
  files = {}

  for folder , sub_folder , file in os.walk(dir_name):

    for fname in file:
      src_path = os.path.join(folder , fname)
      checksum = calculate_checksum(src_path)

      if checksum in files:
        files[checksum].append(src_path)

      else :
        files[checksum] = [src_path]

  for _ , value in files.items():
    if(len(value)>1):
      fobj.write(value[1]+"\n")

  fobj.close()

def main():
  find_duplicate(sys.argv[1])

if __name__ == "__main__":
  main()