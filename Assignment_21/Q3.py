# Code Generate wrong output without Lock
import threading
import time

counter = 0
Lock = threading.Lock()

def incrementCounter():
  global counter
  for i in range(500):
    temp = counter
    time.sleep(0.01)
    # counter+=1
    counter = temp + 1
    


def main():
  N = int(input("Enter number of threads : "))
  threads = []

  for i in range(N):
    t = threading.Thread(target = incrementCounter)
    threads.append(t)
    t.start()

  for t in threads :
    t.join()

  print("Final Value of Counter = ",counter)

if __name__ == "__main__":
  main()