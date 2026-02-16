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
  fobj.close()
  return hobj.hexdigest() 

def find_duplicate(dir_name):
 
  files = {}

  for folder , sub_folder , file in os.walk(dir_name):

    for fname in file:
      src_path = os.path.join(folder , fname)
      checksum = calculate_checksum(src_path)

      if checksum in files:
        files[checksum].append(src_path)

      else :
        files[checksum] = [src_path]


  return files

def duplicate_remove(dir_name):
  
  if(not(os.path.exists(dir_name))):
    print("No such file directory avilable.")
    return
  
  if(not(os.path.isdir(dir_name))):
    print("Unable to search.")
    return
  
  files = {}
  files = find_duplicate(dir_name)

  fobj = open("Answer4.txt","w")
  duplicate = []
  x = list(filter(lambda x : len(x) > 1 , files.values()))
  count = 0
  for file_list in files.values():
   
    if(len(file_list)>1):

      for duplicate_file in file_list[1:]:
        fobj.write(duplicate_file+"\n")
        os.remove(duplicate_file)
        count+=1
      
  fobj.write("Total Delted Files : "+str(count))
  fobj.close()
def main():
 duplicate_remove(sys.argv[1])


if __name__ == "__main__":
  main()