import math
def  ChkPalindrome(No):
  isPalindrome = False
  Reverse = 0
  Temp = No
  while(No>0):
    rem = No%10
    Reverse = (Reverse * 10)+rem
    import math
    No = math.floor(No/10)

  if(Reverse == Temp):
    isPalindrome = True
  
  return isPalindrome

    
  return isPrime

def main():
  No = int(input("Enter Any Number : "))
  Res = ChkPalindrome(No)
  if(Res):
    print(No,"is palindrome Number")
  else:
    print(No,"is not palindrome Number")
    

if __name__ == "__main__" :
  main()