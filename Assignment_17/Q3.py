def Factorial(num):
  fact = 1
  while(num > 0):
    fact*=num
    num-=1
  return fact

def main():
  num = int(input("Enter Any Number : "))
  Result = Factorial(num)
  print(Result)

if __name__ == "__main__":
  main()