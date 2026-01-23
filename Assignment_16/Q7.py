def ChkNum(num):
 return True if num%5==0 else False 

def main():
  num = int(input("Enter Any Number : "))
  print(ChkNum(num))
  
if __name__ == "__main__":
  main()