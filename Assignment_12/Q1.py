def ChkCharacter(Char):
  ch = Char.lower()
  if(ch == 'a' or ch=='e'  or ch=='i' or ch=='o' or ch=='u'):
    print("vowels")
  else:
    print("Not Vowel")
 
def main():
  Char = input("Enter Any Number : ")
  ChkCharacter(Char)
 
if __name__ == "__main__" :
  main()