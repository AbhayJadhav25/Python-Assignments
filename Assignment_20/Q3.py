import threading
def evenNums(lst):
  even = [n for n in lst if n%2==0]
  print("Even Numbers : ",even)
  even_sum = sum(even)
  print(even_sum)

def oddNums(lst):
  odd = [n for n in lst if not(n%2==0)]
  print("odd Numbers : ",odd)
  odd_sum = sum(odd)
  print(odd_sum)

def main():
  print("Enter number of elements : ")
  N = int(input())
  lst = []
  print("Enter Elements in List : ")
  for i in range(N):
    Elements = int(input())
    lst.append(Elements)
  
  EvenList = threading.Thread(target = evenNums , args = (lst , ))
  OddList = threading.Thread(target = oddNums , args = (lst , ))

  EvenList.start()
  OddList.start()

  EvenList.join()
  OddList.join()
  
  print("Both threads have completed execution.")

if __name__ == "__main__":
  main()