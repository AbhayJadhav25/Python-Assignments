import itertools
def First_10_Even():
  cnt = 0
  for i in itertools.count(1):
    if(i % 2 == 0):
      print(i,end="  ")
      cnt+=1
      if cnt== 10:
        break

def main():
  First_10_Even()
  
if __name__ == "__main__":
  main()