import threading
import os
def chkLower(string1):
  print("Thread ID = ",threading.get_ident())
  print("Thread Name = ",threading.current_thread().name)
  cnt = 0
  for element in string1 :
    if(element>='a' and element <='z'):
      cnt+=1
    
  print("Total Lowercase Letter : ",cnt)

def chkUpper(string1):
  print("Thread ID = ",threading.get_ident())
  print("Thread Name = ",threading.current_thread().name)
  cnt = 0
  for element in string1 :
    if(element>='A' and element <='Z'):
      cnt+=1
    
  print("Total Uppercase Letter : ",cnt)

def chkDigit(string1):
  print("Thread ID = ",threading.get_ident())
  print("Thread Name = ",threading.current_thread().name)
  cnt = 0
  for element in string1 :
    if(element>= '0'  and element <= '9'):
      cnt+=1
    
  print("Total Count Letter : ",cnt)

def main():
  string1 = input("Enter a string1 : ")

  Small =  threading.Thread(target = chkLower , args  =(string1,) , name = "Small")
  Captial = threading.Thread(target = chkUpper , args  =(string1,), name = "Captial")
  Digits = threading.Thread(target = chkDigit , args  =(string1,) , name = "Digits")

  Small.start()
  Captial.start()
  Digits.start()

  Small.join()
  Captial.join()
  Digits.join()

if __name__ == "__main__":
  main()
