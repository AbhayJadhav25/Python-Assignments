def Add(num1 , num2):
  return num1+num2
  
def main():
  num1 = int(input("Enter first Number : "))
  num2 = int(input("Enter Second Number : "))
  result = Add(num1 , num2)
  print(result)
  
if __name__ == "__main__":
  main()