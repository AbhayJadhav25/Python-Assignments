import Arithmetic

def main():
  num1 = int(input("Enter First Number : "))
  num2 = int(input("Enter Second Number : "))
  Addition = Arithmetic.Add(num1 , num2)
  Substraction = Arithmetic.Sub(num1 , num2)
  Multiplication = Arithmetic.Mult(num1 , num2)
  Division = Arithmetic.Div(num1 , num2)

  print(Addition)
  print(Substraction)
  print(Multiplication)
  print(Division)

  print("Spracil Function : ",__name__)

if __name__ == "__main__":
  main()