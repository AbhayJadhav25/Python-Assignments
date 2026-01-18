def  ArithmeticOperation(No1 , No2):
  return No1+No2 , No1-No2 , No1*No2 , No1/No2

def main():
  No1 = int(input("Enter First Number : "))
  No2 = int(input("Enter FirsSecondt Number : "))

  Addition , Substraction , Multiplication , Division = ArithmeticOperation(No1 , No2)
  
  print("Addition = ",Addition)
  print("Substraction = ",Substraction)
  print("Multiplication = ",Multiplication)
  print("Division = ",Division)

if __name__ == "__main__" :
  main()