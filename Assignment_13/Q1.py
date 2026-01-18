def Area(Length , Breadth):
  return Length* Breadth

def main():
  Length = int(input("Enter Length : "))
  Breadth = int(input("Enter Breadth : "))
  Res = Area(Length , Breadth)
  print("Area of Rectangle = ",Res)

if __name__ == "__main__" :
  main()
