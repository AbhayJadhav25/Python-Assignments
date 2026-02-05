import sys
import os

def searchWord(FileName , key):
  if(not(os.path.exists(FileName))):
    print("No such file exists.")
    return
  isFound = False
  Fobj = open(FileName , 'r')

  Data = Fobj.read().split()

  for word in Data:
    word = word.lower()
    if(word == key):
      isFound = True
      break
  if(isFound):
    print("Word Found")
  else:
    print("Not Found")

  Fobj.close()
def main():
  searchWord(sys.argv[1] , sys.argv[2])
if __name__ == "__main__":
  main()