def ChkNum(num):
  if(num % 2 == 0):
    print(num,"is even number")
  else:
    print(num,"is odd number")

def main():
  num = int(input("Enter Any Number : "))
  ChkNum(num)
  
if __name__ == "__main__":
  main()