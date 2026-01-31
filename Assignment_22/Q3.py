class Arithmetic:

  def __inti__(self):
    self.Value1 = 0
    self.Value2 = 0

  def Accept(self):
    print("Enter Two Number : ")
    value1 = int(input())
    value2 = int(input())

    self.Value1 = value1
    self.Value2 = value2

  def Addition(self):
    print(self.Value1 + self.Value2)
  
  def Substraction(self):
    print(self.Value1 - self.Value2)
  
  def Multiplication(self):
    print(self.Value1 * self.Value2)

  def Division(self):
    try:
     print(self.Value1 / self.Value2)
    except ZeroDivisionError as zobj:
     print("ERROR: ",zobj)


def main():
  Obj1 = Arithmetic()
  Obj1.Accept()
  Obj1.Addition()
  Obj1.Substraction()
  Obj1.Multiplication()
  Obj1.Division()
  print("*"*5)
  Obj2 = Arithmetic()
  Obj2.Accept()
  Obj2.Addition()
  Obj2.Substraction()
  Obj2.Multiplication()
  Obj2.Division()
  print("*"*5)
if __name__ == "__main__":
  main()