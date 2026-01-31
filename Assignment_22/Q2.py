class Circle:
  PI = 3.14
  def __init__(self):
    self.radius = 0.0
    self.area = 0.0
    self.circumference = 0.0

  def Accept(self):
    print("Enter Radius : ")
    Radius = int(input())
    self.radius = Radius


  def CalculateArea(self):
    return Circle.PI*self.radius*self.radius

  def Calculatecircumference(self):
    return 2*Circle.PI*self.radius
  
  def Display(self):
    print("Radius : ",self.radius)
    Area = self.CalculateArea()
    Circumference = self.Calculatecircumference()
    print(f"Area of circle :{Area:.2f}")
    print(f"Circumferance of circle {Circumference}")
    

def main():
    print("Values of Object1")
    Obj1 = Circle()
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.Calculatecircumference()
    Obj1.Display()
    print("Values of Object 2")
    Obj2 = Circle()
    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.Calculatecircumference()
    Obj2.Display()
    
if __name__ == "__main__":
  main()