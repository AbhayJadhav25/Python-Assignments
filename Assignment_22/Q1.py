class Demo :
  Value = 0
  def __init__(self , no1 , no2):
    self.A = no1
    self.B = no2
  
  def Fun(self):
    print("Values of Instances Vaiable : " , self.A , self.B)
  
  def Gun(self):
    print("Values of Instances Vaiaself.Ble : " , self.A , self.B)

def main():
  Obj1 = Demo(11,21)
  Obj2 = Demo(51,101)

  Obj1.Fun() #11,21
  Obj2.Fun() #51 , 101

  Obj1.Gun() #11 , 21
  Obj2.Gun() #51 , 101

if __name__ == "__main__":
  main()