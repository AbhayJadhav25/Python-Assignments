import sys
import os
import string
def countwords(FileName):

  if(not(os.path.exists(FileName))):
    print("Such File is not avilable.")
    return
  
  count = 0 
  Fobj = open(FileName , 'r')
  
  for line in Fobj:
    Data = line.split()

    for word in Data:
      word =  word.strip(string.punctuation)

      # if word.isalnum() or any(ch.isalpha() for ch in word ):
      if word.isalnum() or word.isalpha():
        count+=1

  print(f"File contains {count} words")
  Fobj.close()
def main():
  countwords(sys.argv[1])
if __name__ == "__main__":
  main()