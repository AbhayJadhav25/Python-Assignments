def Area(Radius):
  import math
  return math.pi * (Radius**2)

def main():
  Radius = int(input("Enter Radius : "))
  Res = Area(Radius)
  print("Area of Circle = ",Res)

if __name__ == "__main__" :
  main()
