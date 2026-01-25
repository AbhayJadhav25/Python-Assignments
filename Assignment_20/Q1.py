import threading
def EvenNum():
  cnt = 0 
  i = 1
  while(cnt < 10 ):
    if(i % 2 == 0):
      print(i , end =" ")
      i+=2
      cnt+=1
    else:
      i+=1
  print()

def OddNum():
  cnt = 0 
  i = 1
  while(cnt < 10 ):
    if(not(i % 2 == 0)):
      print(i , end =" ")
      i+=2
      cnt+=1
    else:
      i+=1
  print()

def main():
  Even = threading.Thread(target = EvenNum)
  Odd = threading.Thread(target = OddNum)
  Even.start()
  Odd.start()
  Even.join()
  Odd.join()
if __name__ == "__main__":
  main()