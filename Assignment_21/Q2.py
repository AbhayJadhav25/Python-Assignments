import threading
def Maximum(lst):
  maxNum = float('-inf')
  for i in lst:
    if i > maxNum:
      maxNum = i
    
  print("Maximum NUmber = ",maxNum)


def Minimum(lst):
  minNum = float('inf')
  for i in lst:
    if i < minNum:
        minNum = i

  print("Minimum NUmber = ",minNum)
  
def main():
  print("Enter number of Elements : ")
  N = int(input())
  lst = []
  print("Enter Elements in List : ")
  for i in range(N):
    Element = int(input())
    lst.append(Element)

  Thread1 = threading.Thread(target = Maximum , args = (lst,)) 
  Thread2 = threading.Thread(target = Minimum , args = (lst,)) 

  Thread1.start()
  Thread2.start()
  Thread1.join()
  Thread2.join()

if __name__ == "__main__":
  main()