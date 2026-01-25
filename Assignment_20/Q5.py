import threading
def Display1To50():
  for i in range(1 , 51):
    print(i)
  print("Thread 1 complete its Execution")

def Display50To1():
  for i in range(50 , 0 , -1):
    print(i)
  print("Thread 2 complete its Execution")
  


def main():
  Thread1 = threading.Thread(target = Display1To50)
  Thread2 = threading.Thread(target = Display50To1)

  Thread1.start()
  Thread1.join()

  Thread2.start()
  Thread2.join()

if __name__ == "__main__":
  main()