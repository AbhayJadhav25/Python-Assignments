def ChkNum(num):
  # if(num > 0):
  #   print(num,"is Positive number")
  # elif(num<0):
  #   print(num,"is Negative number")
  # else:
  #   print(num,"is zero ")
  print("Positive number") if num>0 else print("Negative number.") if num<0 else print("Number is zero")

def main():
  num = int(input("Enter Any Number : "))
  ChkNum(num)
  
if __name__ == "__main__":
  main()