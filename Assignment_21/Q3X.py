import threading

counter = 0 
Lock = threading.Lock()

def incrementCounter():
  global counter

  for i in range(1000):
    Lock.acquire()
    counter+=1
    Lock.release()

def main():
  print("Enter number of threads : ")
  N = int(input())
  threads = []

  for i in range(N):
    t = threading.Thread(target = incrementCounter)
    threads.append(t)
    t.start()

  for i in threads:
    t.join()
  
  print("Value of counter : ",counter)

if __name__ == "__main__":
  main()